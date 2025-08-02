# Name: Keepermod
# Description: Module for save self-destructing images
# Author: @sansaramods
# Commands:
# .kp | .akp
# ---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/exodiast
#-----------------------------------------------------------------------------------
# meta developer: @sansaramods
#-----------------------------------------------------------------------------------

__version__ = (1, 0, 0)

import io

from telethon import types

from .. import loader, utils


@loader.tds
class KeeperMod(loader.Module):
    strings = {"name": "Keeper"}

    async def client_ready(self, client, db):
        self.db = db

    @loader.owner
    async def kpcmd(self, m: types.Message):
        ".kp <reply> - save a self-destructing photo"
        reply = await m.get_reply_message()
        if not reply or not reply.media or not reply.media.ttl_seconds:
            return await m.edit("Интересно")
        await m.delete()
        new = io.BytesIO(await reply.download_media(bytes))
        new.name = reply.file.name
        await m.client.send_file("me", new)

    @loader.owner
    async def akpcmd(self, m: types.Message):
        "toggle photo auto-upload mode in PM"
        new_val = not self.db.get("Keeper", "state", False)
        self.db.set("Keeper", "state", new_val)
        await utils.answer(m, f"<b>[Keeper]</b> <pre>{new_val}</pre>")

    async def watcher(self, m: types.Message):
        if (
            m
            and m.media
            and m.media.ttl_seconds
            and self.db.get("Keeper", "state", False)
        ):
            new = io.BytesIO(await m.download_media(bytes))
            new.name = m.file.name
            await m.client.send_file(
                "me",
                new,
                caption=(
                    "<b>[Keeper] Photo from</b>"
                    f" {f'@{m.sender.username}' if m.sender.username else m.sender.first_name} |"
                    f" <pre>{m.sender.id}</pre>\nTime of life:"
                    f" <code>{m.media.ttl_seconds}sec</code>"
                ),
            )

























































