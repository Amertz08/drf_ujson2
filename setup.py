#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version="1.4.1",
    python_requires=">=3.4",
    description="Django Rest Framework UJSON Renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson2",
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "ujson>=1.35", "djangorestframework"],
    extras_require={"dev": ["pytest", "pytest-runner", "pytest-cov", "pytest-mock"]},
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
