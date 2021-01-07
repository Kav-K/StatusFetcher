from discord.ext import commands
from botCommands.utils.utils import *

from botCommands.utils.utils import ADMIN_CHANNEL_NAME


class Administrative(commands.Cog, name='Administrative'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member_ = None

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')
        await getChannel(ADMIN_CHANNEL_NAME,self.bot.guilds[0]).send("Personal utility features have been activated on "+self.bot.guilds[0].name)
        

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    #A simple test utility command ~ping to check if the bot is running.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")