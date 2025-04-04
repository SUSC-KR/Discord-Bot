import discord
from discord.commands import slash_command
from discord.ext import commands

from discord_bot.config import GUILD_ID


class BasicTest(commands.Cog):
    """
    기본적인 서버 테스트 명령어 모음
    """

    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_ID, description="Ping the server to check latency")
    async def ping(self, interaction):
        """
        서버의 응답 시간을 확인합니다.
        """
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! {latency}ms")

    @slash_command(guild_ids=GUILD_ID, description="Get server information")
    async def serverinfo(self, interaction):
        """
        서버 정보를 확인합니다.
        """
        guild = interaction.guild
        embed = discord.Embed(title="서버 정보", color=discord.Color.blue())
        embed.add_field(name="서버 이름", value=guild.name, inline=False)
        embed.add_field(name="멤버 수", value=guild.member_count, inline=False)
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(BasicTest(bot))
    print("BasicTest Cog is loaded")
