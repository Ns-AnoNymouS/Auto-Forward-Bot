import pyrogram
from pyrogram.types import filters
from bot.py import channelforward


@channelforward.on_message(filter.private)
async def forward(c, m):
    print("working")
