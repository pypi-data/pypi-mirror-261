# setup.py

from setuptools import setup, find_packages

setup(
    name='AddNumbersApp',
    version='0.1.5',  # Increment the version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'add-numbers=addnumbersapp.app:main',  # Adjusted to new package name
        ],
    },
)
