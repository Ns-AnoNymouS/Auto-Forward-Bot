import pyrogram
from pyrogram import filters
from bot import channelforward
from Config import Config 

@channelforward.on_message(filters.private)
async def forward(c, m):
    print("Config.CHANNEL")
