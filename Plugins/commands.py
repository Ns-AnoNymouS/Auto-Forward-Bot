import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation



#strat command

@channelforward.on_message(filters.command(["start"]))
async def start(c, m):
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START,
                           parse_mode="html",
                           reply_to_message_id=m.message_id)
