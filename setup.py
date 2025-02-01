#!/usr/bin/env python

from setuptools import setup, find_packages

from drf_ujson import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version=".".join([str(i) for i in __version__]),
    python_requires=">=3.10",
    description="Django Rest Framework UJSON Renderer",
    keywords="django,djangorestframework,ujson",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf_ujson2",
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "ujson>=4.2.0", "djangorestframework"],
    extras_require={"dev": ["pytest", "pytest-django", "pytest-cov", "pytest-mock"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
