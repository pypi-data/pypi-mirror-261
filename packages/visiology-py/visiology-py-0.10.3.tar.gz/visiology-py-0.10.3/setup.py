#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="visiology-py",
    packages=["visiology_py", "i2ls"],
    version="0.10.3",
    description=(
        "High level wrappers for Visiology APIs: "
        "Smart Forms, ViQube and ViQube admin"
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/polymedia-orv/orv/visiology-py",
    author="Denis <codingjerk> Gruzdev",
    author_email="codingjerk@gmail.com",
    license="MIT",

    install_requires=[
        "funcy<2",
        "requests>=2.24.0,<3"
    ],
    setup_requires=[
        "funcy<2",
        "hypothesis<7",
        "mypy<2",
        "pycodestyle<3",
        "pytest-cov<5",
        "pytest-runner<7",
        "pytest<9",
        "radon<7",
        "requests>=2.24.0,<3",
        "types-requests<3",
        "wheel",
    ],
    tests_require=[
        "funcy<2",
        "hypothesis<7",
        "mypy<2",
        "pycodestyle<3",
        "pytest-cov<5",
        "pytest-runner<7",
        "pytest<9",
        "radon<7",
        "requests>=2.24.0,<3",
        "types-requests<3",
        "wheel",
    ],
    test_suite="tests",
)
