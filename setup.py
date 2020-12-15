#!/usr/bin/env python
# coding=utf-8

from setuptools import find_packages, setup
from LibcSearcher3 import VERSION


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='LibcSearcher3',
    version=VERSION,
    url='https://github.com/Ro0tk1t/LibcSearcher3.git',
    description='libc offset database searcher',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ro0tk1t',
    author_email='R00tk1t@qq.com',
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'libcsearch = LibcSearcher3.main:main',
        ]
    },

    install_requires=[],
)
