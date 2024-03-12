![tests_badge](https://github.com/Jtachan/PyBaseExtension/actions/workflows/unittests.yml/badge.svg)

# Python Base Extension

The `pybase_ext` modules serve three purposes:

* Enable the use of new base classes in older Python versions. For example, `enum.StrEnum` is new in Python 3.11, but `pybase_ext` allows users on previous versions to use it too.
* Enable experimental classes not implemented in other modules. For example, `enum.TupleEnum` is not implemented in `enum`, but `pybase_ext` allows users to create enumerations where its members are tuples.
* Provide of new classes containing commonly used constant values. For example, `pybase_ext.colors.BGR` provides a wrapper to commonly used BGR color codes, like `BGR.WHITE` to use the color code `(255, 255, 255)`


## Setup

Install the package via pip.

```shell
pip install pybase-ext
```

The latest changes on develop can be installed via pip + git:
```shell
pip install git+https://github.com/Jtachan/PyBaseExtension.git@develop
```

## 📖 Documentation

Documentation can be found at the [`docs`](https://github.com/Jtachan/PyBaseExtension/blob/main/docs/index.md) folder.

WIP: Sphinx documentation for further releases.
