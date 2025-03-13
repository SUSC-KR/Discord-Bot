from discord_bot.config import TOKEN


def run_bot(bot):
    if TOKEN is None:
        raise ValueError(
            "Discord Token is not set. Please set Token in config.py"
        )
    bot.run(TOKEN)
