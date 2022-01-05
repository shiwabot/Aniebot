import io
import math

from PIL import Image
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    MessageMediaPhoto,
)

from userbot.utils import *

from . import *

legend = Config.CUSTOM_STICKER_PACK_NAME


@bot.on(admin_cmd(outgoing=True, pattern="png"))
@bot.on(sudo_cmd(pattern="png", allow_sudo=True))
async def kang(args):
    user = await bot.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    is_anim = False

    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            photo = io.BytesIO()
            photo = await bot.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            await args.edit(f"`Wait A Sec Its On Process`")
            photo = io.BytesIO()
            await bot.download_file(message.media.document, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.media.document.attributes
            ):
                message.media.document.attributes[1].alt
        elif "tgsticker" in message.media.document.mime_type:
            await bot.download_file(message.media.document, "AnimatedSticker.tgs")

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    attribute.alt

            is_anim = True
            photo = 1
        else:
            await args.edit("`Unsupported File!`")
            return
    else:
        await args.edit("`No Check One More time`")
        return

        file = io.BytesIO()

        if not is_anim:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")
        else:
            pass
        if is_anim:
            await bot.send_file(arg.chat_id, "AnimatedSticker.tgs")
            remove(args.chat_id, "AnimatedSticker.tgs")
        else:
            file.seek(0)
            await bot.send_file(args.chat_id, file, force_document=True)
    #  await bot.send_file(args.chat_id, packnick, caption=f"Hello")


async def resize_photo(photo):
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image
