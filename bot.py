import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import uvloop
uvloop.install()
from config import Config
from pyrogram import Client 


class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


if __name__ == "__main__" :
    channelforward().run()
