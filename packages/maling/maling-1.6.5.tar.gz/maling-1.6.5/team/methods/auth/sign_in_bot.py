#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import logging

import team
from team import raw
from team import types
from team.errors import UserMigrate
from team.session import Session, Auth

log = logging.getLogger(__name__)


class SignInBot:
    async def sign_in_bot(
        self: "team.Client",
        bot_token: str
    ) -> "types.User":
        """Authorize a bot using its bot token generated by BotFather.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            bot_token (``str``):
                The bot token generated by BotFather

        Returns:
            :obj:`~team.types.User`: On success, the bot identity is return in form of a user object.

        Raises:
            BadRequest: In case the bot token is invalid.
        """
        while True:
            try:
                r = await self.invoke(
                    raw.functions.auth.ImportBotAuthorization(
                        flags=0,
                        api_id=self.api_id,
                        api_hash=self.api_hash,
                        bot_auth_token=bot_token
                    )
                )
            except UserMigrate as e:
                await self.session.stop()

                await self.storage.dc_id(e.value)
                await self.storage.auth_key(
                    await Auth(
                        self, await self.storage.dc_id(),
                        await self.storage.test_mode()
                    ).create()
                )
                self.session = Session(
                    self, await self.storage.dc_id(),
                    await self.storage.auth_key(), await self.storage.test_mode()
                )

                await self.session.start()
            else:
                await self.storage.user_id(r.user.id)
                await self.storage.is_bot(True)

                return types.User._parse(self, r.user)
