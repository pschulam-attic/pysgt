#!/usr/bin/env python2.7

from distutils.core import *
from distutils      import sysconfig

import numpy

try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

_sgt_smoother = Extension("_sgt_smoother",
                          ["sgt_smoother.i", "sgt_smoother.cpp"],
                          include_dirs = [numpy_include],
                          swig_opts=['-c++'])

setup(  name        = "Simple Good-Turing Smoothing",
        description = "gt_smooth takes an array of frequency frequencies and smooths them.",
        author      = "Peter Schulam",
        version     = "1.0",
        ext_modules = [_sgt_smoother])
