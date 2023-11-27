import os,discord,logging,logger
from dotenv import load_dotenv
from discord.ext import bridge
from pathlib import Path
logger.write_logger()
intents = discord.Intents().all()
load_dotenv()
bot = bridge.Bot(command_prefix="!", intents=intents)
def get_model(folder):
    return [p.stem for p in Path(".").glob(f"./{folder}/*.py")]
#load commands
for cog in get_model('cogs'):
    bot.load_extension(f'cogs.{cog}')
#load listener
for cog in get_model('listener'):
    bot.load_extension(f'listener.{cog}')
bot.run(os.getenv("DISCORD_TOKEN"))