""" Userbot module for other small commands. """
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import indomie_cmd


@indomie_cmd(pattern="lhelp$")
async def usit(e):
    aku = await e.client.get_me()
    await e.edit(
        f"**Halo [{aku.first_name}](tg://user?id={aku.id}) Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n┌ [Indomie](t.me/IndomieGenetik)"
        "\n├ [Support](t.me/IndomieProject)"
        "\n├ [IndomieStore](t.me/IndomieStore) `Jasa Bikin Bot.`"
        "\n├ [Repo](https://github.com/indomiegorengsatu/IndomieUserbot)"
        "\n└ [Instagram](instagram.com/w1thmyluv)")


@indomie_cmd(pattern="vars$")
async def var(m):
    await m.edit(
        f"**Ini Daftar Vars Dari [IndomieUserbot](https://github.com/indomiegorengsatu/IndomieUserbot):**\n"
        "\n┌ [DAFTAR VARS](https://raw.githubusercontent.com/IndomieGorengSatu/IndomieUserbot/IndomieUserbot/varshelper.txt)"
        "\n├ [Support](t.me/IndomieProject)"
        "\n├ [IndomieStore](t.me/IndomieStore) `Jasa Bikin Bot.`"
        "\n└ [Repo](https://github.com/indomiegorengsatu/IndomieUserbot)")


CMD_HELP.update({
    "rehelper":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}lhelp`\
    \n↳ : Meminta Bantuan.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vars` :\
    \n↳ : Melihat vars dari `IndomieUserbot`."
})
