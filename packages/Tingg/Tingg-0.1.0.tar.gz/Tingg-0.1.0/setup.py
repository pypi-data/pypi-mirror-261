from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name='Tingg',
    version=VERSION,
    readme = "README.rst",
    license = "LICENSE.rst",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pycryptodome',
    ],
    authors=[
        {"name": "Cellulant", "email": "platforms@cellulant.io"}, 
        {"name": "Howard Mnengwa", "email": "howard@mnengwa.com"},
        {"name": "Muracia Ndungu", "email": "muracia.ndungu@cellulant.io"}
    ],
    description='A package to help you streamline your integration to the Tingg Checkout API',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ],
)