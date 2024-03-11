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
from typing import Optional, Sequence, TextIO

from omniconf.backends.argparse import ArgparseUsageInformation
from omniconf.setting import DEFAULT_REGISTRY as SETTING_REGISTRY
from omniconf.setting import SettingRegistry


def help_requested() -> bool:
    """
    Returns True if `-h` or `--help` was specified on the command line.
    """
    return flag_requested(["-h", "--help"])


def version_requested() -> bool:
    """
    Returns True if `-v` or `--version` was specified on the command line.
    """
    return flag_requested(["-v", "--version"])


def flag_requested(flags: Sequence[str]) -> bool:
    """
    Returns True if the specified list of flags were specified on the
    command line.
    """
    return ArgparseUsageInformation.check_flag(flags)


def show_usage(
    setting_registry: Optional[SettingRegistry] = None,
    name: Optional[str] = None,
    top_message: Optional[str] = None,
    bottom_message: Optional[str] = None,
    out: Optional[TextIO] = None,
    exit: int = 0,
) -> None:
    """
    Prints usage information based on :class:`.Setting` objects in the given
    :class:`.SettingRegistry`. If no `setting_registry` is specified, the
    default :class:`.SettingRegistry` is used.

    If no `name` is specified, `sys.argv[0]` is used. Additionally, a header
    and footer message may be supplied using `top_message` and `bottom_message`
    message respectively.

    By default the usage information is output to `sys.stderr`. This can be
    overidden by specifying a different File-like object to `out`.

    By default, this function will call `sys.exit` and stop the program with
    exit code 0. This can be overridden by a specifying different value to
    `exit`. Set to False to not exit.
    """
    if not setting_registry:
        setting_registry = SETTING_REGISTRY

    ArgparseUsageInformation(
        setting_registry=setting_registry, name=name, top_message=top_message, bottom_message=bottom_message
    ).print_usage(out=out)

    if exit is not False:
        sys.exit(exit)
