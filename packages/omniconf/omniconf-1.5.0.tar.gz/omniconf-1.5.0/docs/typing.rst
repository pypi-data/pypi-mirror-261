.. _type-annotations:

Type annotations
================

omniconf version 1.5.0 added type annotations, and also an experimental mypy plugin for dynamic type annotations
of the return values of :func:`config` by parsing the `_type` and `type_hint` parameters of :func:`setting`.

Without enabling the plugin, the return type of configuration values is `Optional[Any]` .

The mypy plugin has a few prerequisites at this point:

* A mapping is made between :func:`setting` key and its `_type`. This probably only works properly when the
  key is defined as a literal.
* The plugin only works when using the :func:`config` and :func:`setting` functions. Settings added directly
  on :class:`SettingRegistry` and read directly from :class:`ConfigRegistry` will be **not** found or
  properly annotated.
* There is no support for multiple registries, only the default registries are supported.

Despite these limits, if your current worklow only consists on using :func:`setting`, :func:`omniconf_load`
and :func:`config`, you're probably fine.

Enabling the plugin
-------------------

Simply add the plugin to your mypy configuration, for instance using `pyproject.toml`::

   [tool.mypy]
   ...
   plugins = [
     "omniconf.mypy.plugin"
   ]

Annotating settings
-------------------

First, an example script.

.. code-block:: python

   from omniconf import setting, config, omniconf_load
   from omniconf.types import separator_sequence
   from typing import Dict

   class Foo:
      def __init__(self, value: str) -> None:
        self.value = value

   setting("app.optionalstr")
   setting("app.requiredstr",               required=True)
   setting("app.optionalint",   _type=int)
   setting("app.requiredbool",  _type=bool, required=True)
   setting("app.simpledict",    _type=dict, required=True)
   setting("app.annotateddict", _type=dict, required=True, type_hint=Dict[str, Foo])
   setting("app.object",        _type=Foo,  required=True)
   setting("app.sequence",      _type=separator_sequence(","), required=True)
   omniconf_load()

For the simple types, this will behave as expected. Note that the mypy plugin will always annotate using
Unions, to handle the `required` property.

.. code-block:: python

   config("app.optionalstr")   # Union[builtins.str, None]
   config("app.requiredstr")   # Union[builtins.str]
   config("app.optionalint")   # Union[builtins.int, None]
   config("app.requiredbool")  # Union[builtins.bool]
   config("app.object")        # Union[test.Foo]
   config("app.sequence")      # Union[typing.Sequence[builtins.str]]

The `dict` case is a bit more tricky, because by default this will result in a `dict[_KT, _VT]`. This will
cause trouble because this signature disallows indexing and causes mypy to show this message::

   error: Invalid index type "str" for "dict[_KT, _VT]"; expected type "_KT"  [index]
   value["a"]
         ^~~

To work around this, you can set the exact type using `type_hint`, which will be used as-is instead of the
inferred type from `_type`. You can use this in any case where the inferred type is giving you trouble.

.. code-block:: python

   setting("app.simpledict", _type=dict, required=True)
   setting("app.annotateddict", _type=dict, required=True, type_hint=Dict[str, Foo])

   config("simpledict")        # Union[builtins.dict[_KT`1, _VT`2]]
   config("annotateddict")     # Union[builtins.dict[builtins.str, test.Foo]]
