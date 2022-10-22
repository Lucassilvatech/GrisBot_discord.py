import discord
from discord import app_commands
from discord.ext import commands
from youtube_dl import YoutubeDL
from asyncio import sleep


class Music(commands.Cog):
    """Camandos para reproduzir e manipular status do audio em reprodução"""

    def __init__(self, bot):
        self.bot = bot
        

        self.YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


    cont = 0
    @commands.command(name="musga", help="coloque um url da musica que deseja reproduzir!")
    async def play(self, ctx, arg):
        global vc
        
        
        try:
            voice_channel = ctx.author.voice.channel
            vc = await voice_channel.connect()
        except:
            await ctx.send(f"{ctx.author.mention} Ja estou na call")
            print('[ERROR]') #debug

        if vc.is_playing():
            await ctx.send(f', Já estou cantando.')

        else:
            with YoutubeDL(self.YDL_OPTIONS) as ydl:
                info = ydl.extract_info(arg, download=False)
            
            URL = info['formats'][0]['url']
            
            if not discord.opus.is_loaded():
                discord.opus.load_opus() 

            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=URL, **self.FFMPEG_OPTIONS))
               
            while vc.is_playing():
                await sleep(1)
            #if not vc.is_paused():
            
    @commands.hybrid_command(with_app_commands=True)
    async def sair(self, ctx):
        await vc.disconnect()
        embedSair = discord.Embed(color=0xfa0000, title = "Okay saindo, áte logo! ^_^ " )
        await ctx.send(embed = embedSair)


    @commands.hybrid_command(with_app_commands=True)
    async def pause(self, ctx):
        vc.pause()
        await ctx.message.add_reaction('⏯')


    @commands.hybrid_command(with_app_commands=True)
    async def resume(self, ctx):
        vc.resume()
        await ctx.message.add_reaction('⏯')

async def setup(bot):
    await bot.add_cog(Music(bot))
    