# -*- coding:utf-8 -*-

from exmail import __VERSION__

sdict = {
    'name': 'exmail-sdk',
    'version': __VERSION__,
    'keywords': 'tencent, qq, exmail, exmail-sdk, SDK',
    'packages': ['exmail'],
    'zip_safe': False,
    'description': 'Tencent Exmail SDK for Python',
    'long_description': 'Tencent Exmail SDK for Python',
    'url': 'https://github.com/ni-ning/exmail-sdk',
    'author': 'ni-ning',
    'author_email': 'nining1314@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if __name__ == '__main__':
    setup(**sdict)
