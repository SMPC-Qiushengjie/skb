import discord
from discord.ext import commands
from discord.ext import bridge
import discord,wavelink
from discord.ext import bridge, commands
from model import embed,button
class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Game('UwU')
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        print(f"目前登入身份 --> {self.bot.user}")
def setup(bot):
    bot.add_cog(OnReady(bot))
