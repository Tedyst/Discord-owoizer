import discord
import owo
import unicode_conv


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


client = OwOizer()
client.run('NzQ3NDUzNDAyMzk2NDkxODU3.X0PGOg.7nLzFpy_OlGvUurLc6pP0Ju7IaA')
