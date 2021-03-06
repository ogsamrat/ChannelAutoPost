import asyncio
from telethon import events
from ChannelAutoPost import Config, ChannelAutoPost


@ChannelAutoPost.on(events.NewMessage(incoming=True, chats=Config.FROM_CHANNEL)) 
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
                    await event.client.send_message(Config.TO_CHANNEL, msg)
                else:                
                    await event.client.send_message(Config.TO_CHANNEL, event.text)                    
            await asyncio.sleep(2) # avoid flood waits    
        except Exception as oooo:
            print(f"Some error occured!\n\n{oooo}")
