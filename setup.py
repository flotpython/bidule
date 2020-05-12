# minimal setup.py to install in develop mode

from setuptools import setup, find_packages

setup(
    name="bidule",
    packages=find_packages(),

    # see https://semver.org/
    # and https://pypi.org/project/semver/
    version="0.0.1",

    author="Thierry Parmentelat",
    author_email="thierry.parmentelat@inria.fr",
    description="A micro Python package to demo good practices",
    keywords=["Python", "package", "setup.py", "setuptools"],
    url="https://github.com/flotpython/bidule",
    license="Creative Commons BY-CC-ND 4.0",
)
