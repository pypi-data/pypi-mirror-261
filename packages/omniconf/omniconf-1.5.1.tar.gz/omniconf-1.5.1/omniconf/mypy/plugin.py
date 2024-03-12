# Copyright (c) 2024 Cyso < development [at] cyso . com >
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
from typing import Callable, Dict, Optional, Set
from typing import Type as PythonType

from mypy.nodes import Expression
from mypy.plugin import FunctionContext, Plugin
from mypy.types import CallableType, Instance, NoneType, Overloaded, UnionType, get_proper_type
from mypy.types import Type as MypyType

OMNICONF_TYPE_REGISTRY: Dict[str, MypyType] = {}


def get_argument_by_index(ctx: FunctionContext, index: int) -> Optional[Expression]:
    args = ctx.args[index]
    if len(args) != 1:
        # Either an error or no value passed.
        return None
    return args[0]


def get_argtype_by_index(ctx: FunctionContext, index: int) -> Optional[MypyType]:
    arg_types = ctx.arg_types[index]
    if len(arg_types) != 1:
        # Either an error or no value passed.
        return None
    return arg_types[0]


def get_argument_by_name(ctx: FunctionContext, name: str) -> Optional[Expression]:
    if name not in ctx.callee_arg_names:
        return None
    index = ctx.callee_arg_names.index(name)
    return get_argument_by_index(ctx, index)


def get_argtype_by_name(ctx: FunctionContext, name: str) -> Optional[MypyType]:
    if name not in ctx.callee_arg_names:
        return None
    index = ctx.callee_arg_names.index(name)
    return get_argtype_by_index(ctx, index)


def infer_type_param(type_: Optional[MypyType]) -> Set[MypyType]:
    proper_type = get_proper_type(type_)
    types: Set[MypyType] = set()
    if isinstance(proper_type, Overloaded):
        for overloaded_type in proper_type.items:
            if isinstance(overloaded_type.ret_type, Instance):
                # TODO(LordGaav): Properly detect which overloaded type is the correct one, # noqa: TD003
                #                 return the first for now
                types.add(get_proper_type(overloaded_type.ret_type))
                break
    elif isinstance(proper_type, CallableType):
        types.add(proper_type.ret_type)
    elif isinstance(proper_type, Instance) and (ret_type := get_proper_type(proper_type.last_known_value)):
        types.add(ret_type)
    return types


class OmniconfTypePlugin(Plugin):
    def get_function_hook(self, fullname: str) -> Optional[Callable[[FunctionContext], MypyType]]:
        if fullname == "omniconf.setting.setting":
            return register_setting_type
        elif fullname == "omniconf.config.config":
            return set_config_return_type
        return None


def register_setting_type(ctx: FunctionContext) -> MypyType:
    # Bail if setting() signature does not match expected argument count
    if len(ctx.arg_types) != 7:
        return ctx.default_return_type

    # Find key of setting
    key = None
    if (
        (key_arg := get_argtype_by_name(ctx, "key") or get_argtype_by_index(ctx, 0))
        and isinstance(key_arg, Instance)
        and key_arg.last_known_value
    ):
        key = str(key_arg.last_known_value.value)

    # Bail if no key was found
    if not key:
        return ctx.default_return_type

    # Add inferred types based on _type
    return_types: Set[MypyType] = {ctx.api.named_generic_type("builtins.str", [])}
    if type_arg := get_argtype_by_name(ctx, "_type") or get_argtype_by_index(ctx, 1):
        return_types = infer_type_param(type_arg)

    # Add type of default value to inferred types if set
    has_default = False
    if default_arg := get_argtype_by_name(ctx, "default") or get_argtype_by_index(ctx, 3):
        return_types = return_types.union(infer_type_param(default_arg))
        has_default = True

    # Find if setting is marked as required
    is_required = False
    if (
        (required_arg := get_argtype_by_name(ctx, "required") or get_argtype_by_index(ctx, 2))
        and isinstance(required_arg, Instance)
        and required_arg.last_known_value
        and isinstance(required_arg.last_known_value.value, bool)
    ):
        is_required = required_arg.last_known_value.value

    # Override inferred types if type_hint is set
    if type_hint_arg := get_argtype_by_name(ctx, "type_hint") or get_argtype_by_index(ctx, 6):
        return_types = infer_type_param(type_hint_arg)

    # Add None when marked as required without a default
    if not is_required and not has_default:
        return_types.add(NoneType())

    # Merge all types as Union and register
    return_type = UnionType(list(return_types), ctx.context.line, ctx.context.column)
    OMNICONF_TYPE_REGISTRY[key] = return_type

    if "OMNICONF_MYPY_DEBUG" in os.environ:
        print(f"Registering {key} as {return_type}")

    # Return type of setting() / Setting does not change
    return ctx.default_return_type


def set_config_return_type(ctx: FunctionContext) -> MypyType:
    # Bail if config() signature does not match expected argument count
    if len(ctx.arg_types) != 2:
        return ctx.default_return_type

    # Find key of setting
    key = None
    if (
        (key_arg := get_argtype_by_name(ctx, "key") or get_argtype_by_index(ctx, 0))
        and isinstance(key_arg, Instance)
        and key_arg.last_known_value
    ):
        key = str(key_arg.last_known_value.value)

    # Return registered type if found in registry
    if key in OMNICONF_TYPE_REGISTRY:
        return OMNICONF_TYPE_REGISTRY[key]

    # Return type of config() if not found
    return ctx.default_return_type


def plugin(version: str) -> PythonType[OmniconfTypePlugin]:
    return OmniconfTypePlugin
