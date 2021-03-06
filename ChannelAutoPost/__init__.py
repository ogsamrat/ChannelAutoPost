from .Config import Config
from telethon import TelegramClient
from telethon.sync import TelegramClient as StringSessionMaker
from telethon.sessions import StringSession


if Config.USE_AS_USERBOT:
    if Config.BOT_TOKEN is None or Config.APP_ID is None or Config.APP_HASH is None:
        print("Important env variables missing... quitting!")   
        quit(1) 
    ChannelAutoPost = TelegramClient("CAPBOT", Config.APP_ID, Config.APP_HASH)
else:
    with StringSessionMaker(StringSession(), Config.APP_ID, Config.APP_HASH) as autopost:
        session = autopost.session.save()
    ChannelAutoPost = TelegramClient(StringSession(session), Config.APP_ID, Config.APP_HASH)
