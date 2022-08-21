import discord
from discord.ext import commands


class Image(commands.Cog):
    """Comandos com imagens"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="avatar", help="Exibe o avatar de usuario marcado.")
    async def avatar(self, ctx, member: self.discord.Member = None):
        if member != None:
            await ctx.send(member.avatar_url)
        else:
            await ctx.send(ctx.author.avatar_url)


async def setup(bot):
    await bot.add_cog(Image(bot))