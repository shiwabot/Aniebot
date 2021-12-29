import os
import sys

import telethon.utils
from telethon import TelegramClient

from userbot import LOGS, LEGENDversion, bot
from userbot.Config import Config
from var import Var

from .start import legends, hekp, module, assistants, addons, abuses, spams, killer, install

os.system("pip install telethon==1.24.0")
l2 = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"
l1 = Config.COMMAND_HAND_LER

perf = "[ †hê Lêɠêɳ̃dẞø† ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting LegendBot ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 LegendBot Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")


bot.loop.run_until_complete(killer())
bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(install())

print(
    f"""
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @Legend_Userbot
║┣⪼ CREATOR - @The_LegendBoy
║┣⪼ LEGENDBOT - {LEGENDversion}
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

bot.loop.run_until_complete(legends())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
