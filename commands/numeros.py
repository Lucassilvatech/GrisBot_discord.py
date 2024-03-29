from discord.ext import commands
from discord import app_commands

import json
import requests
import random 

class Numeros(commands.Cog):
    """Trabalha com numeros aleatorios e calculos"""

    def __init__(self, bot):
        self.bot = bot
        self.responseGris = ["Não quero", "To com preguiça", "faça vc, tem mão ñ? Hummmm!", "(* ￣︿￣)", "ಠ_ಠ","(¬_¬ )"]

      
    @commands.hybrid_command(name="dado", with_app_commands=True, help="Roda um dado, se nenhum parametro for especificado roda 1D20")
    async def randomLuck(self, ctx, arg=1, arg2=20, arg3=1):
        loop = int(arg3)
        valueDado = int(arg2)
        if loop > 10 or valueDado > 100:
            await ctx.channel.send("O segundo argumanto não pode ser maior que 100 e o ultimo argumento não pode ser maior que 10")
            return
        
        valueDadoInit = int(arg)
        for c in range(0,loop):
            resposta = random.randint(valueDadoInit, valueDado)
            await ctx.reply(f'Voce tirou: {resposta}')
    

    
    
    @commands.hybrid_command(name="calcule", with_app_commands=True)
    async def calcule(self, ctx, *,expression):
        try:
            expression = "".join(expression)
            sorte = random.randint(1, 10)
            if (sorte %2 == 0 ):
                response = eval(expression)
                await ctx.send(f"A resposta é: {response}")
            elif (sorte % 2 == 1):
                sorte2 = random.randint(0, len(self.responseGris)-1)
                await ctx.channel.send(self.responseGris[sorte2])
        except SyntaxError:
            await ctx.send("verifique se colocou os argumentos necessarios!")

    @commands.command()
    async def converter(self, ctx, moeda, valor, help='Converte a moeda que for passada para real.'):

        moedas = {'iene':'JPY',
        'dolar':'USD',
        'euro':'EUR',
        'biticoin':'BTC',
        'remimbi':'CNY'
        }
        # Tenta converter o valor passado em um numero de ponto flutuante
        try:
            valor = float(valor)
        except:
            await ctx.send('A quantidade a ser convertida tem que ser um numero!')
            return

        try:
            moeda = moeda.lower()
            # completa o link com o codigo referente a moeda
            API = f'https://economia.awesomeapi.com.br/last/{moedas[moeda]}'

        except:
            await ctx.send('[O Valor digitado é invalido! Aceito estes valores: [ Iene, Dolar, Euro, Biticoin, Remimbi]')
            return

        request = requests.get(API)
        result = json.loads(request.text)

        result = float(result[moedas[moeda] + 'BRL']['bid']) * valor

        await ctx.send(f'{result:.2f} BRL')


async def setup(bot):
    await bot.add_cog(Numeros(bot))
