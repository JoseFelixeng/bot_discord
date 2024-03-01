import discord 
from discord.ext import commands 
import os 
import random 


# Configurando o bot

TOKEN = '01aed5bb4da34d697e73aa8797b8ae5fd18ea9221881f9353562a7349300beb9' 
PREFIX = '*'

# Inicialização do Bot
bot = commands.Bot(command_prefix=PREFIX)

# Comandos para reproduzir a música 
@bot.command()

async def play(ctx):
    #verificar se o comando foi executado em um canal e voz
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("Voce Precisa estar em um canal de voz para usar!!!")
        return 
    
    # conecta-se ao canal de voz do autor do comando
    channel = ctx.author.voice.channel
    voice_client = await channel.connect()
    
    # Lista todos os arquivos de música na pasta
    music_folder = "./user/musica"
    music_files = [f for ind os.listdir(music_folder) if f.endswith(('.mp3'.'.wav'))]

    # Seleciona uma música aleatória 
    random_music = os.path.join(music_folder, random.choice(music_files))
    
    # Reproduz a múscia selecionada
    voice_client.play(discord.FFmpegPCMAudio(random_music), after=lambda e:print('done', e))
    
    
@bot.event()
async def on_ready():
    print(f'Bot {bot.user.name} está Online!!!')
    
# Executar o bot 
bot.run(TOKEN)
