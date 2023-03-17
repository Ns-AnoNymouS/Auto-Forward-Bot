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
            name="CHANNELFORWARD",@Jedle707
            bot_token=self.BOT_TOKEN,5743390719:AAEJeW5d-DLH1_kC93snhweO2xXUcrsHUQ0
            api_id=self.API_ID,22056986
            api_hash=self.API_HASH,621b3f64ef181561f5e8382657a23f0f
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
