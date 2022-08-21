from discord.ext import commands


class Conversas(commands.Cog):
    """Conversas com o usuario"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi")
    async def sends_hello(self, ctx):
        nome = ctx.author.name
        resposta = f'Olá, {nome}'
        await ctx.reply(resposta)

    @commands.command(name="nyamuuu")
    async def Nyamuuu(self, ctx):
        if ctx.author.id == 387727666197037066: 
            resposta = "Oiiii Ouliçuuuu, nyamuuu nyamuuu"
        elif ctx.author.id == 607772975554625554: 
            resposta = "Oiiii Lontlinhaaa, nyamuuu nyamuuu"
        elif ctx.author.id == 591043145110650880: 
            resposta = "Oiiii Lamissterrr, nyamuuu nyamuuu"
        elif ctx.author.id == 608432952434491392: 
            resposta = "Oiiii Dlagãozinhoo, nyamuuu nyamuuu"
        elif ctx.author.id == 624275294936629283: 
            resposta = "Oiiii Gatlinhuuum, nyamuuu nyamuuu"
        elif ctx.author.id == 479781826161016833: 
            resposta = "Oiiii Papython, nyamuuu nyamuuu"
        else:
            resposta ="Humm, ñ quero falar com vc!"
        await ctx.channel.send(resposta)


async def setup(bot):
    await bot.add_cog(Conversas(bot))
