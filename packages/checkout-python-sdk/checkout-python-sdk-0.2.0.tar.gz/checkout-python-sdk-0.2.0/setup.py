from setuptools import setup, find_packages

VERSION = '0.2.0'

setup(
    name='checkout-python-sdk',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'requests',
        'pycryptodome',
    ],
    author='Muracia Ndungu',
    author_email='muracia.ndungu@cellulant.io',
    description='A Python package to simplify an integration to the Tingg Checkout API',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ],
)