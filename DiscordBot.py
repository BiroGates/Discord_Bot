import random
import os
import discord
from discord.ext import commands
import uuid
import filmes_bot
from matchup import matchup

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def comandos(ctx):
    await ctx.send('!ping, !zerotwo, !filme, !contra')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms :stop_button:')


@client.command()
async def zerotwo(ctx):
    folder = 'imagens/'
    count = 1
    for file_name in os.listdir(folder):
        source = folder + file_name

        destination = folder + str(count) + ".gif"

        os.rename(source, destination)
        count += 1

    l = len(os.listdir('imagens/'))
    r = random.randint(1, l)

    await ctx.send(file=discord.File(f'imagens/{r}.gif'))


@client.command()
async def filme(ctx):
    filds = ['Titulo', 'Data De Lançamento']
    lista = filmes_bot.scraping()
    list_size = len(lista)

    embed = discord.Embed(
        title='Lançamentos de filmes :projector:',
        description='Lançamentos da semana de acordo com o site AdoroCinema.com',
        colour=discord.Colour.blue()
    )

    for c in range(list_size):
        for i in range(0, 1 + 1):
            embed.add_field(name=f'{filds[i]}', value=f'{lista[c][i]}', inline=False)
            embed.add_field(name=chr(173), value=chr(173), inline=False)

    await ctx.send(embed=embed)


@client.command()
async def contra(ctx, jogando_c, contra_c, lane_c):
    # Deixando uppercase
    jogando_c = jogando_c.title()
    contra_c = contra_c.title()

    # Variaveis que preciso
    result = matchup(jogando_c, contra_c, lane_c)

    # Fazendo o embed
    embed = discord.Embed(
        title=f'Matchup de {jogando_c} contra {contra_c}',
        description=f'',
        colour=discord.Colour.blue()
    )

    # Mostrando as estasticas
    embed.add_field(name=chr(173), value=chr(173), inline=True)
    embed.add_field(name=f'{jogando_c} Counter Kills', value=f'{result[0]}', inline=True)
    embed.add_field(name=f'{contra_c} Counter Kills', value=f'{result[1]}', inline=True)

    embed.add_field(name=chr(173), value=chr(173), inline=True)
    embed.add_field(name=f'{jogando_c} Kills', value=f'{result[2]}', inline=True)
    embed.add_field(name=f'{contra_c} Kills', value=f'{result[3]}', inline=True)

    embed.add_field(name=chr(173), value=chr(173), inline=True)
    embed.add_field(name=f'{jogando_c} Early Lead Ratio', value=f'{result[4]}', inline=True)
    embed.add_field(name=f'{contra_c} Early Lead Ratio', value=f'{result[5]}', inline=True)

    embed.add_field(name=chr(173), value=chr(173), inline=True)
    embed.add_field(name=f'{jogando_c} Comeback Ratio', value=f'{result[6]}', inline=True)
    embed.add_field(name=f'{contra_c} Comaback Ratio', value=f'{result[7]}', inline=True)

    embed.add_field(name=chr(173), value=chr(173), inline=True)
    embed.add_field(name=f'{jogando_c} Win Percent', value=f'{result[8]}', inline=True)
    embed.add_field(name=f'{contra_c} Win Percent', value=f'{result[9]}', inline=True)

    await ctx.send(embed=embed)
client.run('TOKEN DO BOT')
