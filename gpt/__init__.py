from .gpt import gpt


def setup(bot):
    bot.add_cog(gpt(bot))