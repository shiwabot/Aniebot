import asyncio

from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

from . import *

file1 = "https://telegra.ph/file/7b901525920ba2ed6a534.jpg"
file2 = "https://telegra.ph/file/e6b71c2f7cd63c7b0dadf.jpg"
file3 = "https://telegra.ph/file/1a0e01965304e16bc8993.jpg"
file4 = "https://telegra.ph/file/a73639ead72c9d3e36566.jpg"

ny_caption = "╭╮╱╭╮\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n┃┃╱┃┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\n╭╮╱╱╭╮\n┃╰╮╭╯┃\n╰╮╰╯╭╯\n╱╰╮╭╯\n╱╱┃┃\n╱╱╰╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭╮╭╮╭╮\n┃┃┃┃┃┃\n┃┃┃┃┃┃\n┃╰╯╰╯┃\n╰╮╭╮╭╯\n╱╰╯╰╯\n╭╮╱╱╭╮\n┃╰╮╭╯┃\n╰╮╰╯╭╯\n╱╰╮╭╯\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭━━━ \n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭╮╭╯\n┃┃┃╰╮\n╰╯╰━╯\n"
edit_time = 5


@bot.on(admin_cmd(pattern="happyny(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good Morning")
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                on = await bot.send_file(chat, file=file1, caption=ny_caption)
                await asyncio.sleep(edit_time)
                ok = await bot.edit_message(chat, on, file=file2)
                await asyncio.sleep(edit_time)
                ok2 = await bot.edit_message(chat, ok1, file=file3)
                await asyncio.sleep(edit_time)
                ok3 = await bot.edit_message(chat, ok1, file=file4)
                done += 1
            except:
                lol += 1
    await event.reply(
        f"🤗 ᵃᵈᵛᵃⁿᶜᵉ💞\n   ✨️ ʰᵃᵖᵖʸ ⁿᵉʷ ʸᵉᵃʳ✨️\n          💫 ᵐᵃʸ ᵗʰᵉ💫\n           🦋ⁿᵉʷ ʸᵉᵃʳ🦋\n          😘 ᵇˡᵉˢˢ ʸᵒᵘ😘\n  🤍🕊️ ʷⁱᵗʰ ʰᵉᵃˡᵗʰ🕊️🤍\n           🥳 ᵖʳᵒˢᵖᵉʳⁱᵗʸ🥳\n🥰🥰ᵃⁿᵈ ʰᵃᵖᵖⁱⁿᵉˢˢ🥰🥰\n"
    )


CmdHelp("new year").add_command(
    "happyny", None, "Wishs Happy New Year in all groups just one command"
).add_info("HAPPY NEW YEAR Wish Command").add_warning("Harmless Module✅").add_type(
    "Addons"
).add()
