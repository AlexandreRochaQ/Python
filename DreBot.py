import discord
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default(), application_id='1040407207503728750')
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'salutations', description='hello')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey, i'm here buddy", ephemeral = True) 

@tree.command(name = 'bonitin', description='bonito')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"lindao", ephemeral = True)

client.run('MTA0MDQwNzIwNzUwMzcyODc1MA.GgY4lj.FbdaD7Wl4_z2Chn8UwrOZ8x61MfgNkzfNozyPQ')