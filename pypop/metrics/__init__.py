#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause-Clear
# Copyright (c) 2019, The Numerical Algorithms Group, Ltd. All rights reserved.

"""\
Metric Calculator Classes
-------------------------

PyPOP provides calculator classes for generating the POP Metrics for different
application types.

Currently PyPOP supports calculation of the following Metric types:

.. autosummary::
    :nosignatures:

    MPI_Metrics
    MPI_OpenMP_Metrics
    OpenMP_Metrics
"""

from .mpi import MPI_Metrics
from .hybrid import MPI_OpenMP_Metrics, MPI_OpenMP_Multiplicative_Metrics
from .openmp import OpenMP_Metrics

__all__ = ['MPI_Metrics',
           'MPI_OpenMP_Metrics',
           'MPI_OpenMP_Multiplicative_Metrics',
           'OpenMP_Metrics']
