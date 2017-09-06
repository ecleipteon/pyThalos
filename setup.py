from setuptools import setup, find_packages

import pyThalos

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyThalos',
    version='0.1.0',
    description='Python client for Thalos server',
    long_description=readme,
    author='Luca Maria Castiglione',
    author_email='luc.castiglione@studenti.unina.it',
    url='https://github.com/ecleipteon/pyThalos',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
