#! /usr/bin/env python

from setuptools import setup

setup(
    name="dash-google-auth-email",
    description="Dash Google Auth Email",
    long_description=open('README.md', 'rt').read().strip(),
    author="Rick Lentz", author_email='rlentz@amfam.com',
    url="https://github.com/ricklentz/dash-google-auth-email",
    license='MIT',
    package='dash_google_auth_email',
    packages=['dash_google_auth_email'],
    install_requires=[
        'dash>=0.40.0',
        'dash-core-components>=0.45.0',
        'dash-html-components>=0.15.0',
        'Flask>=1.0.2',
        'Flask-Dance>=2.0.0',
        'six>=1.13.0',
    ],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    version="0.19.99",
    zip_safe=False,
)
