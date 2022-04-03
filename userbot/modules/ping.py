# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
#
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, indomie_cmd


absen = [
    "**Eh ada Owner keren**",
    "**Hi Tuan, kemana sj?** 🤗",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Saya slalu ada buat Tuan Owner** 🥵",
    "**Hadir kak** 😉",
    "**Jangan kemana mana lagi ya bang**",
    "**Pas banget bang, aku lagi kangen**",
    "**Hadir bang** 😁",
    "**Sokap lo tai** 😡",
    "**Hadir sayang** 😚",
    "**Hadir kak maap telat** 🥺",
    "**Bang owner on juga akhirnya** 🥵",
]

brb = [
    "**Bang owner mau off.**",
    "**Jangan off dong bang.**",
    "**Bang, mau kemana?**",
    "**Jangan lama lama bang**",
    "**Siap bang.**",
    "**Yah udah off aja bang.**",
    "**Off lagi, mau ngewe ya?**",
    "**Bang indomie, lagi ange kah?**",
    "**Jangan lupa makan bang.**",
    "**Yah pasti mao ngocok ni.**",
    "**Jangan off terus lah bang.**",
    "**Mau nonton bokep kah?**",
    "**Mau nonton lipshoe ya?**",
    "**Bang Ganteng telah off.**",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@indomie_cmd(pattern="ping$")
async def indomie(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sabar goblok.__")
    await pong.edit("__Sabar goblok..__")
    await pong.edit("__Sabar goblok...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.edit(
        f"**╼══❃ ɪɴᴅᴏᴍɪᴇᴜꜱᴇʀʙᴏᴛ ❃══╾ **\n\n"
        f"** ▹  Pɪɴɢᴇʀ  : ** "
        f"`%sms` \n"
        f"** ▹  Uᴘᴛɪᴍᴇ  : ** "
        f"`{uptime}` \n"
        f"** ▹  Oᴡɴᴇʀ   : ** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@indomie_cmd(pattern="pings$")
async def redis(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("Assalamualaikum..")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**KONTOOLLLL!!**\n**KEKUATAN KONTOL** : `%sms`\n**DURASI KONTOL** : `{uptime}🕛`" % (duration))


@indomie_cmd(pattern="sping$")
async def redis(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**✲**")
    await pong.edit("**✲✲**")
    await pong.edit("**✲✲✲**")
    await pong.edit("__KONTOL__")
    await pong.edit("🍾")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.edit(
        f"**[{user.first_name}](tg://user?id={user.id})**        \n"
        f"**➾Kecepatan : ** '%sms'  \n"
        f"**➾Branch : ** 'IndomieUserbot` \n" % (duration)
    )


@indomie_cmd(pattern="lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"✧ **-ꜱɪɢɴᴀʟ- :** "
        f"`%sms` \n"
        f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
        f"`{uptime}` \n" % (duration)
    )


@indomie_cmd(pattern="xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**♨ɪɴᴅᴏᴍɪᴇᴜꜱᴇʀʙᴏᴛ**\n"
        f"➾ __Signal__    __:__ "
        f"`%sms` \n"
        f"➾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@indomie_cmd(pattern="sinyal$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Mengecek Sinyal...**")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.edit(
        f"**♨ɪɴᴅᴏᴍɪᴇᴜꜱᴇʀʙᴏᴛ**\n\n"
        f"** ▹  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ▹  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ▹  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@indomie_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@indomie_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("**◕‿- PONG!!🏓**")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    user = await pong.client.get_me()
    await pong.edit(f"**Owner : [{user.first_name}](tg://user?id={user.id})**\n📗 `%sms`" % (duration))


@indomie_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**BABI!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(pattern=r"^\.absen$", sudo=True)
async def memek(jembut):
    await jembut.reply(choice(absen))


# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡



CMD_HELP.update(
    {
        "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` | `.pings` | `.lping` | `.xping` | `.sinyal` | `.sping` | `.pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)
