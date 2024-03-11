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

from typing import Optional, Sequence, TextIO

from configobj import ConfigObj

from omniconf.backends.generic import ConfigBackend, DictConfigBackend
from omniconf.config import ConfigRegistry
from omniconf.keys import join_key
from omniconf.setting import Setting


class ConfigObjBackend(DictConfigBackend):
    """
    Uses a ConfigObj file (or :mod:`StringIO` instance) as a backend, and
    allows values in it to be retrieved using dotted keys.

    Dots in the keys denote a section in the ConfigObj document. For instance,
    the key `section.subsection.key` will correspond to this document::

        [section]
        [[subsection]]
        key=value

    """

    def __init__(self, conf: TextIO) -> None:
        super(ConfigObjBackend, self).__init__(ConfigObj(conf).dict())

    @classmethod
    def autodetect_settings(cls, autoconfigure_prefix: Optional[str]) -> Sequence[Setting]:
        return (Setting(key=join_key(autoconfigure_prefix, "configobj", "filename"), _type=str, required=False),)

    @classmethod
    def autoconfigure(cls, conf: ConfigRegistry, autoconfigure_prefix: Optional[str]) -> Optional[ConfigBackend]:
        filename_key = join_key(autoconfigure_prefix, "configobj", "filename")
        if conf.has(filename_key) and (filename := conf.get(filename_key)):
            with open(filename) as config_file:
                return ConfigObjBackend(conf=config_file)
        return None
