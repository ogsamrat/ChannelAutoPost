import logging

from telethon import events
from ChannelAutoPost import Config
from telethon import events, Button
from sys import argv
from ChannelAutoPost.plugins import *

logging.basicConfig(level=logging.INFO)


@ChannelAutoPost.on(events.NewMessage(pattern="^/start"))
async def start(event):
    await event.reply(
        f"Hello! I am a auto channel post bot, you cannot use me but you can however deploy your instance from the source given below", 
        buttons=[Button.url("Source", "https://github.com/EmiliaDevs/ChannelAutoPost")], 
        )


@ChannelAutoPost.on(events.NewMessage(pattern="^/help"))
async def help(event):
    await event.reply("Get help from /start")


if __name__ == "__main__":
    ChannelAutoPost.start()
    if len(argv) not in (1, 3, 4):
        ChannelAutoPost.disconnect()
    else:
        print("You bot is now running, now pay 69$ to @GodDrick else heck... lel")
        ChannelAutoPost.run_until_disconnected()    