#Created By HakutakaID # TELEGRAM t.me/hakutakaid
from HakuBot import *
from pyrogram import *
from pyrogram.types import *
from config import prefix, DEVS

async def devs_cmdp(_, client, message):
    sudo_users = DEVS
    is_user = message.from_user if message.from_user else message.sender_chat
    is_self = bool(message.from_user and message.from_user.is_self or getattr(message, "outgoing", False))
    return is_user.id in sudo_users or is_self

class HAKU:
    @staticmethod
    def CHA(command, filter=None):
        if filter is None:
            filter = filters.create(devs_cmdp)
        def decorator(func):
            @ubot.on_message(filters.command(command, prefix) & filter)
            async def wrapped_func(client, message):
                return await func(client, message)
            return wrapped_func
        return decorator