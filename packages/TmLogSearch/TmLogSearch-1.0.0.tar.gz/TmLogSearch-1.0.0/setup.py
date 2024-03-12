# setup.py

from setuptools import setup, find_packages

setup(
    name='TmLogSearch',
    version='1.0.0',  # Increment the version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'paramiko',
        'flask-cors'
    ],
    entry_points={
        'console_scripts': [
            'tmsearch=tmlogsearch.app:main',  # Adjusted to new package name
        ],
    },
)
