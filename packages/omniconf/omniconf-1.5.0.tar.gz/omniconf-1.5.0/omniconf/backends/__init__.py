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

from typing import List, Type

from omniconf.backends.argparse import ArgparseBackend
from omniconf.backends.env import EnvBackend
from omniconf.backends.generic import ConfigBackend
from omniconf.backends.json import JsonBackend

available_backends: List[Type[ConfigBackend]] = []
autodetection_backends: List[Type[ConfigBackend]] = []

try:
    from omniconf.backends.configobj import ConfigObjBackend

    available_backends.append(ConfigObjBackend)
except ImportError:  # pragma: nocover
    pass

try:
    from omniconf.backends.yaml import YamlBackend

    available_backends.append(YamlBackend)
except ImportError:  # pragma: nocover
    pass

try:
    from omniconf.backends.toml import TomlBackend

    available_backends.append(TomlBackend)
except ImportError:  # pragma: nocover
    pass

available_backends += [JsonBackend, EnvBackend, ArgparseBackend]
autodetection_backends += [EnvBackend, ArgparseBackend]


__all__ = ["available_backends", "autodetection_backends"]
