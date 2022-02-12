# Copyright © IndomieGorengSatu
# Kalo mau dihargai, jangan hapus kredit yakak:)
# KONTOL buat lo yang hapus credit
#

from userbot import ALIVE_NAME, UPSTREAM_REPO_URL, CMD_HELP
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
REPOLINK = str(
    UPSTREAM_REPO_URL) if UPSTREAM_REPO_URL else "https://github.com/indomiegorengsatu/IndomieUserbot"
# ============================================


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "**Hai Tolol**, **Gue Make** `[ɪɴᴅᴏᴍɪᴇᴜꜱᴇʀʙᴏᴛ]` **Nich**\n"
        "⚉━━━━━━━━━━━━━━━━━━━━━━⚉\n"
        f"┌ **Repo Userbot   :** [ɢɪᴛʜᴜʙ](https://github.com/indomiegorengsatu/IndomieUserbot)\n"
        f"├ **Owner Repo     :** [ɪɴᴅᴏᴍɪᴇ](t.me/IndomieGenetik)\n"
        f"├ **UserbotVersion :** `{BOT_VER}@{branch}`\n"
        f"├ **Support        :** [sᴜᴘᴘᴏʀᴛ](https://t.me/IndomieProject)\n"
        f"└ **Channel        :** [ᴄʜᴀɴɴᴇʟ](https://t.me/IndomieStore)\n"
        "⚉━━━━━━━━━━━━━━━━━━━━━━⚉\n"
    )


CMD_HELP.update({
    "repo": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.repo`\
    \n↳ : Menampilan link Repository IndomieUserbot.",
})
