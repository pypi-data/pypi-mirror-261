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

from typing import Any, Optional, Sequence, Type, Union

import pytest

from omniconf.types import enum, separator_sequence, string_bool, string_or_false

SEPARATOR_SEQUENCES = [
    ("", ",", [""]),
    ("a", ",", ["a"]),
    ("a,b,c", ",", ["a", "b", "c"]),
    ("foo,bar;baz;", ";", ["foo,bar", "baz", ""]),
    (["foo", "bar"], ",", ["foo", "bar"]),
    ([], ",", []),
]


@pytest.mark.parametrize("_in,_sep,_out", SEPARATOR_SEQUENCES)
def test_separator_sequence(_in: Union[str, Sequence[str]], _sep: str, _out: Sequence[str]) -> None:
    seq = separator_sequence(_sep)(_in)
    assert list(seq) == _out
    assert seq.__str__() == _out.__str__()


STRING_OR_FALSE = [("foo", "foo"), ("bar", "bar"), (123, 123), ("False", False), (None, None)]


@pytest.mark.parametrize("_in,_out", STRING_OR_FALSE)
def test_string_or_false(_in: Any, _out: Any) -> None:
    assert string_or_false(_in) == _out


STRING_BOOL = [
    (0, False),
    ("", False),
    ([], False),
    ({}, False),
    ("False", False),
    (False, False),
    ("True", True),
    (True, True),
    ("0", "0"),
    (1, 1),
    ("1", "1"),
]


@pytest.mark.parametrize("_in,_out", STRING_BOOL)
def test_string_bool(_in: Any, _out: Any) -> None:
    assert string_bool(_in) == _out


ENUM = enum(["foo", "bar", "baz"])
ENUMS = [("foo", "foo", None), ("bar", "bar", None), ("baz", "baz", None), ("fun", None, RuntimeError)]


@pytest.mark.parametrize("_in,_out,_exc", ENUMS)
def test_enum(_in: str, _out: str, _exc: Optional[Type[BaseException]]) -> None:
    if _exc:
        with pytest.raises(_exc):
            ENUM(_in)
    else:
        assert ENUM(_in) == _out
