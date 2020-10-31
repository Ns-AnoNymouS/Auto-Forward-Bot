import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.private)
async def forward(c, m):
    for id in Config.CHANNEL:
       from, to = await Config.CHANNEL[str(id)].split(":")
       print(from)
       print(to)
    print(Config.CHANNEL)
