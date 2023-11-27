import discord,wavelink
from discord.ui.item import Item
class select_vc(discord.ui.View):
    def __init__(self, ytk:wavelink.YouTubeTrack,ctx):
        self.ytk=ytk
        self.ctx=ctx
        super().__init__()
    @discord.ui.select(
        select_type=discord.ComponentType.channel_select,
        channel_types=[discord.ChannelType.voice]
    )
    async def select_callback(self, select:discord.ui.Select, interaction:discord.Interaction):
        searched=self.ytk
        voiceclient: wavelink.Player = await select.values[0].connect(cls=wavelink.Player)
        voiceclient.autoplay=True
        if not voiceclient.is_playing():
            print(await voiceclient.play(searched))
        else:
            await voiceclient.queue.put_wait(searched)
        await interaction.response.edit_message(content=f"Now playing `{searched.title}`",view=None)