# PyPOP

Documentation: https://numericalalgorithmsgroup.github.io/pypop/doc.html

A python package for calculating POP metrics from application profiles, primarily designed for
literate programming using Jupyter notebooks.

PyPOP currently consumes Extrae `*.prv` traces, but is designed with a view to adding support for
additional formats.

## Requirements

  * [Extrae] (for trace creation)
  * [Paraver/Paramedir] (for trace analysis)
  * [Dimemas] *optional* (for ideal network analysis)
  * [Numpy]
  * [Pandas]

[Extrae]: https://tools.bsc.es/extrae
[Paraver/Paramedir]: https://tools.bsc.es/paraver#batchprocessing
[Dimemas]: https://tools.bsc.es/dimemas
[Numpy]: https://numpy.org/
[Pandas]: https://pandas.pydata.org/


``Paramedir`` and ``Dimemas`` must be available on the system PATH (Linux ``$PATH`` or Windows
``%PATH%`` variables) so that they can be found by PyPOP.

## Installation

Install using pip:

```bash
$ pip install [--user] git+https://github.com/numericalalgorithmsgroup/pypop
```

The optional `--user` directive instructs pip to install to the users home directory instead of the
system site package directory.

## Usage

Jupyter notebooks are intended to be the primary interface to PyPOP.  This guide uses several
example notebooks to demonstrate the core functionality of PyPOP for calculation of the POP Metrics
as well as advanced analysis of trace files.

PyPOP comes with example notebooks. These are located in the examples directory, which can be
found using the `pypop.examples` module:

```bash
$ python -m pypop.examples
/home/phil/repos/pypop/pypop/examples
```

Copy these to directory where you have read permissions, e.g.

```bash
  $ cp -vr $(python -m pypop.examples) $HOME/pypop_examples
```

These notebooks demonstrate usage of the main elements of the package.

See the [quickstart] guide and [API documentation] for more detail on usage.

[quickstart]: https://numericalalgorithmsgroup.github.io/pypop/quickstart.html
[API documentation]: https://numericalalgorithmsgroup.github.io/pypop/api/pypop.html

Copyright (c) 2019, Numerical Algorithms Group Ltd.
