import discord
import sys
import os
from discord_bot.config import EXTENSIONS
from discord_bot.bot import run_bot


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "discord_bot"))
)

intents = discord.Intents.all()

bot = discord.Bot(intents=intents)

if __name__ == "__main__":
    if not EXTENSIONS:
        print("No extensions to load.")

    for extension in EXTENSIONS:
        try:
            bot.load_extension(extension)
            print(f"Successfully loaded extension: {extension}")

        except Exception as e:
            print(f"Failed to load extension {extension}: {e}", file=sys.stderr)

    run_bot(bot)
