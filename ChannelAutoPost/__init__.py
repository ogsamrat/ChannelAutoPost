from .Config import Config
from telethon import TelegramClient
from telethon.sessions import StringSession


if not Config.USE_AS_USERBOT:
    if Config.BOT_TOKEN is None or Config.APP_ID is None or Config.APP_HASH is None:
        print("Important env variables missing... quitting!")   
        quit(1) 
    ChannelAutoPost = TelegramClient("CAPBOT", Config.APP_ID, Config.APP_HASH)
else:
    if Config.SESSION is None or Config.APP_ID is None or Config.APP_HASH is None:
        print("Important env variables missing... quitting!")   
        quit(1)     
    ChannelAutoPost = TelegramClient(StringSession(Config.SESSION), Config.APP_ID, Config.APP_HASH)
