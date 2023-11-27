from discord import Embed,Color
import wavelink
volume=[
    '--------------------',
    '==------------------',
    '====----------------',
    '======--------------',
    '========------------',
    '==========----------',
    '============--------',
    '==============------',
    '================----',
    '==================--',
    '===================='
]
embeds={
    "not-in-voice-channel":[
        Embed(
            title='你不在語音頻道裡',
            color=Color.red(),
            description='請選擇你要播放音樂的頻道'
            )
        ]
}
def nowplay(payload: wavelink.TrackEventPayload,track:wavelink.YouTubeTrack):
    
    return [
        (
            Embed(
                title='正在播放',
                description=f'[{track.title}]({track.uri})',
            )
            .set_thumbnail(url=track.thumbnail)
        )
        (
        Embed(
            title='控制器',
            color=Color.red(),
        )
        .add_field(name='循環模式',value='`off`', inline=True)
        .add_field(name='自動推薦',value='`on`', inline=True)
        .add_field(name='音量',value=f'{volume[int(payload.player.volume/10)]}', inline=False)
    )]