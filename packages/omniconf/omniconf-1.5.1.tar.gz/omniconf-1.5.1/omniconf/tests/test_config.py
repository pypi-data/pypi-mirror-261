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

import unittest
from typing import Any, Optional, Type
from unittest.mock import Mock

import pytest

from omniconf.backends.generic import ConfigBackend
from omniconf.config import DEFAULT_REGISTRY as CONFIG_REGISTRY
from omniconf.config import ConfigRegistry, config
from omniconf.exceptions import UnconfiguredSettingError, UnknownSettingError
from omniconf.setting import DEFAULT_REGISTRY as SETTING_REGISTRY
from omniconf.setting import Setting, SettingRegistry
from omniconf.types import CallableType


class TestConfigRegistry(unittest.TestCase):
    def setUp(self) -> None:
        self.test_settings = [
            Setting("key", _type=str, required=True),
            Setting("default", _type=str, default="present"),
        ]
        self.setting_registry = SettingRegistry()
        for setting in self.test_settings:
            self.setting_registry.add(setting)
        self.config_registry = ConfigRegistry(setting_registry=self.setting_registry)

    def test_config_registry_clear(self) -> None:
        self.assertEqual(len(self.setting_registry.registry), 2)
        self.setting_registry.clear()
        self.assertEqual(len(self.setting_registry.registry), 0)

    def test_config_registry_set_without_setting(self) -> None:
        with self.assertRaises(UnknownSettingError):
            self.config_registry.set("nope", "value")

    def test_config_registry_set_with_setting(self) -> None:
        self.config_registry.set("key", "value")
        self.assertEqual(self.config_registry.registry["key"], "value")

    def test_config_registry_has(self) -> None:
        self.assertFalse(self.config_registry.has("key"))
        self.config_registry.set("key", "added")
        self.assertTrue(self.config_registry.has("key"))

    def test_config_registry_has_with_default(self) -> None:
        self.assertTrue(self.config_registry.has("default"))

    def test_config_registry_get_without_config(self) -> None:
        with self.assertRaises(UnconfiguredSettingError):
            self.config_registry.get("nope")

    def test_config_registry_get(self) -> None:
        self.config_registry.set("key", "value")
        self.assertEqual(self.config_registry.get("key"), "value")

    def test_config_registry_get_with_default(self) -> None:
        self.assertEqual(self.config_registry.get("default"), "present")

    def test_config_registry_get_not_required_no_value(self) -> None:
        self.setting_registry.add(Setting("unneeded", _type=str))
        self.assertIs(self.config_registry.get("unneeded"), None)

    def test_config_registry_list(self) -> None:
        self.assertEqual(self.config_registry.list(), self.config_registry.registry)

    def test_config_registry_unset(self) -> None:
        self.config_registry.set("key", "soon")
        self.assertEqual(self.config_registry.get("key"), "soon")
        self.config_registry.unset("key")
        with self.assertRaises(UnconfiguredSettingError):
            self.config_registry.get("key")

    def test_config_registry_load(self) -> None:
        mock_backend = Mock(autospec=ConfigBackend)
        mock_backend.get_values.return_value = [(s, "value") for s in self.test_settings]
        self.config_registry.load([mock_backend])

        mock_backend.get_values.assert_called_once_with(self.test_settings)
        self.assertEqual(self.config_registry.get("key"), "value")
        self.assertEqual(self.config_registry.get("default"), "value")

    def test_config_registry_load_with_previous_values(self) -> None:
        mock_backend = Mock(autospec=ConfigBackend)
        mock_backend.get_values.return_value = [(s, "value") for s in self.test_settings]
        self.config_registry.set("key", "other")
        self.config_registry.set("default", "other")

        self.config_registry.load([mock_backend])

        self.assertEqual(self.config_registry.get("key"), "other")
        self.assertEqual(self.config_registry.get("default"), "other")

    def test_config_registry_load_with_unavailable_values(self) -> None:
        mock_backend = Mock(autospec=ConfigBackend)
        mock_backend.get_values.return_value = []

        with self.assertRaises(UnconfiguredSettingError):
            self.config_registry.load([mock_backend])

    def test_config_registry_load_value_error(self) -> None:
        int_setting = Setting(key="foo", _type=int)
        self.setting_registry.add(int_setting)

        mock_backend = Mock(autospec=ConfigBackend)
        mock_backend.get_values.return_value = [(int_setting, "bar")]

        with self.assertRaises(ValueError):
            self.config_registry.load([mock_backend])


class TestConfigMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.setting_registry = SettingRegistry()
        self.setting_registry.add(Setting("key", _type=str, required=True))
        self.setting_registry.add(Setting("default", _type=str, default="present"))
        self.config_registry = ConfigRegistry(setting_registry=self.setting_registry)

    def test_config_method_without_config(self) -> None:
        with self.assertRaises(UnconfiguredSettingError):
            config("key", registry=self.config_registry)

    def test_config_method(self) -> None:
        self.config_registry.set("key", "value")
        self.assertEqual(config("key", registry=self.config_registry), "value")

    def test_config_method_with_default(self) -> None:
        self.assertEqual(config("default", registry=self.config_registry), "present")

    def test_config_method_with_default_registry(self) -> None:
        with self.assertRaises(UnconfiguredSettingError):
            config("foo")

        _setting = Setting(key="foo", _type=str)
        SETTING_REGISTRY.add(_setting)
        CONFIG_REGISTRY.set("foo", "bar")
        self.assertEqual(config("foo"), "bar")

        CONFIG_REGISTRY.unset("foo")
        SETTING_REGISTRY.remove(_setting)


VALUE_TESTS = [
    # Normal values
    ("foobar", "foobar", str, None),
    (123456, "123456", str, None),
    ("1234", 1234, int, None),
    ("123.456", 123.456, float, None),
    ("['a', 'b', '1', 'c']", ["a", "b", "1", "c"], list, None),
    ("('a', 'b', '1', 'c')", ("a", "b", "1", "c"), tuple, None),
    ("{'a': 'b', 'foo': 'bar'}", {"a": "b", "foo": "bar"}, dict, None),
    ("False", False, bool, None),
    ("True", True, bool, None),
    (False, False, bool, None),
    # Value is False codepath
    (False, False, list, None),
    # Exception codepath
    ("foobar", None, int, ValueError),
    ("foobar", None, float, ValueError),
    ("foobar", None, list, ValueError),
    ("foobar", None, dict, ValueError),
]


@pytest.mark.parametrize("_in,_out,_type,side_effect", VALUE_TESTS)
def test_config_registry_set_value_conversion(
    _in: Any, _out: Any, _type: CallableType, side_effect: Optional[Type[BaseException]]
) -> None:
    settings = SettingRegistry()
    settings.add(Setting("test.value", _type=_type))

    configs = ConfigRegistry(setting_registry=settings)

    if side_effect:
        with pytest.raises(side_effect):
            configs.set("test.value", _in)
    else:
        configs.set("test.value", _in)
        assert configs.get("test.value") == _out
