import os
import sqlite3

from discord.commands import slash_command
from discord.ext import commands

from discord_bot.config import GUILD_ID

os.makedirs("./db", exist_ok=True)
CHANNEL_ID_ALLOWED = os.getenv("GEEKNEWS_ID")

conn = sqlite3.connect("./db/geeknews.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()


class NewsManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_ID, description="뉴스 링크를 저장합니다.")
    async def news_add(self, ctx, url):
        cursor.execute("INSERT INTO news (url) VALUES (?)", (url,))
        conn.commit()
        await ctx.respond(f"링크가 저장되었습니다:\n{url}")

    @slash_command(guild_ids=GUILD_ID, description="저장된 뉴스 링크 전체 목록을 확인합니다.")
    async def news_list(self, ctx):
        if ctx.channel.id != CHANNEL_ID_ALLOWED:
            await ctx.respond("이 명령어는 지정된 채널에서만 사용 가능합니다.", ephemeral=True)
            return

        cursor.execute("SELECT url FROM news ORDER BY created_at DESC")
        rows = cursor.fetchall()

        if not rows:
            await ctx.respond("아직 저장된 뉴스가 없습니다.")
            return

        message = "\n".join([f"{idx + 1}. {url}" for idx, (url,) in enumerate(rows)])

        if len(message) > 100:
            await ctx.respond("링크가 너무 많아 일부 생략됩니다.")
        else:
            await ctx.respond(f"**저장된 뉴스 목록:**\n{message}")

    @slash_command(guild_ids=GUILD_ID, description="저장된 뉴스 링크를 모두 삭제합니다.")
    @commands.has_any_role("운영진", "긱뉴스")  # 임의명 긱뉴스 역할에도 권한 할당.
    async def news_rm(self, ctx):
        cursor.execute("DELETE FROM news")
        conn.commit()
        await ctx.respond("저장된 뉴스 링크가 모두 삭제되었습니다.")


def setup(bot):
    bot.add_cog(NewsManager(bot))
    print("NewsManager Cog is loaded")
