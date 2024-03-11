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

from typing import Optional

from omniconf.backends.generic import ConfigBackend, DictConfigBackend
from omniconf.config import ConfigRegistry
from omniconf.setting import Setting


class MockConfigBackend(DictConfigBackend):
    @classmethod
    def autoconfigure(cls, conf: ConfigRegistry, autoconfigure_prefix: Optional[str]) -> Optional["ConfigBackend"]:
        return None


def test_config_backend_autodetect_settings() -> None:
    assert MockConfigBackend.autodetect_settings(None) == ()


def test_config_backend_get_values_no_settings() -> None:
    assert MockConfigBackend({}).get_values([]) == []


def test_config_backend_get_values_missing_value() -> None:
    backend = MockConfigBackend(conf={})
    setting = Setting("foo", _type=str)
    values = backend.get_values([setting])
    assert values == []


def test_config_backend_get_values() -> None:
    backend = MockConfigBackend(conf={"foo": "bar"})
    setting = Setting("foo", _type=str)
    values = backend.get_values([setting])
    assert values == [(setting, "bar")]
