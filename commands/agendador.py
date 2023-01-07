from discord.ext import commands
from manager_db import Manager_DB

from datetime import datetime, date

gerente = Manager_DB()

class Agendador(commands.Cog):
    """Agenda uma mensagem para ser mandada a o usuario depois"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def agendar(self, ctx, *, args):
        args = args.split()
        value = (ctx.author.id, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), f'{args[5:]}')
        keys = '(usuario, dia, mes, ano, hora, minuto, lembrete)'
        gerente.insert('agendas', keys, value)
        await ctx.send(f'Vc tem um lembrete para o dia {args[0]} as {args[3]} horas')

async def setup(bot):
    await bot.add_cog(Agendador(bot))
