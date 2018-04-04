import asyncio
import discord
from discord.ext import commands

from base_discord_bot import Music


class John_Bot(Music):
    @commands.command()
    async def info(self):
        await self.bot.say(
            """
            I can do the following commands\n
            ?Calc : Standard Calculator (NOT Scientific, uses python operators)\n
            """)

    """
    Below Is old redundant code for addition and sub traction. New method Calc does all the below and some more.

    I use eval but do check that it is only mathimatical operators or numbers which are use, so hopefully hackers can't
    destroy this program. Never say never though!
    """

    # @commands.command(pass_context=False, no_pm=True)
    # async def add(self, *nums):
    #     try:
    #         result = sum(map(int, nums))
    #     except:
    #         await self.bot.say("Numbers only please")
    #     await self.bot.say("{} = {}".format((' + '.join(map(str, list(nums)))), result))
    #
    # @commands.command(pass_context=False, no_pm=True)
    # async def sub(self, *nums):
    #     try:
    #         nums = list(map(int, nums))
    #         result = nums[0] - sum(nums[1:])
    #     except:
    #         await self.bot.say("Numbers only please")
    #     await self.bot.say("{} = {}".format((' - '.join(map(str, list(nums)))), result))

    @commands.command(pass_context=True, no_pm=True)
    async def MyEntrance(self, ctx, member: discord.Member, channel: discord.Channel):
        """
        Cannot get bot to move voice channel once it is connected to a voice channel.
        Solution is to perhaps to disconnect bot after it plays the message.

        """

        # try:
        #     voice = await bot.join_voice_channel(channel)
        # except:
        #     #sort this out!
        #     #discord.VoiceClient.move_to(bot.get_channel(channel.id))
        # await self.bot.move_member(member, channel)
        # player = voice.create_ffmpeg_player('Ta Da.mp3')
        # player.start()
        pass

    @commands.command(pass_context=False, no_pm=True)
    async def Calc(self, *string):
        allowable_chars = ["(", ")", "+", "-", "/", "*", "//", "%", "[", "]", "{", "}"]
        string = "".join(string)

        for char in list(string):
            if char not in allowable_chars and char.isdigit() is False:
                await bot.say("Not acceptable characters used, try an equal this time please")
                return

        string = "".join(string)
        await bot.say(eval(string))

    @commands.command(pass_context=False, no_pm=True)
    async def GMaps(self, *string):
        print(string)
        if len(string) == 1:
            output = ('https://www.google.co.uk/maps/place/{}\''.format(string[0]))
        else:
            output = 'https://www.google.co.uk/maps/dir/'
            for location in list(string):
                location = location.replace(" ","+")
                location = location.replace(",", "+,")
                output += str(location)
                output += '/'
        output += ''
        await bot.say(output)


bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description='A playlist example for discord.py')
bot.add_cog(John_Bot(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run('put token here')