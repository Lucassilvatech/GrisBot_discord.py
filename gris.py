from dotenv import load_dotenv
from discord.ext import commands
import os


bot = commands.Bot(command_prefix="!", intents=5)

for file in os.listdir("commands"):
    if file.endswith(".py"):
        cog = file[:-3]
        bot.load_extension(f"commands.{cog}")


bot.load_extension("gerenciadores")


load_dotenv()
TOKEN = os.getenv("token")
bot.run(TOKEN)






