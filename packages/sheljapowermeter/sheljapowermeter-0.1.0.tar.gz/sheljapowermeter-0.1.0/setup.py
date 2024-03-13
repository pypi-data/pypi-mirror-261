from setuptools import setup, find_packages

setup(
    name='sheljapowermeter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyvisa',
        # Add your dependencies here if any
    ],
)