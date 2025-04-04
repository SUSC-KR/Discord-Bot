import discord
from discord.commands import slash_command
from discord.ext import commands


class StudyManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Create a study room with roles and channels")
    @commands.has_permissions(administrator=True)
    async def create_study(
        self,
        ctx,
        study_name: str,
        year: str,
        season: str,
        category_name: str = None,
    ):
        guild = ctx.guild
        study_name = study_name.upper()
        season = season.upper()
        year_short = year[-2:]
        category_name = category_name.upper()

        role_name = f"{year_short}-{season}-{study_name}"

        if await self.role_exists(guild, role_name):
            return await ctx.send(f"'{role_name}' 역할이 이미 존재합니다.")

        category = await self.get_or_create_category(guild, category_name, role_name)
        await self.create_study_channels(guild, category, study_name, role_name)

        await ctx.send(f"'{role_name}' 스터디 역할과 채널이 생성되었습니다.")

    @slash_command(description="Delete study room and migrate role members")
    @commands.has_permissions(administrator=True)
    async def delete_study(self, ctx, year: str, study_name: str, season: str, category_name: str):
        guild = ctx.guild
        season = season.upper()
        year_short, year_long = year[-2:], year[-4:]
        role_name = f"{year_short}-{season}-{study_name.upper()}"
        season_role_name = f"{year_long} {season}"
        category_name = category_name.upper()

        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            return await ctx.send(f"'{category_name}' 카테고리가 존재하지 않습니다.")

        await self.delete_study_channels_with_study_name(category, study_name)
        season_role = await self.get_or_create_role(guild, season_role_name)
        await self.migrate_members_from_role(guild, role_name, season_role)

        await ctx.send(
            f"'{category_name}' 카테고리와 관련된 스터디 룸과 역할이 삭제되고, 멤버가 '{season_role_name}' 역할로 이동되었습니다."
        )

    async def role_exists(self, guild, role_name):
        return discord.utils.get(guild.roles, name=role_name) is not None

    async def get_or_create_category(self, guild, category_name, role_name):
        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                await self.get_or_create_role(guild, role_name): discord.PermissionOverwrite(view_channel=True),
            }
            category = await guild.create_category(name=category_name, overwrites=overwrites)
            await self.create_default_channels(guild, category)
        return category

    async def create_default_channels(self, guild, category):
        await guild.create_text_channel("자유", category=category)
        await guild.create_voice_channel("라운지", category=category)

    async def create_study_channels(self, guild, category, study_name, role_name):
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            await self.get_or_create_role(guild, role_name): discord.PermissionOverwrite(view_channel=True),
        }
        await guild.create_text_channel(f"{study_name}-채팅", category=category, overwrites=overwrites)
        await guild.create_voice_channel(f"{study_name}-음성", category=category, overwrites=overwrites)

    async def delete_study_channels_with_study_name(self, category, study_name):
        for channel in category.channels:
            if f"{study_name.lower()}-채팅" in channel.name or f"{study_name.upper()}-음성" in channel.name:
                await channel.delete()

    async def migrate_members_from_role(self, guild, role_name, new_role):
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            for member in role.members:
                await member.add_roles(new_role)
                await member.remove_roles(role)
            await role.delete()

    async def get_or_create_role(self, guild, role_name):
        """Retrieve or create a role."""
        role = discord.utils.get(guild.roles, name=role_name)
        return role if role else await guild.create_role(name=role_name)


def setup(bot):
    bot.add_cog(StudyManager(bot))
    print("StudyManager Cog is loaded")
