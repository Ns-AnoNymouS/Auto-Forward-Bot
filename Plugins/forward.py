import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.private)
async def forward(c, m):
    for id in Config.CHANNEL:
       from_channel, to_channel = id.split(":")
       print(from_channel)
       print(to_channel)
    print(Config.CHANNEL)
