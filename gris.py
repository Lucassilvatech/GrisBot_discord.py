from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
import os


bot = commands.Bot(command_prefix="!", intents=Intents.all())


def load_cogs(bot):
    bot.load_extension("gerenciadores")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")
            

load_cogs(bot)


load_dotenv()
TOKEN = os.getenv("token")
bot.run(TOKEN)






