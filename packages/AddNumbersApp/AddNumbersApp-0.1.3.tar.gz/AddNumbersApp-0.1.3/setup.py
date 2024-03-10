from setuptools import setup, find_packages

setup(
    name='AddNumbersApp',
    version='0.1.3',  # Remember to increment the version if re-uploading
    packages=find_packages(),
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
