from .. import loader, utils
import asyncio

class CloneChannelMod(loader.Module):
    """Clone messages from one channel to another"""
    strings = {"name": "CloneChannel"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def clonecmd(self, message):
        """Clone messages from source to target channel"""
        args = utils.get_args(message)
        if len(args) != 2:
            await message.edit("<b>Usage: .clone <source_channel> <target_channel></b>")
            return
        
        source_channel = args[0]
        target_channel = args[1]
        
        try:
            async for msg in self.client.iter_messages(source_channel):
                try:
                    if msg.text:
                        await self.client.send_message(target_channel, msg.text)
                    elif msg.media:
                        # Додайте затримку перед кожним відправленням медіафайлу
                        await asyncio.sleep(2)  # Наприклад, затримка 2 секунди
                        await self.client.send_file(target_channel, msg.media)
                    
                except Exception as e:
                    await message.edit(f"<b>Failed to clone message: {str(e)}</b>")
                    await asyncio.sleep(5)  # Затримка перед наступною спробою

        except Exception as ex:
            await message.edit(f"<b>Error: {str(ex)}</b>")
            return

        await message.edit("<b>Cloning complete!</b>")
