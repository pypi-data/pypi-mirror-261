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

from typing import Any, Optional, Type
from unittest.mock import patch

import pytest

from omniconf.backends import available_backends
from omniconf.backends.argparse import ArgparseBackend
from omniconf.config import ConfigRegistry
from omniconf.setting import Setting, SettingRegistry

ARGS_FILE = [
    "--foo",
    "bar",
    "--section-bar",
    "baz",
    "--section-subsection-baz",
    "foo",
    "--bool-normal",
    "1",
    "--bool-true",
    "--bool-false",
    "--missing-value",  # Has to be the last because we're omitting the value
]

PREFIX_ARGS_FILE = [
    "--prefix-foo",
    "bar",
    "--prefix-section-bar",
    "baz",
    "--prefix-section-subsection-baz",
    "foo",
    "--prefix-bool-normal",
    "1",
    "--prefix-bool-true",
    "--prefix-bool-false",
    "--prefix-missing-value",  # Has to be the last because we're omitting the value
]

CONFIGS = [
    (Setting(key="foo", _type=str), "bar", None),
    (Setting(key="section.bar", _type=str), "baz", None),
    (Setting(key="section.subsection.baz", _type=str), "foo", None),
    (Setting(key="", _type=str), None, KeyError),
    (Setting(key="missing.value", _type=str), None, KeyError),
    (Setting(key="missing.arg", _type=str), None, IndexError),  # Raise in test
    (Setting(key="bool.normal", _type=bool), "1", None),
    (Setting(key="bool.true", _type=bool, default=False), True, None),
    (Setting(key="bool.false", _type=bool, default=True), False, None),
    (Setting(key="bool.default.true", _type=bool, default=True), True, None),
    (Setting(key="bool.default.false", _type=bool, default=False), False, None),
]


def test_argparse_backend_in_available_backends() -> None:
    assert ArgparseBackend in available_backends


def test_argparse_backend_autoconfigure() -> None:
    prefix = "testconf"
    settings = SettingRegistry()
    settings.add(Setting(f"{prefix}.prefix", _type=str))
    configs = ConfigRegistry(settings)
    configs.set(f"{prefix}.prefix", "bar")
    backend = ArgparseBackend.autoconfigure(configs, prefix)
    assert isinstance(backend, ArgparseBackend)
    assert backend.prefix == "bar"


def test_argparse_backend_get_value() -> None:
    with pytest.raises(NotImplementedError):
        backend = ArgparseBackend()
        backend.get_value(Setting("Foo", str))


@pytest.mark.parametrize("setting,value,sideeffect", CONFIGS)
def test_argparse_backend_get_values(setting: Setting, value: Any, sideeffect: Optional[Type[BaseException]]) -> None:
    _test_get_values(setting, value, sideeffect, None)
    _test_get_values(setting, value, sideeffect, "prefix")


def _test_get_values(
    setting: Setting, value: Any, sideeffect: Optional[Type[BaseException]], prefix: Optional[str]
) -> None:
    with patch("omniconf.backends.argparse.ARGPARSE_SOURCE", ARGS_FILE if not prefix else PREFIX_ARGS_FILE):
        backend = ArgparseBackend(prefix=prefix)
        if sideeffect:
            with pytest.raises(sideeffect):
                setting, config = backend.get_values([setting])[0]
        else:
            setting, config = backend.get_values([setting])[0]
            assert config == value


def test_mixed_flags_and_settings() -> None:
    MIXED_ARGS = ["--verbose", "--loud", "--foo-bar", "baz", "--bar", "buzz"]

    settings = SettingRegistry()
    settings.add(Setting(key="verbose", _type=bool, default=False))
    settings.add(Setting(key="loud", _type=bool, default=True))
    settings.add(Setting(key="foo.bar", _type=str))
    settings.add(Setting(key="bar", _type=str))
    configs = ConfigRegistry(setting_registry=settings)

    with patch("omniconf.backends.argparse.ARGPARSE_SOURCE", MIXED_ARGS):
        backend = ArgparseBackend(prefix=None)
        configs.load([backend])

        assert configs.get("verbose") is True
        assert configs.get("loud") is False
        assert configs.get("foo.bar") == "baz"
        assert configs.get("bar") == "buzz"
