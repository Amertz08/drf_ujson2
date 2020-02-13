#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version="1.4.1",
    python_requires=">=3.6",
    description="Django Rest Framework UJSON Renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson2",
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "ujson>=1.35", "djangorestframework"],
    extras_require={
        "dev": [
            "pytest",
            "pytest-django",
            "pytest-runner",
            "pytest-cov",
            "pytest-mock",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
    ],
)
