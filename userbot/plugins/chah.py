import html

from coffeehouse.api import API
from coffeehouse.lydia import LydiaAI
from telegram import Update
from telegram.ext import CallbackContext
from telegram.utils.helpers import mention_html

from userbot.plugins.sql_helper import chatbot_sql as sql

SUPPORT_CHAT = "Legend_Userbot"
OWNER_ID = "2082798662"
AI_API_KEY = os.environ.get(
    "AI_API_KEY", sk - vcZIC3jAhTXVJBET3BlbkFJtrBdYkQVwmQx0IG3v76d
)
CoffeeHouseAPI = API(AI_API_KEY)
api_client = LydiaAI(CoffeeHouseAPI)


@bot.on(admin_cmd(pattern="chatbot(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="chatbot(?: |$)(.*)", allow_sudo=True))
def add_chat(update: Update, context: CallbackContext):
    global api_client
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user
    is_chat = sql.is_chat(chat.id)
    if chat.type == "private":
        msg.reply_text("You can't enable AI in PM.")
        return

    if not is_chat:
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        sql.set_ses(chat.id, ses_id, expires)
        msg.reply_text("AI successfully enabled for this chat!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#AI_ENABLED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    else:
        msg.reply_text("AI is already enabled for this chat!")
        return ""
