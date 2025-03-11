import discord
from discord.ext import commands
from discord.commands import slash_command

class StudyManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Create a study room with roles and channels")
    @commands.has_permissions(administrator=True)
    async def create_study(self, ctx, study_name: str, year: str, season: str, category_name: str = None):
        guild = ctx.guild
        study_name = study_name.upper()
        season = season.upper()
        category_name = category_name.upper()
        year_short = year[-2:]

        role_name = f"{year_short}-{season}-{study_name}"
        role = discord.utils.get(guild.roles, name=role_name)

        # 역할이 이미 있는 경우, 이미 존재하는 메시지를 반환
        if role:
            await ctx.send(f"'{role_name}' 역할이 이미 존재합니다.")
            return

        category = discord.utils.get(
            guild.categories, name=category_name) if category_name else None

        role = await guild.create_role(name=role_name)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            role: discord.PermissionOverwrite(view_channel=True),
        }

        if category:
            await guild.create_text_channel(f"{study_name}-채팅", category=category, overwrites=overwrites)
            await guild.create_voice_channel(f"{study_name}-음성", category=category, overwrites=overwrites)
        else:
            study_category = await guild.create_category(name=category_name, overwrites=overwrites)
            role = await guild.create_role(name=category_name)
            await guild.create_text_channel("자유", category=category)
            await guild.create_voice_channel("라운지", category=category)
            await guild.create_text_channel(f"{study_name}-채팅", category=study_category)
            await guild.create_voice_channel(f"{study_name}-음성", category=study_category)

        await ctx.send(f"'{role_name}' 스터디 역할과 채널이 생성되었습니다.")

    @slash_command(description="Delete study room and migrate role members")
    @commands.has_permissions(administrator=True)
    async def delete_study(self, ctx, year: str, study_name: str, season: str):
        guild = ctx.guild
        season = season.upper()
        year_short = year[-2:]
        year_long = year[-4:]

        role_name = f"{year_short}-{season}-{study_name}"
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            await ctx.send(f"'{role_name}' 역할이 존재하지 않습니다.")
            return

        category = discord.utils.get(guild.categories, name=role_name)
        if category:
            for channel in category.channels:
                if channel.name in [f"{study_name}-채팅", f"{study_name}-음성"]:
                    await channel.delete()

        season_role_name = f"{year_long}_{season}"
        season_role = discord.utils.get(guild.roles, name=season_role_name)
        if not season_role:
            season_role = await guild.create_role(name=season_role_name)

        for member in role.members:
            await member.add_roles(season_role)
            await member.remove_roles(role)

        await role.delete()
        await ctx.send(f"'{role_name}' 스터디 룸과 역할이 삭제되고, 멤버가 '{season_role_name}' 역할로 이동되었습니다.")


def setup(bot):
    bot.add_cog(StudyManager(bot))
    print("StudyManager Cog is loaded")
