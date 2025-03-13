import discord
import sqlite3
import datetime
from discord import option
from discord.ext import commands, tasks
from discord_bot.config import GUILD_ID
from discord.commands import slash_command

conn = sqlite3.connect("./db/ambassacor.db")
cursor = conn.cursor()


class AmbassadorManager(commands.Cog):
    """
    Ambassador 관리 명령어 모음
    """

    def __init__(self, bot):
        self.bot = bot
        self.reset_monthly_ad_count.start()

    @slash_command(guild_ids=GUILD_ID, description="홍보 인증을 제출합니다.")
    @commands.has_any_role("엠베서더", "운영진")
    @option(
        "attachment",
        discord.Attachment,
        description="메세지에 홍보 인증 이미지를 첨부하여 제출합니다.",
        required=True,
    )
    async def proof_promo(
        self,
        interaction,
        attachment: discord.Attachment,
        attachment1: discord.Attachment = None,
        attachment2: discord.Attachment = None,
    ):
        """
        홍보 인증을 제출하는 명령어입니다.
        """
        user = interaction.user

        cursor.execute(
            """
            INSERT INTO ambassador (id, name, monthly_ad_count, total_ad_count, joined_at, updated_at)
            VALUES (?, ?, 1, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            ON CONFLICT(id) DO UPDATE
            SET
                monthly_ad_count = monthly_ad_count + 1,
                total_ad_count = total_ad_count + 1,
                updated_at = CURRENT_TIMESTAMP
            """,
            (user.id, user.name),
        )
        conn.commit()

        await interaction.response.send_message(
            f"{interaction.user.mention}님이 홍보 인증을 제출했습니다:\n"
            f"{attachment.url} "
            f"{attachment1.url if attachment1 else ''} "
            f"{attachment2.url if attachment2 else ''}"
        )

    @slash_command(
        guild_ids=GUILD_ID, description="이번 달 앰베서더 랭킹을 확인합니다."
    )
    @commands.has_any_role("엠베서더", "운영진")
    async def monthly_ranking(self, interaction):
        """
        현재 월의 홍보 랭킹을 출력하는 명령어
        """
        cursor.execute(
            """
            SELECT name, monthly_ad_count FROM ambassador
            ORDER BY monthly_ad_count DESC
            LIMIT 10
        """
        )
        rankings = cursor.fetchall()

        if rankings:
            ranking_message = "**🏆 이번 달 엠베서더 랭킹 TOP 10 🏆**\n\n"
            previous_count = None
            current_rank = 0
            display_rank = 0

            for name, count in rankings:
                if count != previous_count:
                    display_rank = current_rank + 1
                ranking_message += f"**{display_rank}위** - {name}: {count}회\n"
                previous_count = count
                current_rank += 1
        else:
            ranking_message = "아직 엠베서더 활동이 없습니다."

        await interaction.response.send_message(ranking_message)

    @tasks.loop(hours=24)
    async def reset_monthly_ad_count(self):
        """
        매월 1일에 monthly_ad_count를 초기화하면서 공동 등수를 반영한 랭킹을 전송
        """
        now = datetime.datetime.now()
        if now.day == 1:
            cursor.execute(
                """
                SELECT name, monthly_ad_count FROM ambassador
                ORDER BY monthly_ad_count DESC
                LIMIT 10
            """
            )
            rankings = cursor.fetchall()

            if rankings:
                ranking_message = "**🏆 이번 달 엠베서더 랭킹 TOP 10 🏆**\n\n"

                previous_count = None
                current_rank = 0
                display_rank = 0

                for name, count in rankings:
                    if count != previous_count:
                        display_rank = current_rank + 1
                    ranking_message += (
                        f"**{display_rank}위** - {name}: {count}회\n"
                    )
                    previous_count = count
                    current_rank += 1

            channel_id = 1349236438251868180
            channel = self.bot.get_channel(channel_id)

            if channel:
                await channel.send(ranking_message)

            cursor.execute("UPDATE ambassador SET monthly_ad_count = 0")
            conn.commit()

    @reset_monthly_ad_count.before_loop
    async def before_reset(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(AmbassadorManager(bot))
    print("AmbassadorManager Cog is loaded")
