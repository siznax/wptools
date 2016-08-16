#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()


setup(
    name='wptools',
    version='0.0.4',
    description='Get Wikipedia article lead (summary), infobox, and more via MediaWiki API',
    long_description=readme + '\n\n' + history,
    url='https://github.com/siznax/wptools/',
    license='MIT',
    author='Steve @siznax',
    author_email='steve@siznax.net',
    py_modules=['wptools'],
    packages=find_packages(exclude=['tests']),
    install_requires=['html5lib', 'lxml', 'pycurl', 'requests'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wp_html = scripts.html:main',
            'wp_image = scripts.image:main',
            'wp_infobox = scripts.infobox:main',
            'wp_lead = scripts.lead:main',
            'wp_parsetree = scripts.parsetree:main',
            'wp_text = scripts.text:main',
            'wp_wikitext = scripts.wikitext:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
