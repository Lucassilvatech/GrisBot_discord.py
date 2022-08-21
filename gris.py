from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
import asyncio
import os


bot = commands.Bot(command_prefix="!", intents=Intents.all())


async def load_cogs():
    await bot.load_extension("gerenciadores")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")


load_dotenv()
TOKEN = os.getenv("token")


async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


asyncio.run(main())







