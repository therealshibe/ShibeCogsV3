from num2words import num2words
from discord.ext import commands
from word2number import w2n
from redbot.core import Config
from redbot.core.utils import chat_formatting

class spellnum:
    """Converts Words to Numbers and Numbers to words"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def spellnum(self, ctx, num):
        """Command for converting a number to words"""
        i = int(num)
        wordnum = num2words(i)
        await ctx.send(wordnum)

    @commands.command(pass_context=True)
    async def wordnum(self, ctx, word):
        """Command for converting words to numbers"""
        wordnum = w2n.word_to_num(word)
        await ctx.send(wordnum)
