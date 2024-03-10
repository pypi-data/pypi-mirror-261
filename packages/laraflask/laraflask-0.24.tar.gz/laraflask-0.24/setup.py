# laraflask/setup.py

import os
from setuptools import setup, find_packages

# Get the path to the README file relative to the setup.py script
readme_path = os.path.join(os.path.dirname(__file__), 'Readme.md')

# Check if the README file exists before trying to read it
if os.path.exists(readme_path):
    long_description = open(readme_path).read()
else:
    long_description = ''

setup(
    name='laraflask',
    version='0.24', # don't forget to change the version number
    packages=find_packages(include=['laraflask', 'laraflask.*']),
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'python-dotenv'
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
    entry_points={
        "console_scripts": ["project_name = project_name.__main__:main"]
    },
)

# Create a Virtual Environment:
# python3 -m venv venv

# Activate the Virtual Environment:
# source venv_development/bin/activate

# Deactivate the Virtual Environment:
# deactivate

# Install necessary build tools:
# $ pip install wheel twine build setuptools

# Build the Distribution Package:
# $ python setup.py sdist
# $ python3 setup.py sdist bdist_wheel
# $ python3 -m build

# Upload the Distribution Package to PyPI:
# $ twine upload dist/*

# Install the Distribution Package Locally:
# $ pip install dist/laraflask-0.21.tar.gz

# Uninstall the Distribution Package:
# $ pip uninstall laraflask
