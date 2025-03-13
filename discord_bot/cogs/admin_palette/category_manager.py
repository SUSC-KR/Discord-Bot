import discord
from discord.ext import commands
from discord_bot.config import GUILD_ID
from discord.commands import slash_command


class CategoryManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_ID, description="Display the category list")
    @commands.has_permissions(administrator=True)
    async def display_category_list(self, ctx):
        embed = discord.Embed(title="카테고리 목록", color=discord.Color.blue())
        if ctx.guild.categories:
            for category in ctx.guild.categories:
                embed.add_field(
                    name=category.name,
                    value=f"카테고리 ID: {category.id}",
                    inline=False,
                )

            if len(embed.fields) > 25:
                embeds = [
                    discord.Embed(
                        title="카테고리 목록", color=discord.Color.blue()
                    )
                ]
                for i, field in enumerate(embed.fields):
                    if i % 25 == 0 and i != 0:
                        embeds.append(
                            discord.Embed(
                                title="카테고리 목록",
                                color=discord.Color.blue(),
                            )
                        )
                    embeds[-1].add_field(
                        name=field.name, value=field.value, inline=False
                    )
                for page in embeds:
                    await ctx.send(embed=page)
            else:
                await ctx.send(embed=embed)
        else:
            embed.description = "서버에 카테고리가 없습니다."
            await ctx.send(embed=embed)

    @slash_command(guild_ids=GUILD_ID, description="Create a category and role")
    @commands.has_permissions(administrator=True)
    async def create_category(self, ctx, name: str):
        guild = ctx.guild
        upper_name = name.upper()

        role = discord.utils.get(guild.roles, name=upper_name)
        if role:
            await ctx.send(f"'{upper_name}' 역할이 이미 존재합니다.")
            return

        try:
            role = await guild.create_role(name=upper_name)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(
                    view_channel=False
                ),
                role: discord.PermissionOverwrite(view_channel=True),
            }
            category = await guild.create_category(
                name=upper_name, overwrites=overwrites
            )
            await guild.create_text_channel("자유", category=category)
            await guild.create_voice_channel("라운지", category=category)

            await ctx.send(f"'{upper_name}' 카테고리와 역할이 생성되었습니다.")
        except discord.DiscordException as e:
            await ctx.send(f"오류가 발생했습니다: {str(e)}")

    @slash_command(guild_ids=GUILD_ID, description="Delete a category and role")
    @commands.has_permissions(administrator=True)
    async def delete_category(self, ctx, category_name: str):
        guild = ctx.guild
        category_name = category_name.upper()
        category = discord.utils.get(guild.categories, name=category_name)

        if category is None:
            await ctx.send(f"'{category_name}' 카테고리가 존재하지 않습니다.")
            return

        try:
            for channel in category.channels:
                await channel.delete()

            await category.delete()

            role = discord.utils.get(guild.roles, name=category_name.upper())
            if role:
                await role.delete()

            await ctx.send(
                f"'{category_name}' 카테고리와 포함된 모든 채널, 역할이 삭제되었습니다."
            )
        except discord.DiscordException as e:
            await ctx.send(f"오류가 발생했습니다: {str(e)}")


def setup(bot):
    bot.add_cog(CategoryManager(bot))
    print("CategoryManager Cog is loaded")
