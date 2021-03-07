import logging

from telethon import events
from ChannelAutoPost import Config, ChannelAutoPost
from telethon import events, Button
from sys import argv
from ChannelAutoPost.plugins import *

logging.basicConfig(level=logging.INFO)


@ChannelAutoPost.on(events.NewMessage(pattern="^/start"))
async def start(event):
    await event.reply(
        f"Hello! I am a **Channel Auto Post bot**, I can help you manage your channel efficiently. You need to deploy your own instance for that from the source given below! :)", 
        buttons=[
            [
                Button.url("Source", "https://github.com/EmiliaDevs/ChannelAutoPost"),
                Button.url("Developer", "https://telegram.me/GodDrick"),                
            ]
        ], 
    )


@ChannelAutoPost.on(events.NewMessage(pattern="^/help"))
async def help(event):
    await event.reply("These are the things I can do,\n\n"
                      "> Forward posts of one or more channels to provided channel!\n"
                      "> Add custom footer at last of all vew posts\n"
                      "> Remove all of the new media post caption as per user's choice"
                      "> Can be used as an userbot, therefore you just need to join the channels from where to leech and "
                      "need not to be admin in them, you just need to admin in the forwarding or `TO_CHANNEL` channel!"
                      "\n\n**NOTE:** You have to add the bot in both the channels from where to forward and to where forward! [For bot instances and not userbots]"
                      "\n\nLiked the bot? Give the [repo](github.com/EmiliaDevs/ChannelAutoPost) a star! With ❤️ by @GodDrick",
                      link_preview=False,
                     )


if __name__ == "__main__":
    ChannelAutoPost.start(bot_token=Config.BOT_TOKEN)
    if len(argv) not in (1, 3, 4):
        ChannelAutoPost.disconnect()
    else:
        print("You bot is now running, now pay 69$ to @GodDrick else heck... lel")
        ChannelAutoPost.run_until_disconnected()    
