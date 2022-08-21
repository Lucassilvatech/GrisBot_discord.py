from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
import asyncio
import os


bot = commands.Bot(command_prefix="!", intents=Intents.all())


async def load_cogs(bot):
    await asyncio.sleep(5)
    asyncio.run(bot.load_extension("gerenciadores")) 

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            asyncio.run(bot.load_extension(f"commands.{cog}"))
            

asyncio.run(load_cogs(bot)) 


load_dotenv()
TOKEN = os.getenv("token")
bot.run(TOKEN)






