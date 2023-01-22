from discord.ext import tasks, commands
from datetime import datetime, date

from manager_db import Manager_DB


gerente = Manager_DB()


class Verificar(commands.Cog):
    """Faz validaçoes"""

    def __init__(self, bot):
        self.bot = bot
 
    @commands.Cog.listener()
    async def on_ready(self):
        self.loop_alert.start()

 
    @tasks.loop(seconds=30)
    async def loop_alert(self):
        canal = self.bot.get_channel(991470178019856447)

        current_date = datetime.today()

        day = current_date.day
        month = current_date.month
        year = current_date.year

        hour = current_date.hour
        minute = current_date.minute


        dados = gerente.select('agendas')
        for value in dados:

            if value['mes'] == month and value['dia'] == day:

                if value['hora'] == hour:

                    gerente.delete_record('agendas', value['id'])
                    result = value['lembrete']

                    result = result.replace("[", "")
                    result = result.replace("]", "")
                    result = result.replace("'", "")
                    result = result.replace(",", "")
                    
                    await canal.send('Lembrete: '+ result)

async def setup(bot):
    await bot.add_cog(Verificar(bot))

