[![PyPI - License](https://img.shields.io/pypi/l/autotwin_gmglib)](https://github.com/AutotwinEU/graph-model-gen/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/autotwin_gmglib)](https://www.python.org/downloads/)
[![PyPI - Version](https://img.shields.io/pypi/v/autotwin_gmglib)](https://pypi.org/project/autotwin_gmglib/)

# Graph Model Generation (GMG) Library for Auto-Twin

The graph model generation (GMG) library provides a set of utility functions to
import an event log from a system knowledge graph, generate a graph model from
the event log and export the graph model to the system knowledge graph (SKG).

## Installation
To facilitate installation, the GMG library is released as a Python module,
`autotwin_gmglib`, in the
[PyPI repository](https://pypi.org/project/autotwin_gmglib/).
`autotwin_gmglib` depends on `pygraphviz`. This dependency however cannot be
resolved automatically by `pip`. As a preparation, you need to install
`pygraphviz` manually, following instructions provided on
[this page](https://pygraphviz.github.io/documentation/stable/install.html).
Whenever `pygraphviz` is available, the latest version of `autotwin_gmglib` can
be easily installed with `pip`.

    pip install autotwin_gmglib

## Getting Started
This repository includes 
