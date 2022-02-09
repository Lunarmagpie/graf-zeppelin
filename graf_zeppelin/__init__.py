import os
from typing import cast

import hikari
import dotenv

dotenv.load_dotenv()


bot = hikari.GatewayBot(token=os.environ["TOKEN"])


@bot.listen()
async def on_message(event: hikari.GuildMessageCreateEvent):
    messge = event.message

    if messge.author.is_bot:
        return

    if messge.content and messge.content.lower() == "i hate everything":
        await event.get_channel().send("I hate everything except Mawwwam")

bot.run()
