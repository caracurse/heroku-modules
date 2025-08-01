#Name: speedtester
#Description: Module for checking your Internet speed.
#Author: @sansaramods
# Commands:
# .speed
# ---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/exodiast
#-----------------------------------------------------------------------------------
# meta developer: @sansaramods
#-----------------------------------------------------------------------------------

__version__ = (1, 1, 2)

from typing import Tuple
import speedtest
import logging 
from heroku import loader, utils #type: ignore
from telethon.tl.custom import Message #type: ignore


logger = logging.getLogger(__name__)

@loader.tds
class Speedtest(loader.Module):
    """Module for checking your speedtest."""
    strings = {
        "name": "speedtester",
       
        "speedtest": "Testing.. ",
        "speed": (
            "<b> Download: <code>{dowload}</code> Mbit/s</b>\n"
            "<b>Upload: <code>{upload}</code> Mbit/s</b>\n"
            "<b>Server ping: <code>{ping}</code> ms</b>"
        ),
    }

    strings_ru = {
        "_cls_doc": "Высчитывает скорость вашего Интернет-соединения",
        "_cmd_doc_speedtest": "Проверка скорости.. ",
        "speed": (
            "<b> Загружено: <code>{dowload}</code> Мбит/с</b>\n"
            "<b>Выгружено: <code>{upload}</code> Мбит/с</b>\n"
            "<b>Пинг сервера: <code>{ping}</code> мс</b>"
        )
    }

    strings_de = {
        "<b> Geladen: <code>{dowload}</code> Mbit/s</b>\n"
            "<b>Hochgeladen: <code>{upload}</code> Mbit/s</b>\n"
            "<b>Server-Ping: <code>{ping}</code> Ms</b>"
    }

    strings_fr = {
        "<b>Chargé: <code>{dowload}</code> Mbit/s</b>\n"
            "<b>Téléchargé: <code>{upload}</code> Mbit/s</b>\n"
            "<b>Ping serveur: <code>{ping}</code> ms</b>"
    }
    strings_uk = {
        "<b>Завантажено: <code>{dowload}</code> Мбiт/с</b>\n"
            "<b>Вивантажено: <code>{upload}</code> Мбiт/с</b>\n"
            "<b>Пінг сервера: <code>{ping}</code> мс</b>"
    }

    strings_tr = {
        "<b>Yüklendi: <code>{dowload}</code>Mbps</b>\n"
            "<b>yüklendi: <code>{upload}</code>Mbps</b>\n"
            "<b>Sunucu Pingi: <code>{ping}</code>ms</b>"
    }



    
    async def speedcmd(self, message:Message):
        """ - start speedtest"""
        s = await utils.answer(message, self.strings("speedtest"))
        results = await utils.run_sync(self.run_speedtest)
        await utils.answer(
            s,
            self.strings("speed").format(
            dowload=round(results[0] / 1024 / 1024),
            upload=round(results[1] / 1024 / 1024),
            ping=round(results[2], 3),
            ),
        )


    @staticmethod
    def run_speedtest() -> Tuple[float, float, float]:
        """Speedtest using `speedtest` library."""

        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]
