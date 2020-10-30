import pyrogram
from pyrogram import filters
from bot import channelforward


@channelforward.on_message(filter.private)
async def forward(c, m):
    print("working")
