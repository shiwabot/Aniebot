import logging
import os
import random

from moviepy.editor import VideoFileClip
from PIL import Image, ImageOps

from ..helpers.tools import media_type
from ..utils import edit_or_reply
from .helpers.runner import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        catevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        catevent = event
    catmedia = None
    catfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(catfile):
        os.remove(catfile)
    if mediatype == "Photo":
        catmedia = await reply.download_media(file="./temp")
        im = Image.open(catmedia)
        im.save(catfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, catfile, thumb=-1)
    elif mediatype == "Sticker":
        catmedia = await reply.download_media(file="./temp")
        if catmedia.endswith(".tgs"):
            catcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{catmedia}' '{catfile}'"
            stdout, stderr = (await runcmd(catcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif catmedia.endswith(".webp"):
            im = Image.open(catmedia)
            im.save(catfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, catfile, thumb=-1)
        if not os.path.exists(catfile):
            catmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(catfile, 0.1)
            except Exception:
                clip = clip.save_frame(catfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            catmedia = await reply.download_media(file="./temp")
            im = Image.open(catmedia)
            im.save(catfile)
    if catmedia and os.path.lexists(catmedia):
        os.remove(catmedia)
    if os.path.lexists(catfile):
        return catevent, catfile, mediatype
    return catevent, None


async def vid_to_gif(inputfile, outputfile, speed=None, starttime=None, endtime=None):
    try:
        clip = VideoFileClip(inputfile)
        if starttime is not None and endtime is not None:
            clip = clip.subclip(int(starttime), int(endtime))
        if speed is not None:
            clip = clip.speedx(float(speed))
        clip.write_gif(outputfile, logger=None)
        return outputfile
    except Exception as e:
        LOGS.error(e)
        return None


async def r_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((i, h))
        img2 = img2.resize((w - i, h))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        outframes.append(temp)
    return outframes


async def l_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = ImageOps.mirror(img1.resize((i, h)))
        img2 = ImageOps.mirror(img2.resize((w - i, h)))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        temp = ImageOps.mirror(temp)
        outframes.append(temp)
    return outframes


async def ud_frames(image, w, h, outframes, flip=False):
    for i in range(1, h, h // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((w, i))
        img2 = img2.resize((w, h - i))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (0, i))
        if flip:
            temp = ImageOps.flip(temp)
        outframes.append(temp)
    return outframes


async def spin_frames(image, w, h, outframes):
    image.thumbnail((512, 512), Image.ANTIALIAS)
    img = Image.new("RGB", (512, 512), "black")
    img.paste(image, ((512 - w) // 2, (512 - h) // 2))
    image = img
    way = random.choice([1, -1])
    for i in range(1, 60):
        img = image.rotate(i * 6 * way)
        outframes.append(img)
    return outframes


async def invert_frames(image, w, h, outframes):
    image.convert("RGB")
    invert = ImageOps.invert(image)
    outframes.append(image)
    outframes.append(invert)
    return outframes


from telethon import functions, types

from ..helpers.logger import logging

LOGS = logging.getLogger(__name__)


async def unsavegif(event, sandy):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=sandy.media.document.access_hash,
                    file_reference=sandy.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        LOGS.info(str(e))
