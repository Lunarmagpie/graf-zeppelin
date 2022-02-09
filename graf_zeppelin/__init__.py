# This file is part of Graf Zeppelin.

# Graf Zeppelin is free software: you can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.

# Graf Zeppelin is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with Graf
# Zeppelin. If not, see <https://www.gnu.org/licenses/>.

import os

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
