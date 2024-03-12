.. _supported-backends:

Supported backends
==================

The following backends are supported as of version |version|:

.. contents :: :local:

generic backend interface
-------------------------

All backends implement the same interface, which allows for easy addition of new (or external backends).

.. autoclass :: omniconf.backends.generic.ConfigBackend
   :members:

dict backend interface
----------------------

For backends that basically work like a dictionary lookup, another generic interface is added that only
requires the implementation of passing the loaded config using the `conf` init parameter and defining the
needed autoconfiguration settings.

.. autoclass :: omniconf.backends.generic.DictConfigBackend
   :members:

commandline arguments
---------------------

Command line arguments are implemented using :mod:`argparse`. This backend is enabled by default.

.. autoclass :: omniconf.backends.argparse.ArgparseBackend
   :members:


environment variables
---------------------

Environments are read from :any:`os.environ`. This backend is enabled by default.

.. autoclass :: omniconf.backends.env.EnvBackend
   :members:


ConfigObj files
---------------

Files in ConfigObj format are supported. This backend is only enabled if `omniconf.configobj.filename` is specified
during setup.

.. autoclass :: omniconf.backends.configobj.ConfigObjBackend
   :members:


JSON files
----------

Files in JSON format are supported. This backend is only enabled if `omniconf.json.filename` is specified during setup.

.. autoclass :: omniconf.backends.json.JsonBackend
   :members:

TOML files
----------

Files in TOML format are supported. This backend is only enabled if `omniconf.toml.filename` is specified during setup.

.. autoclass :: omniconf.backends.toml.TomlBackend
   :members:

YAML files
----------

Files in YAML format are supported. This backend is only enabled if `omniconf.yaml.filename` is specified during setup.
All YAML documents in the file are consumed.

.. autoclass :: omniconf.backends.yaml.YamlBackend
   :members:
