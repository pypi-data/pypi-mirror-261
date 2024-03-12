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

from typing import Any, Tuple

import pytest

from omniconf.keys import join_key

# fmt: off
KEYS = [
    ("",            (None,)),
    ("foo",         ("foo",)),
    ("foo.bar",     ("foo", "bar")),
    ("foo.bar.baz", ("foo", "bar", "baz")),
    ("foo.bar",     (None, "foo", None, "bar")),
    ("foo.baz",     (None, None, None, "foo", "baz")),
    ("foo",         ("foo", None, None, "", False, 0))
]
# fmt: on


@pytest.mark.parametrize("_out,parts", KEYS)
def test_join_key(_out: str, parts: Tuple[Any, ...]) -> None:
    assert _out == join_key(*parts)
