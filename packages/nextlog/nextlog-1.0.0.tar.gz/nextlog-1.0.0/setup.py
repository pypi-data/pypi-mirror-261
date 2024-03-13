from setuptools import setup, find_packages

description = 'A python logging library with async. dispatch to monitoring services like loki'
long_description = 'Documentation coming soon.'

setup(
    name='nextlog',
    version='1.0.0',
    description=description,
    long_description=long_description,
    author='Sourav',
    author_email='imsrv2k@gmail.com',
    packages=find_packages(),
    install_requires=[
        # list of dependencies
        'requests',
        'redis'
    ],
)