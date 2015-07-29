# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='simplefb',
    version='0.1.0',
    description='A simple facebook graph api',
    url='https://github.com/fm100/simplefb',
    author='Freddie Park',
    author_email='sorelove@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='facebook graph api',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
