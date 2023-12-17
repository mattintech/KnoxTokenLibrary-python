from setuptools import setup, find_packages

setup(
    name='pyktl',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
        'pyjwt[crypto]'
    ],
)
