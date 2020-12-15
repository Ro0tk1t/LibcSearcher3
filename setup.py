#!/usr/bin/env python
# coding=utf-8

from setuptools import find_packages, setup
from LibcSearcher3 import VERSION


setup(
    name='LibcSearcher3',
    version=VERSION,
    url='https://github.com/Ro0tk1t/LibcSearcher3.git',
    description='libc offset database searcher',
    author='Ro0tk1t',
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'libcsearch = LibcSearcher3:main',
        ]
    },

    install_requires=[],
)
