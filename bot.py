import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "auto",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )

    app.run()

