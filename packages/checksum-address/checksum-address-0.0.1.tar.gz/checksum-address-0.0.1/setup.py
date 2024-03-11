from setuptools import setup, find_packages

setup(
    name="checksum-address",
    version="0.0.1",
    packages=find_packages(),
    keywords=['ethereum', 'web3'],
    install_requires=['eth_utils'],
)