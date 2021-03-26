import os

class Config(object):
    USE_AS_USERBOT = bool(os.environ.get("USE_AS_USERBOT", False))
    APP_ID = int(os.environ.get("APP_ID"))
    APP_HASH = os.environ.get("APP_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION = os.environ.get("SESSION", None)    
    OWNER_ID = int(os.environ.get("OWNER_ID"))    
    FROM_CHANNEL = set(int(x) for x in os.environ.get("FROM_CHANNEL").split())
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL"))
    REMOVE_POST_CAPTION = bool(os.environ.get("REMOVE_POST_CAPTION"))
    CUSTOM_FOOTER = os.environ.get("CUSTOM_FOOTER")
    
