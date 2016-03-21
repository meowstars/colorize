#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='Colorize',
    description='Palette manager for term apps.',
    author="Yann 'Meow' Bordenave",
    author_email='meow@meo.wf',
    version=open('VERSION').read(),
    install_requires=['PyYAML', 'jinja2', 'pillow'],
    packages=[],
    license='zlib',
    long_description=open('README').read(),
    scripts=[
        'bin/colorize',
    ],
)
