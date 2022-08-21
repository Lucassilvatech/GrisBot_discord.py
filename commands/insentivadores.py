from discord.ext import commands
import requests
import json

class Insentivadores(commands.Cog):
    """Comandos de insentivo"""
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="insentive", help="Envia uma frase inspiradora hahaha")
    async def motivation(self, ctx):
        var = requests.get("https://zenquotes.io/api/random")
        frase = json.loads(var.text)
        await ctx.send(frase[0]["q"])

async def setup(bot):
    await bot.add_cog(Insentivadores(bot))