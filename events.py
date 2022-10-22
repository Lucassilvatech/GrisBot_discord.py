import discord
from discord.ext import commands


class Events(commands.Cog):
    """gerencia eventos"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = self.bot.get_channel(991470178019856447)
        await canal.send(f"{member.mention} Seja bem vindo!")


async def setup(bot):
    await bot.add_cog(Events(bot))