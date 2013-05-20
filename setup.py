#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='BuSys',
    version='1.0',
    packages=find_packages(),
    package_dir={'busys': 'busys'},
    include_package_data=True,
    license='BSD License',
    long_description=README,
    url='https://github.com/rtbustamantec/busys',
    author='Raul Bustamante Cruzado',
    author_email='rtbustamantec@gmail.com',
    install_requires=[
        'Django==1.5.1',
        'Fabric==1.6.0',
        'South==0.7.6',
        'django-grappelli==2.4.4',
        'wsgiref==0.1.2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Bug Tracking',
    ],
)



