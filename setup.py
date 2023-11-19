import os.path

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(

    keywords="apk dex axml",

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        "pyelftools",
        "cigam",
        "xmltodict",
    ],
)
