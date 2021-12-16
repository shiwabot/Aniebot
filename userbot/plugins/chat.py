from userbot.plugins.sql_helper import chatbot_sql as sql

AI_API_KEY = os.environ.get("AI_API_KEY", sk-vcZIC3jAhTXVJBET3BlbkFJtrBdYkQVwmQx0IG3v76d)

CoffeeHouseAPI = API(AI_API_KEY)
api_client = LydiaAI(CoffeeHouseAPI)
import html

# AI module using Intellivoid's Coffeehouse API by @TheRealPhoenix
from time import sleep, time


from coffeehouse.api import API
from coffeehouse.exception import CoffeeHouseError as CFError
from coffeehouse.lydia import LydiaAI

def chatbot(event):
    global api_client
    msg = event.effective_message
    chat_id = event.chat_id
    is_chat = sql.is_chat(chat_id)
    if not is_chat:
        return
    if msg.text and not msg.document:
        sesh, exp = sql.get_ses(chat_id)
        query = msg.text
        try:
            if int(exp) < time():
                ses = api_client.create_session()
                ses_id = str(ses.id)
                expires = str(ses.expires)
                sql.set_ses(chat_id, ses_id, expires)
                sesh, exp = sql.get_ses(chat_id)
        except ValueError:
            pass
        try:
            bot.send_chat_action(chat_id, action="typing")
            rep = api_client.think_thought(sesh, query)
            sleep(0.3)
            msg.reply_text(rep, timeout=60)
        except CFError as e:
            pass

@bot.on(admin_cmd(pattern="adai(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="adai(?: |$)(.*)", allow_sudo=True))
def add_chat(event):
    global api_client
    chat = event.effective_chat
    msg = event.effective_message
    user = event.sender_id
    is_chat = sql.is_chat(chat.id)
    if chat.type == "private":
        msg.reply_text("You can't enable AI in PM.")
        return
    if not is_chat:
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        sql.set_ses(chat.id, ses_id, expires)
        await eod("AI successfully enabled for this chat!")
        message = (
            f".."
            f"#AI_ENABLED\n"
            f"Admin"
        )
        return message
    else:
        await eod("AI is already enabled for this chat!")
        return
