# Copyright (c) 2016 Cyso < development [at] cyso . com >
#
# This file is part of omniconf, a.k.a. python-omniconf .
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see
# <http://www.gnu.org/licenses/>.


from abc import ABC, abstractmethod
from contextlib import suppress
from typing import Any, Mapping, Optional, Sequence, Tuple

from omniconf.config import ConfigRegistry
from omniconf.setting import Setting


class ConfigBackend(ABC):
    """
    Defines a configuration backend, which provides configuration values
    based on keys.
    """

    @classmethod
    def autodetect_settings(cls, autoconfigure_prefix: Optional[str]) -> Sequence[Setting]:
        """
        Returns a tuple of :class:`.Setting` objects, that are required for
        :func:`autoconfigure` to complete successfully.
        """
        return ()

    @classmethod
    @abstractmethod
    def autoconfigure(
        cls, conf: ConfigRegistry, autoconfigure_prefix: Optional[str]
    ) -> Optional["ConfigBackend"]:  # pragma: nocover
        """
        Called with a :class:`.ConfigRegistry`, the result of this method must
        be either a new instance of this class, or :any:`None`. This method
        is automatically called during the autoconfigure phase.
        """
        ...

    @abstractmethod
    def get_value(self, setting: Setting) -> Any:  # pragma: nocover
        """
        Retrieves the value for the given :class:`.Setting`.
        """
        ...

    def get_values(self, settings: Sequence[Setting]) -> Sequence[Tuple[Setting, Any]]:
        """
        Retrieves a list of :class:`.Setting`s all at once. Values are returned
        as a sequence of tuples containing the :class:`.Setting` and value.
        """
        values = []
        for setting in settings:
            with suppress(KeyError):
                values.append((setting, self.get_value(setting)))
        return values


class DictConfigBackend(ConfigBackend):
    def __init__(self, conf: Mapping[str, Any]):
        self.config = conf

    def get_value(self, setting: Setting) -> Any:
        section = self.config
        for _key in setting.key.split("."):
            section = section[_key]
        return section
