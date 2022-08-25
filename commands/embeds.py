import discord
from discord.ext import commands


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    @commands.command(name="gris")
    async def sobre_gris(self, ctx):
        grisEmbed = discord.Embed(title="Olá eu sou a Gris", description="Sou a bot mais fofa que existe nesse mundo!", color=0xfa0000)
        grisEmbed.set_author(name=f"{self.bot.user.name}", icon_url=f"{self.bot.user.avatar}")
        grisEmbed.set_thumbnail(url="https://64.media.tumblr.com/8d850af50ab8c2045b540cc395e67d2c/98a9bd948bcea9b0-5e/s400x600/680578381dddd199d3fb6f8fc80a4850c229c6cd.png")
        grisEmbed.add_field(name="gris", value="Sou um bot em desenvolvimento, tenham paciencia comigo! Nyamuuuuuu!!! ", inline=True)
        grisEmbed.set_image(url=f"{self.bot.user.avatar}")
        grisEmbed.set_footer(text="GitHub.com/Lucassilvatech")

        await ctx.send(embed=grisEmbed)


async def setup(bot):
    await bot.add_cog(Embeds(bot))