# Copyright (C) 2023 twyleg
import versioneer
from pathlib import Path
from setuptools import find_packages, setup


def read(fname):
    return open(Path(__file__).parent / fname).read()


setup(
    name="random_number_provider",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description="Random numbers as a service",
    license="GPL 3.0",
    keywords="random numbers as a service",
    url="https://github.com/twyleg/",
    packages=find_packages(),
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=[
        "xmlschema~=2.3.1",
        "multimethod~=1.10",
        "gunicorn~=21.2.0",
        "flask~=2.3.3",
        "werkzeug~=2.3.7",
    ],
    entry_points={
        "console_scripts": [
            "random_number_provider = random_number_provider.app:start",
        ]
    },
)