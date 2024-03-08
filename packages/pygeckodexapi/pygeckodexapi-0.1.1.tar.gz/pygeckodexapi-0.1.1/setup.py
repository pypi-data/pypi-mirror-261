from setuptools import setup, find_packages

setup(
    name='pygeckodexapi',
    version='0.1.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/labfunny/jetton-price-api',
    license='MIT',
    author='Max',
    description='Unofficial SDK for working with the GeckoTerminal API',
    classifiers = ['Programming Language :: Python :: 3.6']
)