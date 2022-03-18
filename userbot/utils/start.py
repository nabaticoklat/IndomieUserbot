from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption=" **Indomie Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.2@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @IndomieProject ",
                buttons=[(Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/IndomieProject"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
