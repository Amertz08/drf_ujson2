#!/usr/bin/env python

from setuptools import setup, find_packages

from drf_ujson import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version=".".join([str(i) for i in __version__]),
    python_requires=">=3.6",
    description="Django Rest Framework UJSON Renderer",
    keywords="django,djangorestframework,ujson",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson2",
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "ujson>=1.35,<2", "djangorestframework"],
    extras_require={
        "dev": ["pytest", "pytest-django", "pytest-runner", "pytest-cov", "pytest-mock"]
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
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
