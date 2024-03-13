from setuptools import setup, find_packages

setup(
    name='mp_basic_calculator',
    version='0.4',
    packages=find_packages(),
    install_requires=['pytest'],
    long_description=open('README.md').read()
)
