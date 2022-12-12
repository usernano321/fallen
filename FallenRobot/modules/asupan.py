# ⚠️ © @greyyvbss 

# ⚠️ Don't Remove Credits

import os

import random

from pyrogram import Client, filters

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from FallenRobot.events import register

from FallenRobot import telethn as tbot, ubot2                 

@register(pattern="^/asupan ?(.*)")

async def _(event):

    memeks = await event.reply("**Mencari Video Asupan...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@Database_TonicUbot", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Asupan nya Kak 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Asupannya gaada komsol")
