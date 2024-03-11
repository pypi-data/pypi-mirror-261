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

from io import StringIO
from typing import Optional, Type
from unittest.mock import mock_open, patch

import pytest

from omniconf.backends import available_backends
from omniconf.backends.json import JsonBackend
from omniconf.config import ConfigRegistry
from omniconf.setting import Setting, SettingRegistry

JSON_FILE = """
{
    "foo": "bar",
    "section": {
        "bar": "baz",
        "subsection": {
            "baz": "foo"
        }
    }
}
"""

CONFIGS = [
    ("foo", "bar", None),
    ("section.bar", "baz", None),
    ("section.subsection.baz", "foo", None),
    ("", None, KeyError),
    ("section", {"bar": "baz", "subsection": {"baz": "foo"}}, None),
    ("unknown", None, KeyError),
]


def test_json_backend_in_available_backends() -> None:
    assert JsonBackend in available_backends


@patch("builtins.open", mock_open(read_data=JSON_FILE))
def test_json_backend_autoconfigure() -> None:
    prefix = "testconf"
    settings = SettingRegistry()
    settings.add(JsonBackend.autodetect_settings(prefix)[0])
    conf = ConfigRegistry(setting_registry=settings)

    backend = JsonBackend.autoconfigure(conf, prefix)
    assert backend is None

    conf.set("{0}.json.filename".format(prefix), "bar")
    backend = JsonBackend.autoconfigure(conf, prefix)
    assert isinstance(backend, JsonBackend)


@pytest.mark.parametrize("key,value,sideeffect", CONFIGS)
def test_get_value(key: str, value: Optional[str], sideeffect: Optional[Type[BaseException]]) -> None:
    f = StringIO(JSON_FILE)
    backend = JsonBackend(f)
    setting = Setting(key=key, _type=str)
    if sideeffect:
        with pytest.raises(sideeffect):
            backend.get_value(setting)
    else:
        assert backend.get_value(setting) == value
