from discord.ext import commands
import wikipedia


class Pesquisa(commands.Cog):
    """Pesquisas da web"""

    def __init__(self, bot):
        self.bot = bot
        self.lang = "pt"

    @commands.command(name="wiki")
    async def pesquisaWiki(self, ctx, *, content):
        try:
            wikipedia.set_lang(self.lang)
            res = wikipedia.summary(content, sentences=4)
            await ctx.send(res)
        except:
            await ctx.send("Sinto muito, não encontrei sua pesquisa 😔.")

    
    @commands.command(name="lang")
    async def langue(self, ctx):
        if self.lang == "pt":
            self.lang = "en"
            await ctx.channel.send("As pesquisa de wiki agora são feitas em ingles!")
        elif self.lang == "en":
            self.lang = "pt"
            await ctx.channel.send("As pesquisas da wiki agora são feitas em portugues!")


async def setup(bot):
    await bot.add_cog(Pesquisa(bot))
