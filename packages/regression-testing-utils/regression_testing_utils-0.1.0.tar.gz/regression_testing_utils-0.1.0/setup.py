#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    "Rich",
    "PyYAML",
    "xlsxwriter",
]

test_requirements = [ ]

setup(
    author="Jaideep Sundaram",
    author_email='jai.python3@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Collection of Python tools to support execution of regression testing.",
    entry_points={
        'console_scripts': [
            'make-regression-testing-utils=regression_testing_utils.make_shell_scripts_and_aliases:main',
            'regression-testing-runner=regression_testing_utils.runner:main',
            'regression-testing-compare-tsv=regression_testing_utils.compare_tsv_files:main',
            'regression-testing-compare-csv=regression_testing_utils.compare_csv_files:main',
            'regression-testing-compare=regression_testing_utils.compare_files:main',
            'regression-testing-config-checker=regression_testing_utils.config_checker:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='regression_testing_utils',
    name='regression_testing_utils',
    packages=find_packages(include=['regression_testing_utils', 'regression_testing_utils.*']),
    package_data={"regression_testing_utils": ["conf/config.yaml"]},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jai-python3/regression-testing-utils',
    version='0.1.0',
    zip_safe=False,
)
