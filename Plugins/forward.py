import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def forward(c, m):
    # Forwarding the messages to the channel

    for id in Config.CHANNEL:
       from_channel, to_channel = id.split(":")
       if m.chat.id == int(from_channel):
          await m.forward(int(to_channel), as_copy=True)
          print("Forwarded a message from", from_channel, "to", to_channel)
          asyncio.sleep(1)
