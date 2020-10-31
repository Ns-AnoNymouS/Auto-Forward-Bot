import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation

@channelforward.on_message(filters.command(["start"]))
async def start(c, m)
      await m.send_message(chat_id=m.chat.id,
                           text=Translation.start,
                           parse_mode="html",
                           quote=True)
