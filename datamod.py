# Name: Time
# Author: kayt3m
# Commands:
# .now
# Licenced under the GNU AGPLv3
#                           https://www.gnu.org/licence/apgl-3.0.html
#meta developer: @def_n0

from datetime import datetime
from .. import loader, utils

class Time(loader.Module):

    strings = {"name": "Today"}

    @loader.command()
    async def now(self, message):
        """- показать сегодняшнюю дату"""
        current_datetime = datetime.now()


        await utils.answer(
                message,
                ("<b><emoji document_id=5370711279134582149>🗓</emoji><u>Today</u>\n"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji><u>year</u>: {current_datetime.year}\n</b>"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji><u>month</u>: {current_datetime.month}\n</b>"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji><u>day</u>: {current_datetime.day}\n</b>"
                 f"<b><emoji document_id=5258258882022612173>⏲</emoji><u>Real time</u>: {current_datetime.hour}</b>:"
                 f"{current_datetime.minute}:"
                 f"{current_datetime.second}(UTC+3)</b>"

                 ),
            )
