import discord
from discord.ext import commands, tasks
from youtube_dl import YoutubeDL
from asyncio import sleep


class Music(commands.Cog):
    """Camandos para reproduzir e manipular status do audio em reprodução"""

    def __init__(self, bot):
        self.bot = bot
        self.my_list = []
        self.valid = False
        self.URL = None
        self.ctx = None

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
            print('[ERROR]') #debug
        
        if vc.is_playing():
            await ctx.send(f'{ctx.author.mention}, Já estou na call.')

        else:
            with YoutubeDL(self.YDL_OPTIONS) as ydl:
                info = ydl.extract_info(arg, download=False)
            
            self.URL = info['formats'][0]['url']

            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source = self.URL, **self.FFMPEG_OPTIONS))
            discord.opus.load_opus('opus')      
            while vc.is_playing():
                await sleep(1)
            #if not vc.is_paused():


    @commands.command(name='stop')
    async def stop_loop(self, ctx):
        self._loop.stop()
        self._loop.cancel()
        self._list.start()
        await ctx.message.add_reaction('↪️')


    @commands.command()
    async def loop(self, ctx):
        self._list.stop()
        self._list.cancel()
        self._loop.start()
        await ctx.message.add_reaction('🔂')


    @tasks.loop(seconds=1.0)
    async def _loop(self):
        if not vc.is_playing() and not vc.is_paused():

            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source = self.URL, **self.FFMPEG_OPTIONS))
            discord.opus.load_opus('opus')


    @commands.command(name='list')
    async def listar(self, ctx, args):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(args, download=False)
        
        MY_URL = info['formats'][0]['url']
        self.my_list.append(MY_URL)
        if not self.valid:
            self.valid = True
            self._list.start()


    @tasks.loop(seconds=1.0)
    async def _list(self):
        if not vc.is_playing():
            if len(self.my_list) == 0:
                await self.ctx.send('A lista está vazia!')
                vc.resume()
                return
            
            self.URL = self.my_list.pop(0)
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source = self.URL, **self.FFMPEG_OPTIONS))
            discord.opus.load_opus('opus')      
            while vc.is_playing():
                await sleep(1)

            
    @commands.command()
    async def prox(self, ctx):
        self.ctx = ctx
        vc.pause()
        self._list.start()

            
    @commands.command()
    async def sair(self, ctx):
        await vc.disconnect()


    @commands.command()
    async def pause(self, ctx):
        vc.pause()
        await ctx.message.add_reaction('⏯')


    @commands.command()
    async def resume(self, ctx):
        vc.resume()
        await ctx.message.add_reaction('⏯')

async def setup(bot):
    await bot.add_cog(Music(bot))
    