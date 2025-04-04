import discord
from discord.commands import slash_command
from discord.ext import commands

from discord_bot.config import GUILD_ID


class RoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="add a role to a user", guild_id=GUILD_ID)
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        """
        유저에게 역할을 추가합니다.
        """
        if role in member.roles:
            await ctx.respond(f"{member.name}님은 이미 {role.name} 역할을 가지고 있습니다.")
        else:
            await member.add_roles(role)
            await ctx.respond(f"{member.name}님에게 {role.name} 역할을 추가했습니다.")

    @slash_command(description="remove a role from a user", guild_id=GUILD_ID)
    @commands.has_permissions(administrator=True)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        """
        유저로부터 역할을 제거합니다.
        """
        if role not in member.roles:
            await ctx.respond(f"{member.name}님은 {role.name} 역할을 가지고 있지 않습니다.")
        else:
            await member.remove_roles(role)
            await ctx.respond(f"{member.name}님으로부터 {role.name} 역할을 제거했습니다.")


def setup(bot):
    bot.add_cog(RoleManager(bot))
    print("RoleManager Cog is loaded")
