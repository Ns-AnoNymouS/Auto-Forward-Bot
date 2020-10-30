import pyrogram
from pyrogram import filters
from bot.py import channelforward


@channelforward.on_message(filter.private)
async def forward(c, m):
    print("working")
