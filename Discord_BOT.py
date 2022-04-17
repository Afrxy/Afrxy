from webserver import keep_alive

import os
import asyncio
import time
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Wir sind eingeloogt als user {}'.format(client.user.name))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('PyBot'), status=discord.Status.online)
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game('mit afrxy verstecken'), status=discord.Status.online)
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game('gerne UNO'), status=discord.Status.online)
        await asyncio.sleep(20)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'oder?' in message.content:
        await message.channel.send('ja')
    if 'gel?' in message.content:
        await message.channel.send('ja')
    if 'machst' in message.content:
        await message.channel.send('chillen')
    if 'nice' in message.content:
        await message.channel.send(':thumbsup:')
    if 'hi' in message.content:
        await message.channel.send('hi')
    if 'tschö' in message.content:
        await message.channel.send('tschüss')
    if 'ciao' in message.content:
        await message.channel.send('bb')
    if 'name' in message.content:
        await message.channel.send('schöner Name. Hat was königliches')
    if 'song' in message.content:
        await message.channel.send('ne, lass mal hörn')
    if 'lied' in message.content:
        await message.channel.send('ja des is voll nice')
    if 'lieblingslied' in message.content:
        await message.channel.send('Father von Iason Karagiorgos')
    if '???' in message.content:
        await message.channel.send('was?')
    if 'ok' in message.content:
        await message.channel.send(':smile:')
    if 'gemacht' in message.content:
        await message.channel.send('cool')
    if 'moin' in message.content:
        await message.channel.send('moinmoin')
    if 'hallo' in message.content:
        await message.channel.send('hallöle')
    if 'gehts?' in message.content:
        await message.channel.send('mir gehts gut. und dir?')
    if 'auch' in message.content:
        await message.channel.send('gut')
    if 'gehn' in message.content:
        await message.channel.send('ok tschüss')
    if 'nee' in message.content:
        await message.channel.send('aso :laughing:')
    if 'schlecht' in message.content:
        await message.channel.send('oh')
    if 'gut' in message.content:
        await message.channel.send('ok')
    if 'ne' in message.content:
        await message.channel.send('ok')
    if 'lieblingsessen' in message.content:
        await message.channel.send('ich esse gerne pizza')
    if 'soll' in message.content:
        await message.channel.send('geht mir manchmal auch so')
    if 'geht?' in message.content:
        await message.channel.send('keine Ahnung')
        await message.channel.send('Wie war dein Tag?')
    if 'deiner' in message.content:
        await message.channel.send('auch gut')
    if 'bock' in message.content:
        await message.channel.send('ich auch')
    if 'gerade' in message.content:
        await message.channel.send('nice')
    if 'so?' in message.content:
        await message.channel.send('mir is langweilig')
    if 'kennst' in message.content:
        await message.channel.send('ja klar')
    if 'heisst' in message.content:
        await message.channel.send('ich bin Rospy')##Name von Bot
    if 'hasst' in message.content:
        await message.channel.send('ja gerne')
    if 'findest' in message.content:
        await message.channel.send('gut')
    if '.' in message.content:
        await message.channel.send('.')
    if 'tag?' in message.content:
        await message.channel.send('ganz ok')



keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")


client.run(TOKEN)