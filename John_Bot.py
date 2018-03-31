import asyncio
import discord
from discord.ext import commands

from base_discord_bot import Music


class John_Bot(Music):

    @commands.command()
    async def help(self):
        await self.bot.say(
        """
        I can do the following commands\n
        add : add n numbers (n1 + n2 + n3 .....)
        sub : sub n numbers (n1 - n2 - n3 .....)
        """)

    @commands.command(pass_context=False, no_pm=True)
    async def add(self, *nums):
        result = 0
        for num in nums:
            try:
                result += int(num)
            except:
                await self.bot.say("Numbers only please 2")
                break
        await self.bot.say("{} = {}".format((' + '.join(map(str, list(nums)))), result))


    @commands.command(pass_context=False, no_pm=True)
    async def sub(self, *nums):
        result = int(nums[0]) * 2
        for num in nums:
            print(num)
            try:
                result -= int(num)
            except:
                await self.bot.say("Numbers only please 2")
                break
        await self.bot.say("{} = {}".format((' - '.join(map(str, list(nums)))), result))

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description='A playlist example for discord.py')
bot.add_cog(John_Bot(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run('put token here')