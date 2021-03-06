import discord
import owo
import unicode_conv
from dotenv import load_dotenv
import os

load_dotenv()


class OwOizer(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if message.content.startswith('owo '):
            nonowoed = message.content[4:]
            print('%s said %s, converting!' %
                  (message.author, message.content))
            owoed = owo.owo(nonowoed)
            owoed = unicode_conv.converted(owoed)
            response = await message.channel.send(owoed)
            await response.add_reaction('🅾')
            await response.add_reaction('🇼')
            await response.add_reaction('🇴')
            herbert = client.get_emoji(743013337033343056)
            await response.add_reaction(herbert)
        elif message.content.startswith('miniowo '):
            nonowoed = message.content[8:]
            print('%s said %s, converting!' %
                  (message.author, message.content))
            owoed = owo.owo(nonowoed)
            response = await message.channel.send(owoed)
            await response.add_reaction('🅾')
            await response.add_reaction('🇼')
            await response.add_reaction('🇴')
            herbert = client.get_emoji(743013337033343056)
            await response.add_reaction(herbert)


client = OwOizer()
client.run(os.getenv('TOKEN'))
