"""
 Socket provider for all data sockets used by algorithms.
"""
import json

#  Copyright (c) 2023-2024. ECCO Sneaks & Data
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from typing import final, Optional

from adapta.process_communication import DataSocket


@final
class ExternalSocketProvider:
    """
    Wraps a socket collection
    """

    def __init__(self, *sockets: DataSocket):
        self._sockets = {socket.alias: socket for socket in sockets}

    def socket(self, name: str) -> Optional[DataSocket]:
        """
        Retrieve a socket if it exists.
        """
        return self._sockets.get(name, None)

    @classmethod
    def from_serialized(cls, socket_list_ser: str) -> "ExternalSocketProvider":
        """
        Creates a SocketProvider from a list of serialized sockets
        """
        return cls(
            *[
                DataSocket.from_dict(socket_dict)
                for socket_dict in json.loads(socket_list_ser)
            ]
        )
