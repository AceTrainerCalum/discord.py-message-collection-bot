from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      file = open("Events/msg_logs.txt", 'w')
      file.write(F"{message.author} sent: {message.contents} \n")
      file.close()
      

def setup(bot):
    bot.add_cog(Events(bot))