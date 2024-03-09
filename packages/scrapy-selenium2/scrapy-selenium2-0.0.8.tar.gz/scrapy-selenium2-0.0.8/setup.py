"""This module contains the packaging routine for the pybook package"""

import setuptools

# from scrapy_selenium import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="scrapy-selenium2",
    version="0.0.8",
    license="BSD",
    description="Scrapy with selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Clément Denoix",
    author_email="clement.denoix@gmail.com",
    url="https://github.com/clemfromspace/scrapy-selenium",
    packages=["scrapy_selenium"],
    python_requires=">=3.8",
    install_requires=[
        "scrapy>=2.0,!=2.4.0",
        "selenium>=4.18.1",
    ],
)
