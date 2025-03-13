import discord
from discord.ext import commands
from discord.commands import slash_command
import random
import csv
import os
import re


class TechInterview(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="회사의 테크 인터뷰 질문을 랜덤으로 가져옵니다.")
    async def give_question(self, ctx):
        """
        Tech-Interview-Questions 폴더에서 랜덤으로 인터뷰 질문을 가져옵니다.
        """

        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../")
        )
        questions_dir = os.path.join(project_root, "Tech-Interview-Questions")

        company_folders = self.get_company_folders(questions_dir)

        if not company_folders:
            await ctx.send(
                "Tech-Interview-Questions 폴더에 유효한 회사 폴더가 없습니다."
            )
            return

        company_name = random.choice(company_folders)
        questions_file_path = os.path.join(
            questions_dir, company_name, "questions.csv"
        ).strip()

        if not os.path.exists(questions_file_path):
            await ctx.send(f"{company_name}에 대한 질문이 없습니다.")
            return

        questions = self.load_questions_from_csv(questions_file_path)

        if not questions:
            await ctx.send(f"{company_name}에 사용할 질문이 없습니다.")
            return

        question = random.choice(questions)

        embed = self.create_question_embed(company_name, question)

        await ctx.respond(embed=embed)

    def get_company_folders(self, questions_dir):
        return [
            f
            for f in os.listdir(questions_dir)
            if os.path.isdir(os.path.join(questions_dir, f))
            and re.match(r"^[^\\]+$", f)
            and not f.startswith(".")
        ]

    def load_questions_from_csv(self, file_path):
        try:
            with open(file_path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                questions = [row["question"] for row in reader]
            return questions
        except Exception as e:
            print(f"Error reading CSV file {file_path}: {e}")
        return []

    def create_question_embed(self, company_name, question):
        embed = discord.Embed(
            title=f"{company_name}의 인터뷰 질문 중에 하나입니다.",
            color=discord.Color.blue(),
        )

        embed.add_field(name="질문", value=question, inline=False)

        embed.add_field(
            name="기여하기",
            value="문제에 이상이 있거나 문제를 추가하고 싶으시다면, [여기](https://github.com/SUSC-KR/Tech-Interview-Questions) 를 통해 기여해주세요.",
            inline=True,
        )

        return embed


def setup(bot):
    bot.add_cog(TechInterview(bot))
    print("TechInterview Cog is loaded")
