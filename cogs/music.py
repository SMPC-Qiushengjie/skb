import discord,wavelink
from discord.ext import bridge, commands
from model import embed,button
class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ctx=None
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        await self.bot.wait_until_ready()

        node = wavelink.Node(uri = '127.0.0.1:2333', password='youshallnotpass')
        await wavelink.NodePool.connect(client = self.bot, nodes = [node])
    @commands.Cog.listener()
    async def on_wavelink_track_start(self,payload: wavelink.TrackEventPayload):
        track=wavelink.YouTubeTrack.search(payload.track.uri)
        track=track[0]
        await self.ctx.edit_original_response(content=None,embeds=embed.nowplay(payload=payload,track=track))
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEventPayload):
        ...
    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f"Node: <{node.uri}> is ready!")

    @bridge.bridge_command()
    async def play(self, ctx:discord.ApplicationContext, search: str):
        """播放youtube的音樂
        
        可以使用url或是關鍵字
        """
        '''Play music'''
        
        searched = await wavelink.YouTubeTrack.search(search)
        searched=searched[0]
        if not getattr(ctx.user.voice, "channel", None):
            return await ctx.respond(embeds=embed.embeds['not-in-voice-channel'],view=button.select_vc(searched, ctx))
        elif not ctx.guild.voice_client:
            voiceclient: wavelink.Player = await ctx.user.voice.channel.connect(cls=wavelink.Player)
        else:
            voiceclient: wavelink.Player = ctx.guild.voice_client
        
        if not voiceclient.is_playing():
            self.ctx=await ctx.respond(f"正在播放: `{searched.title}`")
            print(await voiceclient.play(searched))
            
        else:
            await voiceclient.queue.put_wait(searched)
            await ctx.respond(f"添加: `{searched.title}`",ephemeral=True)
def setup(bot):
    bot.add_cog(Music(bot))