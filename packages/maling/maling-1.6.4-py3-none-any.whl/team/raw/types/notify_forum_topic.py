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


class NotifyForumTopic(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~team.raw.base.NotifyPeer`.

    Details:
        - Layer: ``158``
        - ID: ``226E6308``

    Parameters:
        peer (:obj:`Peer <team.raw.base.Peer>`):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "top_msg_id"]

    ID = 0x226e6308
    QUALNAME = "types.NotifyForumTopic"

    def __init__(self, *, peer: "raw.base.Peer", top_msg_id: int) -> None:
        self.peer = peer  # Peer
        self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotifyForumTopic":
        # No flags
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b)
        
        return NotifyForumTopic(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_msg_id))
        
        return b.getvalue()
