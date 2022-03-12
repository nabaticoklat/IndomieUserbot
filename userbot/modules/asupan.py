# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from time import sleep
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import register
import random
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Video.**")

        await event.edit()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan.**")
        sleep(2)


@register(outgoing=True, pattern=r"^\.desah$")
async def _(event):
    try:
        desahannya = [
            desah
            async for desah in event.client.iter_messages(
                "@DESAHANFCE", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahannya),
            caption=f"**Berhasil menemukan desahannya.**")

        await event.edit()
    except Exception:
        await event.edit("**Tidak bisa menemukan vn desah.**")
        sleep(2)


@register(outgoing=True, pattern=r"^\.ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Nih ayang mu [{DEFAULTUSER}](tg://user?id={aing.id}).**")

        await event.edit()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")
        sleep(2)


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}desah`\
        \n  •  **Function : **Untuk Mengirim voice desah secara random.\
        \n\n  •  **Syntax :** `{cmd}ayang`\
        \n  •  **Function : **Untuk Mencari ayang buat cowok yang jomblo.\
    "
    }
)
