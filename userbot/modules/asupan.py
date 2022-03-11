# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.events import register
import random
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice


@register(outgoing=True, pattern=r"^\.asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Gabutnyazaen", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Video**.")

        await event.edit()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@register(outgoing=True, pattern=r"^\.desah$")
async def _(event):
    try:
        desahan = [
            desah
            async for desah in event.client.iter_messages(
                "@DESAHANFCE", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahan),
            caption=f"**Nih kak [{owner}](tg://user?id={chat.id}) Desahannya.**")

        await event.edit()
    except Exception:
        await event.edit("Tidak bisa menemukan vn desah.")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}desah`\
        \n  •  **Function : **Untuk Mengirim voice desah secara random.\
    "
    }
)
