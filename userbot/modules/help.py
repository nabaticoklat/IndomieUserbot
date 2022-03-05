# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(indomie):
    """ For .help command,"""
    args = indomie.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await indomie.edit(str(CMD_HELP[args]))
        else:
            await indomie.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(50)
            await indomie.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ✦  "
        await indomie.edit(f"**♨ List Help [ɪɴᴅᴏᴍɪᴇᴜꜱᴇʀʙᴏᴛ](https://github.com/indomiegorengsatu/IndomieUserbot):**\n\n"
                           f"**♨ ʙᴏᴛ ᴏᴡɴᴇʀ {DEFAULTUSER}**\n**♨ Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                           "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                           f"✦ {string}✦\n\n")
        await indomie.reply(
            "\n✎ **ɴᴏᴛᴇꜱ :** `<.help ping>` **Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha...**")

        await asyncio.sleep(50)
        await indomie.delete()
