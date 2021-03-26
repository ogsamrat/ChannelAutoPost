import asyncio
from contextlib import suppress
from telethon import events
from ChannelAutoPost import *


@channel_poster.on(events.NewMessage(incoming=True, chats=Config.FROM_CHANNEL)) 
async def autopost(event): 
    if not event.is_private:
        try:
            if event.media:
                if Config.REMOVE_POST_CAPTION:
                    caption = Config.CUSTOM_FOOTER if Config.CUSTOM_FOOTER else None
                    await event.client.send_file(Config.TO_CHANNEL, event.media, caption=caption) 
                elif Config.CUSTOM_FOOTER:
                    caption = str(event.text) + "\n\n" + str(Config.CUSTOM_FOOTER)           
                    await event.client.send_file(Config.TO_CHANNEL, event.media, caption=caption) 
                else:    
                    await event.client.send_file(Config.TO_CHANNEL, event.media, caption=event.text) 
            else:
                if Config.CUSTOM_FOOTER:
                    msg = str(event.text) + "\n\n" + str(Config.CUSTOM_FOOTER)
                    await event.client.send_message(Config.TO_CHANNEL, msg, link_preview=False)
                else:                
                    await event.client.send_message(Config.TO_CHANNEL, event.message, link_preview=False)                    
            await asyncio.sleep(5) # avoid flood waits    
        except Exception as oooo:
            with suppress(Exception):
                await event.client.send_message(Config.OWNER_ID, f"An error occured while forwarding message to `{Config.TO_CHANNEL}`:\n\nError:\n`{oooo.__class__.__name__}: {oooo}`")
            print("An error occured, check your PM to get error traceback!")
