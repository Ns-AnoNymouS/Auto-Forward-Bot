import pyrogram
from pyrogram import Filters
from bot.py import channelforward


@channelforward.on_message()
async def forward(c, m):
