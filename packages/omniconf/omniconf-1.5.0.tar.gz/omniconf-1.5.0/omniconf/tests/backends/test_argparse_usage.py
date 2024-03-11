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

import sys
import unittest
from collections import OrderedDict
from io import StringIO
from unittest.mock import patch

from omniconf.backends.argparse import ArgparseUsageInformation, format_argparse_key
from omniconf.setting import Setting, SettingRegistry

SETTINGS = [
    Setting("module1.str", _type=str, help="Optional str argument."),
    Setting("module1.int", _type=int, help="Optional int argument."),
    Setting("module1.required", _type=str, required=True, help="Required str argument."),
    Setting("module1.default", _type=str, default="foo", help="Optional str argument with default."),
    Setting("module2.setting", _type=str, help="Optional str argument."),
    Setting("module2.bool_flag", _type=str, default=False, help="Optional boolean flag with default."),
    Setting("zmodule", _type=str, help="Optional, top-level str argument."),
    Setting("xmodule.setting", _type=str, help="Optional str argument."),
]

ORDERED_SETTINGS = [
    "zmodule",
    "module1.default",
    "module1.int",
    "module1.required",
    "module1.str",
    "module2.bool_flag",
    "module2.setting",
    "xmodule.setting",
]

GROUPED_SETTINGS = OrderedDict(
    (
        ("_", ["zmodule"]),
        ("module1", ["module1.default", "module1.int", "module1.required", "module1.str"]),
        ("module2", ["module2.bool_flag", "module2.setting"]),
        ("xmodule", ["xmodule.setting"]),
    )
)


class TestArgparseUsageInformation(unittest.TestCase):
    def setUp(self) -> None:
        registry = SettingRegistry()
        for setting in SETTINGS:
            registry.add(setting)
        self.registry = registry
        self.usage = ArgparseUsageInformation(registry)

    def test_argparse_usage_information_group_settings(self) -> None:
        keys, groups = self.usage.group_settings()
        assert keys == ORDERED_SETTINGS
        assert groups == GROUPED_SETTINGS

    def test_argparse_usage_information_print_usage_expected_options(self) -> None:
        buf = StringIO()
        self.usage.print_usage(out=buf)
        message = buf.getvalue()
        for setting in ORDERED_SETTINGS:
            _, _, _arg = format_argparse_key(setting)
            self.assertIn(_arg, message)

    def test_argparse_usage_information_print_usage_expected_groups(self) -> None:
        buf = StringIO()
        self.usage.print_usage(out=buf)
        message = buf.getvalue()
        for group in GROUPED_SETTINGS:
            if group == "_":
                if sys.version_info < (3, 10):
                    group = "optional arguments"
                else:
                    group = "options"

            self.assertIn(group + ":", message)

    def test_argparse_usage_check_flag_not_specified(self) -> None:
        self.assertFalse(self.usage.check_flag(["--nope"]))

    def test_argparse_usage_check_flag_specified(self) -> None:
        with patch("omniconf.backends.argparse.ARGPARSE_SOURCE", ["--yep"]):
            self.assertTrue(self.usage.check_flag(["--yep"]))
