# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# t.me/hakutakaid
from HakuBot import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *
import asyncio
from config import BLACKLIST_GCAST

@HAKU.CHA("gcast")
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "<b>Started global broadcast...</b>")
    else:
        return await message.edit_text("<b>Berikan Sebuah Pesan atau Reply</b>")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    error += 1
    await Man.edit_text(
        f"<b>Berhasil Mengirim Pesan Ke <code>{done}</code> Grup, Gagal Mengirim Pesan Ke <code>{error}</code> Grup</b>"
    )