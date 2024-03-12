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

import os
from typing import Optional, Type
from unittest.mock import patch

import pytest

from omniconf.backends import available_backends
from omniconf.backends.env import EnvBackend
from omniconf.config import ConfigRegistry
from omniconf.setting import Setting, SettingRegistry

ENV_FILE = {
    "COLORTERM": "gnome-terminal",
    "DESKTOP_MODE": "1",
    "DESKTOP_SESSION": "ubuntu",
    "DISPLAY": ":0",
    "EDITOR": "vim",
    "HOME": "/home/user/workspace/omniconf",
    "LANG": "en_US.UTF-8",
    "LANGUAGE": "en_US:",
    "LC_ADDRESS": "nl_NL.UTF-8",
    "LC_IDENTIFICATION": "nl_NL.UTF-8",
    "LC_MEASUREMENT": "nl_NL.UTF-8",
    "LC_MONETARY": "nl_NL.UTF-8",
    "LC_NAME": "nl_NL.UTF-8",
    "LC_NUMERIC": "nl_NL.UTF-8",
    "LC_PAPER": "nl_NL.UTF-8",
    "LC_TELEPHONE": "nl_NL.UTF-8",
    "LC_TIME": "nl_NL.UTF-8",
    "OLDPWD": "/home/user",
    "PATH": "/foo/bar/baz",
    "PWD": "/home/user",
    "SHELL": "/bin/bash",
    "TERM": "xterm",
    "USER": "user",
    "_": "/home/user/workspace/omniconf/vendor/bin/python",
    "TEST_FOO": "bar",
    "TEST_SECTION_BAR": "baz",
    "TEST_SECTION_SUBSECTION_BAZ": "foo",
}

CONFIGS = [
    ("foo", "bar", None),
    ("section.bar", "baz", None),
    ("section.subsection.baz", "foo", None),
    ("", None, KeyError),
    ("section", None, KeyError),
    ("unknown", None, KeyError),
]


def test_env_backend_in_available_backends() -> None:
    assert EnvBackend in available_backends


def test_env_backend_autoconfigure() -> None:
    prefix = "testconf"
    settings = SettingRegistry()
    settings.add(Setting(f"{prefix}.prefix", _type=str))
    configs = ConfigRegistry(settings)
    configs.set(f"{prefix}.prefix", "bla")
    backend = EnvBackend.autoconfigure(configs, prefix)
    assert isinstance(backend, EnvBackend)
    assert backend.prefix == "bla"


@pytest.mark.parametrize("key,value,sideeffect", CONFIGS)
def test_get_value(key: str, value: Optional[str], sideeffect: Optional[Type[BaseException]]) -> None:
    with patch.dict(os.environ, ENV_FILE):
        backend = EnvBackend(prefix="TEST")
        setting = Setting(key=key, _type=str)
        if sideeffect:
            with pytest.raises(sideeffect):
                backend.get_value(setting)
        else:
            assert backend.get_value(setting) == value
