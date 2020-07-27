import os
from setuptools import setup, Extension
import pybind11

setup(
    name="foo",
    ext_modules=[
        Extension(
            "foo", ["foo.cpp"],
            include_dirs=[pybind11.get_include()],
            extra_compile_args=[{"posix": "-std=c++1z", "nt": "/std:c++17"}[os.name]]
        ),
    ],
)
