#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:04:43 2021.

@author: fabulous
"""


from codecs import open

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


SOLVERS = [
    "gurobipy",
    "highspy",
    "cplex",
    "mosek",
    "mindoptpy",
    "coptpy",
    "xpress; platform_system != 'Darwin' and python_version < '3.11'",
    "pyscipopt; platform_system != 'Darwin'",
]


setup(
    name="linopy",
    author="Fabian Hofmann",
    author_email="hofmann@fias.uni-frankfurt.de",
    description="Linear optimization with N-D labeled arrays in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyPSA/linopy",
    license="MIT",
    packages=find_packages(exclude=["doc", "test"]),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "scipy",
        "bottleneck",
        "toolz",
        "numexpr",
        "xarray>=2023.9.0",
        "dask>=0.18.0",
        "tqdm",
        "deprecation",
    ],
    extras_require={
        "docs": [
            "ipython",
            "numpydoc",
            "sphinx",
            "sphinx_rtd_theme",
            "sphinx_book_theme",
            "nbsphinx",
            "nbsphinx-link",
            "gurobipy",
            "ipykernel",
            "matplotlib",
        ],
        "dev": [
            "pytest",
            "pytest-cov",
            "netcdf4",
            "pre-commit",
            "paramiko",
            "gurobipy",
            "highspy",
        ],
        "solvers": SOLVERS,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
