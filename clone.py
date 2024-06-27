from .. import loader, utils

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
        
        async for msg in self.client.iter_messages(source_channel):
            if msg.text:
                await self.client.send_message(target_channel, msg.text)
            elif msg.media:
                await self.client.send_file(target_channel, msg.media)
        
        await message.edit("<b>Cloning complete!</b>")