import discord
from discord.ext import commands
import os

class Files(commands.Cog):
    """Cria e manipula arquivos"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="write", help="Cria um arquivo .txt com os dados inseridos na mensagem")
    async def create_file(self, ctx, *, text):
        with open(ctx.author.name + ".txt","a") as file:
            text = text + "\n"
            file.write(text)
        
 

    @commands.command(name="send_me", help="Envia o arquivo criado com o comando '!write'")
    async def arquivo(self, ctx):
        await ctx.send(file=discord.File(ctx.author.name + ".txt"))
        os.remove(ctx.author.name + ".txt")

async def setup(bot):
    await bot.add_cog(Files(bot))