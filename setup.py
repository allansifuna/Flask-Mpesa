#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='Flask-Mpesa',
    version='1.2.8',
    url='https://github.com/allansifuna/flask-mpesa',
    license='BSD',
    author='Allan Namasaka Sifuna',
    author_email='allansifuna324@gmail.com',
    description='A Safaricom\'s DarajaAPI2.0 Package for Flask Applications.',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
