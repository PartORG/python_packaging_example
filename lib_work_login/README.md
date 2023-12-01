# lib_work_login
A simple package that executes provided bash commands from .work_login.conf file.

## Purpose of Project
This project illustrates a packaging example with Python and setuptools.

Project has a good setup.py file content. It will be useful for other projects to be used as an example.

## Useful commands for packaging
python3 setup.py develop - will install your package.

python3 setup.py bdist_wheel - create package with wheel extension.

## Upload to Pypi
twine upload dist/* --skip-existing