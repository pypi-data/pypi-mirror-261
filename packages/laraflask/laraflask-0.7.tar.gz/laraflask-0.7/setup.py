# laraflask/setup.py

from setuptools import setup, find_packages

import glob

# Get a list of all files in the current directory
all_files = glob.glob('*')

setup(
    name='laraflask',
    version='0.7', # don't forget to change the version number
    packages=find_packages(),
    data_files=[('laraflask', all_files)], 
    install_requires=[
        'flask',
        'requests',
    ],
    long_description=open('Readme.md').read(),
    long_description_content_type='text/markdown',
    author='Teguh Rijanandi',
    author_email='teguhrijanandi02@gmail.com',
    description='A flask package for Laraflask',
    license='MIT',
    keywords='laraflask flask package',
    url='https://github.com/laraflask/laraflask',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

# Build the Distribution Package:
# $ python setup.py sdist
# $ python setup.py sdist bdist_wheel
# $ python -m build

# Upload the Distribution Package to PyPI:
# $ twine upload dist/*

# Install the Distribution Package Locally:
# $ pip install dist/laraflask-0.1.tar.gz

# Uninstall the Distribution Package:
# $ pip uninstall laraflask
