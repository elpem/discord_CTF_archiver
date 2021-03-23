# bot.py
import os
import random
from datetime import date
from dotenv import load_dotenv

#import discord
from discord.ext import commands
from discord import TextChannel, Client
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
ARCHIVE_CATEGORY_NAME = os.getenv("ARCHIVE_CATEGORY_NAME")

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    global guild 
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected!\n'
        f'{bot.get_all_channels()}\n'
        f'{guild.name}\n'
        f'{guild.categories}\n'
    )
    
@bot.command(name="archive")
async def archive(ctx, *, category_name=""):
    print(category_name)
    if category_name=="":
        await ctx.send("use syntax: ~archive <category_label>")
    else:

        category = [c for c in guild.categories if c.name.lower()==category_name.lower()] # gives possible category list
        if len(category) == 0:
            await ctx.send(f"Impossible to find category with name: {category_name}")
        elif len(category) >= 2:
            await ctx.send(f"Error, too many category choices. Rename one of those categories and try again : {[c.name for c in category]}")
        
        else:
            category = category[0]
            await transfer_category_content(category, discord.utils.get(guild.categories, name=ARCHIVE_CATEGORY_NAME))
            await del_voice_channel(category)
            await category.delete(reason="archived")
            await ctx.send(f"{category_name} successfully archived!")


async def transfer_category_content(src, dst):
    #src the souce category and dst the destination category
    prefix = str(date.today().year) + "_" + src.name + "_"

    for tc in src.text_channels:
        await tc.edit(name=prefix+tc.name, category=dst)


async def del_voice_channel(category):
    for vc in category.voice_channels:
        await vc.delete()


bot.run(TOKEN)
