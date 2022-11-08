from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH")
      API_ID = int(getenv("API_ID", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))