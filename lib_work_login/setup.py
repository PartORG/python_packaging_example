# -*- coding: utf-8 -*-

"""This module sets up the package for the lib_work_login"""

from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as fh:
#   long_description = fh.read()

setup(
    name="lib_work_login",
    author="Ievgen Perederieiev",
    author_email="test_ievgen@gmail.com",
    maintainer="Ievgen Perederieiev",
    maintainer_email="maintainer_test@gmail.com",
    version="0.1.2",
    url="https://github.com/PartORG/",
    download_url="https://github.com/PartORG/",
    keywords=['Furuness', 'Login', 'login', 'terminal'],
    license="BSD",
    description="Logs you into work",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    project_urls={
        "Git URL": "https://github.com/PartORG/"
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pynput==1.7.6",
        "pytest",
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD Licence',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
    # entry_points={
    #     'console_scripts': [
    #         'login = lib_work_login.__main__:main',
    #         'configure = lib_work_login.__main__:configure'
    #     ],
    # },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
