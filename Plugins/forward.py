import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def forward(c, m):
    for id in Config.CHANNEL:
       from_channel, to_channel = id.split(":")
       if m.chat.id == from_channel:
          await m.forward(to_channel)
       print(from_channel)
       print(to_channel)
    print(Config.CHANNEL)
