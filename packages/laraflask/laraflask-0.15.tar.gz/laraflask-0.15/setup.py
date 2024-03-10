# laraflask/setup.py

import os
from setuptools import setup, find_packages

def scan_dir_files_and_return_full_path(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

# Get the path to the README file relative to the setup.py script
readme_path = os.path.join(os.path.dirname(__file__), 'Readme.md')

# Check if the README file exists before trying to read it
if os.path.exists(readme_path):
    long_description = open(readme_path).read()
else:
    long_description = ''

setup(
    name='laraflask',
    version='0.15', # don't forget to change the version number
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'laraflask': [os.path.relpath(path, 'src') for path in scan_dir_files_and_return_full_path('src')]},
    py_modules={'laraflask'},
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
    ],
    long_description=long_description,
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

# Create a Virtual Environment:
# python3 -m venv venv

# Activate the Virtual Environment:
# source venv/bin/activate

# Deactivate the Virtual Environment:
# deactivate

# Install necessary build tools:
# $ pip install wheel twine build setuptools

# Build the Distribution Package:
# $ python setup.py sdist bdist_wheel
# $ python -m build

# Upload the Distribution Package to PyPI:
# $ twine upload dist/*
# $ twine upload --skip-existing dist/*

# Install the Distribution Package Locally:
# $ pip install dist/laraflask-0.1.tar.gz

# Uninstall the Distribution Package:
# $ pip uninstall laraflask
