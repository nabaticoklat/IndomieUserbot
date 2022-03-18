# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import DEFAULTUSER
from userbot.events import register
import random
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Asupan by [{DEFAULTUSER}](tg://user?id={aku.id})**")

        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan.**")


@register(outgoing=True, pattern=r"^\.desah$")
async def _(event):
    try:
        desahannya = [
            desah
            async for desah in event.client.iter_messages(
                "@IndomieGanteng", filter=InputMessagesFilterVoice
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahannya),
            caption=f"**Desahan by [{DEFAULTUSER}](tg://user?id={aku.id})**")

        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan vn desah.**")


@register(outgoing=True, pattern=r"^\.ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Ayang by [{DEFAULTUSER}](tg://user?id={aku.id})**")

        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")


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
