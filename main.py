from libottdadmin2.client.sync import OttdSocket
from libottdadmin2.packets.admin import AdminRcon
import os
import discord
from dotenv import load_dotenv
import logging


load_dotenv()
socket = OttdSocket(os.getenv('OTTD_PASS'))
socket.connect((os.getenv('OTTD_HOST'), 3977))

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    logging.debug(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.name not in ["openttd", "test-ttd"]:
        return

    if message.content == '!pause':
        logging.debug("Pausing")
        msg = AdminRcon()
        msg.encode("pause")
        socket.send_packet(msg)
        await message.channel.send("Paused")

    if message.content == '!unpause':
        logging.debug("Pausing")
        msg = AdminRcon()
        msg.encode("unpause")
        socket.send_packet(msg)
        await message.channel.send("Unpaused")

client.run(TOKEN)

