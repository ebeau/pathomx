#!/usr/bin/env python
# coding=utf-8
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages
import py2app

# Build the .app file
setup(

    name='metapath',
    version='1.0.0',
    author='Martin Fitzpatrick',
    author_email='martin.fitzpatrick@gmail.com',
    url='https://github.com/mfitzp/metapath',
    download_url='http://github.com/mfitzp/metapath',
    description='Metabolic pathway visualisation and analysis.',
    long_description='MetaPath is a tool for the analysis of metabolic pathway and \
        associated visualisation of experimental data. Built on the MetaCyc database it \
        provides an interactive map in which multiple pathways can be simultaneously \
        visualised. Multiple annotations from the MetaCyc database are available including \
        synonyms, associated reactions and pathways and database unification links.',

    packages = find_packages(),
    include_package_data = True,
    package_data = {
        '': ['*.txt', '*.rst', '*.md'],
        'metapath': ['static/*', 'examples/*', 'db/*', 'identities/*', 'html/*','icons/*'],
    },
    exclude_package_data = { '': ['README.txt'] },

    entry_points = {
        'console_scripts': [
            'metapath = metapath.metapath:main',
        ],
        'gui_scripts': [
            'metapath-gui = metapath.metapath-gui:main',
        ]
    },

    install_requires = ['PySide>0.0','numpy>0.0'],

    keywords='bioinformatics metabolomics research analysis science',
    license='GPL',
    classifiers=['Development Status :: 4 - Beta',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 2',
               'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
               'License :: OSI Approved :: GNU Affero General Public License v3',
               'Topic :: Scientific/Engineering :: Bio-Informatics',
               'Topic :: Education',
               'Intended Audience :: Science/Research',
               'Intended Audience :: Education',
              ],

    options=dict(
        py2app=dict(
            iconfile='static/icon.icns',
            packages=['PySide','numpy'],
#            includes=['xml.etree.ElementTree'],
            excludes=['matplotlib', 'scipy','_xmlplus'],
            #'_ssl', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect',],
            site_packages=True,
            optimize=2,
            resources=['static', 'examples', 'db', 'identities', 'html','icons'],
            plist=dict(
                CFBundleName               = "MetaPath",
                CFBundleShortVersionString = "1.0.0",     # must be in X.X.X format
                CFBundleGetInfoString      = "MetaPath 1.0.0",
                CFBundleExecutable         = "MetaPath",
                CFBundleIdentifier         = "com.ables.metapath",
            ),
        ),
    ),
    app=[ 'metapath-qt.py' ],

    )