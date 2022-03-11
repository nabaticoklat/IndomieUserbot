# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import register
import random
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice


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
            caption=f"**Berhasil menemukan Video**.")


@register(outgoing=True, pattern=r"^\.desah$")
async def _(event):
    user = await bot.get_me()
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@DESAHANFCE", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Nih kak (tg://user?id={user.id}) Desahnya",
        )

CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        f\n\n  •  **Syntax :** `.asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
    "
    }
)
