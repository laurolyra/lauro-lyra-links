import discord

class DiscordMessager(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

  def send_message(message):
    return f"mesage link: {message.url}"

intents = discord.Intents.default()
intents.message_content = True

client = DiscordMessager(intents=intents)
client.run('token')