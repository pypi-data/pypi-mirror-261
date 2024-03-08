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

from io import BytesIO

from team.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from team.raw.core import TLObject
from team import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ChatParticipantCreator(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~team.raw.base.ChatParticipant`.

    Details:
        - Layer: ``158``
        - ID: ``E46BCEE4``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id"]

    ID = 0xe46bcee4
    QUALNAME = "types.ChatParticipantCreator"

    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantCreator":
        # No flags
        
        user_id = Long.read(b)
        
        return ChatParticipantCreator(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
