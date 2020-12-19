import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


import pyrogram
from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation


########################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command(["start"]))
async def start(c, m):
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START,
                           parse_mode="html",
                           disable_web_page_preview=True,
                           reply_to_message_id=m.message_id)

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command(["about"]))
async def about(c, m):
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.ABOUT,
                           parse_mode="html",
                           disable_web_page_preview=True,
                           reply_to_message_id=m.message_id)

################################################################################################################################################################################################################################################
