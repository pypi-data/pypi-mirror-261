# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages
from frunner import __version__, __description__

try:
    long_description = open(os.path.join('', "README.md"), encoding='utf-8').read()
except IOError:
    long_description = ""

setup(
    name="frunner",
    version=__version__,
    description=__description__,
    author="冯建伟",
    author_email="894948041@qq.com",
    url="https://github.com",
    platforms="Android,IOS,Web,Api",
    packages=find_packages(),
    long_description=long_description,
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
    include_package_data=True,
    package_data={
        r'': ['*.yml'],
    },
    install_requires=[
        'tidevice==0.6.1',
        'facebook-wda==1.4.6',
        'uiautomator2==2.16.13',
        'selenium==4.1.3',
        'webdriver-manager==3.5.2',
        'pytest==6.2.5',
        'pytest-rerunfailures==10.2',
        'pytest-ordering==0.6',
        'pytest-xdist==2.5.0',
        'pytest-dependency==0.5.1',
        'allure-pytest==2.9.45',
        'jmespath==0.9.5',
        'python-dateutil==2.8.2',
        'PyYAML==6.0',
        'baseImage==2.1.1',
        'pydantic==1.8.2'
    ],
    extras_require={
        "excel": ['pandas==1.3.4', 'openpyxl==3.0.9', 'XlsxWriter==3.0.2'],
        "jira": ['jira==3.1.1'],
        "mysql": ['PyMySQL==0.10.1'],
        "mongo": ['pymongo==4.0.1'],
        "encrypt": ['pycryptodome==3.14.1'],
        "win": ['PyAutoGUI==0.9.53'],
        "mac": ['pyobjc==8.5', 'pyobjc-core==8.5', 'PyAutoGUI==0.9.53']
    },
    entry_points={
        'console_scripts': [
            'frun = frunner.cli:main',
            'frunner = frunner.cli:main'
        ]
    },
)
