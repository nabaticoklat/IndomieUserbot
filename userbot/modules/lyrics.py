# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import os
import lyricsgenius

from userbot.events import register
from userbot import CMD_HELP, GENIUS, lastfm, LASTFM_USERNAME
from pylast import User

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@register(outgoing=True, pattern="^.lyrics (?:(now)|(.*) - (.*))")
async def lyrics(lyric):
    await lyric.edit("`Bentar lagi di ambil mek...`")
    if GENIUS is None:
        await lyric.edit(
            "`Provide genius access token to Heroku ConfigVars...`")
        return False
    if lyric.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            await lyric.edit(
                "`Gue Ga Nemu Apapun di Lastfm scrobbling cuy...`"
            )
            return False
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = lyric.pattern_match.group(2)
        song = lyric.pattern_match.group(3)
    await lyric.edit(f"`Sedang Mencari {artist} - {song}...`")
    songs = genius.search_song(song, artist)
    if songs is None:
        await lyric.edit(f"`Lagu`  **{artist} - {song}**  `Tidak Ditemukan...`")
        return False
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lirik nya Terlalu Panjang, Liat Di File Yang Gua kirim Aja.`")
        with open("lyrics.txt", "w+") as f:
            f.write(
                f"Permintaan Pencarian: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
        return True
    else:
        await lyric.edit(
            f"**Permintaan Pencarian**:\n`{artist}` - `{song}`"
            f"\n\n```{songs.lyrics}```"
        )
        return True


CMD_HELP.update({
    "lyrics":
    "`.lyrics` **<nama artis> - <judul lagu>**"
    "\nUsage: Mendapatkan Lirik Yang Sesuai Dengan Artis Dan Lagu."
    "\n\n`.lyrics now`"
    "\nUsage: Mendapatkan Lirik Dan Artis Dari lastfm scrobbling Saat Ini."
})
