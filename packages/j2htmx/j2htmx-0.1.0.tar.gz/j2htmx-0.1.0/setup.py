import pathlib

from setuptools import find_packages
from setuptools import setup


def find_required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_version(filename='j2htmx/version'):
    return open(filename, "r").read().strip()


HERE = pathlib.Path(__file__).parent
README = open("README.md").read()
setup(
    name="j2htmx",
    version=get_version(),
    description="jinja2 template for light-weight htmx page rendering",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yuriy Sagitov",
    author_email="pro100.ko10ok@gmail.com",
    python_requires=">=3.10.0",
    url="https://github.com/ko10ok/j2htmx",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=find_required(),
    entry_points={},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={
        'j2htmx': ['version'],
    },
)
