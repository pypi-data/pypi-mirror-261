# setup.py
from setuptools import setup

setup(
    name='AddNumbersApp',
    version='0.1.1',
    packages=['test'],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'add-numbers=test.app:main',
        ],
    },
)
