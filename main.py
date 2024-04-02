import discord
import random
import string
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN') # get the the token from the .env file

intents = discord.Intents.all() # set the intents
intents.members = True
intents.message_content = True 

client = commands.Bot(command_prefix='-', intents=intents) # set the bots prefix for commands, doesn't matter as this is only a slash cmd.

@client.event
async def on_ready():
    await client.tree.sync()
    print('Logged in as {0.user} (ID: {0.user.id})'.format(client)) # display when the bot is ready

def generate_random_id(length=6): # generate a unique id for the infraction (useful for database expanations)
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
random_id = generate_random_id()

@client.tree.command(description="Infract a staff member.") # the actual infraction command
async def infract(interaction: discord.Interaction, member: discord.Member, reason: str, action: str):
    random_id = generate_random_id()
    channel = client.get_channel(1206499238226305084)
    embed=discord.Embed(title="Staff Infraction Log", color=0x2b2d31)
    embed.add_field(name="Action:", value=action, inline=False)
    embed.add_field(name="Staff Member:", value=f"@{member.name} (`{member.id}`)", inline=False)
    embed.add_field(name="Reason:", value=reason, inline=False)
    embed.add_field(name="Issued By:", value=f"@{interaction.user.name} (`{interaction.user.id}`)", inline=False)
    embed.add_field(name="Date:", value=discord.utils.format_dt(discord.utils.utcnow(), style='f'), inline=True)
    embed.add_field(name="ID:", value=random_id, inline=True)
    embed.timestamp = discord.utils.utcnow()
    await channel.send(f"<@{member.id}>",embed=embed)
    await interaction.response.send_message("Infraction issued!", ephemeral=True)
    await member.send(embed=embed)

if __name__ == '__main__':
    client.run(TOKEN) # run the discord bot