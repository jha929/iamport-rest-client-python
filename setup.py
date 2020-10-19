# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import codecs
install_requires = ['requests', 'protobuf']


def readme():
    with codecs.open('README.rst', encoding='utf-8') as f:
        return f.read()


setup(
    name='iamport-rest-client',
    version='0.8.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    author='PerhapsSPY',
    author_email='perhapsspy@gmail.com',
    url='https://github.com/iamport/iamport-rest-client-python',
    description="REST client for I'mport;(http://www.iamport.kr)",
    long_description=readme(),
    license='MIT',
    zip_safe=False,
    data_files=[
        (
            'shared/typehints/python2.7',
            ['iamport/client.pyi'],
        ),
        (
            'shared/typehints/python3.5',
            ['iamport/client.pyi'],
        ),
        (
            'shared/typehints/python3.6',
            ['iamport/client.pyi'],
        ),
        (
            'shared/typehints/python3.7',
            ['iamport/client.pyi'],
        ),
        (
            'shared/typehints/python3.8',
            ['iamport/client.pyi'],
        ),
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
