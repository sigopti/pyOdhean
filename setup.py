#!/usr/bin/env python3
"""PyODHeaN

Optimization of District Heating Networks.
"""

from setuptools import setup, find_packages

# Get the long description from the README file
with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyodhean",
    version="1.0.0",
    description="Optimization of District Heating Networks",
    long_description=long_description,
    url="https://github.com/sigopti/pyodhean",
    author="Nobatek/INEF4",
    author_email="jlafrechoux@nobatek.com",
    license="GPLv3+",
    keywords=[
        "District",
        "Heating",
        "Network",
        "Optimization",
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pyomo>=6,<7",
    ],
    packages=find_packages(exclude=["tests*"]),
)
