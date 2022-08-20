import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Gerenciadores(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Estou pronta!')
        canal = self.bot.get_channel(991477136592478258)
        await canal.send("A mãe tá on")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("Visual Studio Code com Papython"))
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Esse comando não existe! Use `!help` para saber os comandos existentes.")
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Você não passou todos os argumentos necessarios, verifique e tente novamente!")
        else:
            raise error


def setup(bot):
    bot.add_cog(Gerenciadores(bot))