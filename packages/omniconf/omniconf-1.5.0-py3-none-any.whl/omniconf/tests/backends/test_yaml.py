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
from omniconf.backends.yaml import YamlBackend
from omniconf.config import ConfigRegistry
from omniconf.setting import Setting, SettingRegistry

YAML_FILE = """
---
foo: bar
section:
  bar: baz
  subsection:
    baz: foo
---
bar:
  sub: bar-sub-value
"""

CONFIGS = [
    ("foo", "bar", None),
    ("section.bar", "baz", None),
    ("section.subsection.baz", "foo", None),
    ("", None, KeyError),
    ("section", {"bar": "baz", "subsection": {"baz": "foo"}}, None),
    ("unknown", None, KeyError),
    ("bar.sub", "bar-sub-value", None),
]


def test_yaml_backend_in_available_backends() -> None:
    assert YamlBackend in available_backends


@patch("builtins.open", mock_open(read_data=YAML_FILE))
def test_yaml_backend_autoconfigure() -> None:
    prefix = "testconf"
    settings = SettingRegistry()
    settings.add(YamlBackend.autodetect_settings(prefix)[0])
    conf = ConfigRegistry(setting_registry=settings)

    backend = YamlBackend.autoconfigure(conf, prefix)
    assert backend is None

    conf.set("{0}.yaml.filename".format(prefix), "bar")
    backend = YamlBackend.autoconfigure(conf, prefix)
    assert isinstance(backend, YamlBackend)


@pytest.mark.parametrize("key,value,sideeffect", CONFIGS)
def test_get_value(key: str, value: Optional[str], sideeffect: Optional[Type[BaseException]]) -> None:
    f = StringIO(YAML_FILE)
    backend = YamlBackend(f)
    setting = Setting(key=key, _type=str)
    if sideeffect:
        with pytest.raises(sideeffect):
            backend.get_value(setting)
    else:
        assert backend.get_value(setting) == value
