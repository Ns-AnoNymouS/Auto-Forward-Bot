import pyrogram
from pyrogram import Filters
from bot.py import channelforward


@channelforward.on_message(Filter.private)
async def forward(c, m):
    print("working")
