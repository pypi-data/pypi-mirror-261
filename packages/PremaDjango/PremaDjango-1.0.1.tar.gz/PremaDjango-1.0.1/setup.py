"""PremaDjango setup.py."""

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PremaDjango",
    version="1.0.1",
    packages=find_packages(),
    install_requires=["Django", "setuptools_scm"],
    author="Premanath",
    author_email="talamarlapremanath143@gmail.com",
    description="configurations and settings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prema1432/premadjango/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    license="MIT",
)
