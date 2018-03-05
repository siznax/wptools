#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()


setup(
    name='wptools',
    version='0.4.11',
    description='Wikipedia tools (for Humans)',
    long_description=readme + '\n\n' + history,
    url='https://github.com/siznax/wptools/',
    license='MIT',
    author='Steve @siznax',
    author_email='steve@siznax.net',
    py_modules=['wptools'],
    packages=find_packages(exclude=['tests']),
    test_suite='tests.test_basic',
    install_requires=['certifi', 'html2text', 'lxml', 'pycurl'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['wptool=scripts.wptool:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
