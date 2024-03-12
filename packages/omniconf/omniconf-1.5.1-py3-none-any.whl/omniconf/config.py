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

import ast
from collections import OrderedDict
from typing import TYPE_CHECKING, Any, Dict, Optional, Sequence

from omniconf.exceptions import UnconfiguredSettingError, UnknownSettingError
from omniconf.setting import DEFAULT_REGISTRY as SETTING_REGISTRY
from omniconf.setting import SettingRegistry
from omniconf.types import CallableType

if TYPE_CHECKING:  # pragma: nocover
    from omniconf.backends.generic import ConfigBackend

UnreprType = (list, dict, tuple, bool)


def unrepr(src: Any, _type: CallableType) -> Any:
    """
    Returns an interpreted value based on ``src``. If ``source`` is already an
    instance of ``_type``, no interpretation is performed.
    """
    if isinstance(src, _type):  # type: ignore[arg-type]
        return src
    if not src:
        return src
    return ast.literal_eval(src)


class ConfigRegistry:
    """
    A registry of Configured values for a :class:`.SettingRegistry`.
    """

    def __init__(self, setting_registry: Optional[SettingRegistry] = None) -> None:
        if not setting_registry:
            self.settings = SETTING_REGISTRY
        else:
            self.settings = setting_registry
        self.clear()

    def clear(self) -> None:
        self.registry: Dict[str, Any] = OrderedDict()

    def set(self, key: str, value: str) -> None:
        """
        Configures the value for the given key. The value will be converted to
        the type defined in the :class:`.Setting`, by calling the type as a
        function with the value as the only argument. Trying to configure a
        value under an unknown key will result in an UnknownSettingError.
        """
        if not self.settings.has(key):
            raise UnknownSettingError("Trying to configure unregistered key " "{0}".format(key))
        setting = self.settings.get(key)

        if setting.type in UnreprType:
            self.registry[key] = unrepr(value, setting.type)
        else:
            self.registry[key] = setting.type(value)

    def has(self, key: str) -> bool:
        """
        Checks if a value has been configured for the given key, or if a
        default value is present.
        """
        if key in self.registry or (self.settings.has(key) and self.settings.get(key).default is not None):
            return True
        return False

    def get(self, key: str) -> Optional[Any]:
        """
        Returns the configured value for the given key, or the default value if
        the key was not configured.
        """
        if key in self.registry:
            return self.registry[key]
        elif self.settings.has(key) and self.settings.get(key).default is not None:
            return self.settings.get(key).default
        elif self.settings.has(key) and not self.settings.get(key).required:
            return None
        raise UnconfiguredSettingError("No value or default available for {0}".format(key))

    def list(self) -> Dict[str, Any]:
        """
        Returns all configured values as a dict.
        """
        return self.registry

    def unset(self, key: str) -> None:
        """
        Removes the value for a given key from the registry.
        """
        if key in self.registry:
            del self.registry[key]

    def load(self, backends: Sequence["ConfigBackend"]) -> None:
        """
        Attempt to configure all settings defined in the
        :class:`.SettingRegistry` using the provided backends. If a setting
        was attempting to load, and no value found and no default was set, an
        UnconfiguredSettingError is raised.
        """
        for backend in backends:
            for setting, value in backend.get_values(self.settings.list()):
                if setting.key in self.registry:
                    continue
                try:
                    self.set(setting.key, value)
                except ValueError as ve:
                    raise ValueError("An invalid value was specified for " "{0}: {1}".format(setting.key, ve)) from None

        missing_settings = []
        for setting in self.settings.list():
            if not self.has(setting.key) and setting.required:
                missing_settings.append(setting.key)
        if missing_settings:
            raise UnconfiguredSettingError("No value was configured for: {0}".format(", ".join(missing_settings)))


DEFAULT_REGISTRY = ConfigRegistry()
"""
Global :class:`.ConfigRegistry` which will be used when no specific
:class:`.ConfigRegistry` is defined.
"""


def config(key: str, registry: Optional[ConfigRegistry] = None) -> Optional[Any]:
    """
    Retrieves the configured value for a given key. If no specific registry is
    specified, the value will be retrieved from the default
    :class:`.ConfigRegistry`.
    """
    if not registry:
        registry = DEFAULT_REGISTRY

    return registry.get(key)
