# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import indomie_cmd
import random
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@indomie_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@IndomieGantengV3", filter=InputMessagesFilterVideo
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Asupan by** [{aku.first_name}](tg://user?id={aku.id})")

        await event.delete()
    except Exception:
        await event.edit("**Tidak dapat menemukan video asupan.**")


@indomie_cmd(pattern="desah$")
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
            caption=f"**Desahan by** [{aku.first_name}](tg://user?id={aku.id})")

        await event.delete()
    except Exception:
        await event.edit("**Tidak dapat menemukan vn desah.**")


@indomie_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@IndomieGantengV2", filter=InputMessagesFilterPhotos
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Ayang by** [{aku.first_name}](tg://user?id={aku.id})")

        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")


@indomie_cmd(pattern="makan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@IndomieGantengV4", filter=InputMessagesFilterVideo
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Laper kan lo,** [{aku.first_name}](tg://user?id={aku.id}) **Makan ampe abis ye anjing**")

        await event.delete()
    except Exception:
        await event.edit("**Tidak dapat menemukan video makanan.**")


@indomie_cmd(pattern="makanan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@IndomieGantengV4", filter=InputMessagesFilterPhotos
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Laper kan lo,** [{aku.first_name}](tg://user?id={aku.id}) **Makan ampe abis ye anjing**")

        await event.delete()
    except Exception:
        await event.edit("**Tidak dapat menemukan pap makanan.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}desah`\
        \n  •  **Function : **Mengirim voice desah secara random.\
        \n\n  •  **Syntax :** `{cmd}ayang`\
        \n  •  **Function : **Mencari ayang buat cowok yang jomblo.\
        \n\n  •  **Syntax :** `{cmd}makan`\
        \n  •  **Function : **Mencari video asmr makan.\
        \n\n  •  **Syntax :** `{cmd}makanan`\
        \n  •  **Function : **Mencari pap takjil.\
    "
    }
)
