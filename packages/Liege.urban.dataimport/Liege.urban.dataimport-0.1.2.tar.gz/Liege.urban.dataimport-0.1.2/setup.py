# -*- coding: utf-8 -*-
"""Installer for the Liege.urban.dataimport package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + "\n" + \
    read('docs', 'CONTRIBUTORS.rst') + "\n" + \
    read('docs', 'CHANGES.rst') + "\n" + \
    read('docs', 'LICENSE.rst')

setup(
    name='Liege.urban.dataimport',
    version='0.1.2',
    description="liege urban dataimport",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Zope Plone',
    author='IMIO',
    author_email='dev@imio.be',
    url='http://pypi.python.org/pypi/Liege.urban.dataimport',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['Liege', 'Liege.urban'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework',
        ],
        'develop': [
            'zest.releaser',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
