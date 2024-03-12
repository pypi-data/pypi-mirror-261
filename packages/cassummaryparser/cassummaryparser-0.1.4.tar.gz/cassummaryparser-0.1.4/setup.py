from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name='cassummaryparser',
    packages=find_packages(include=['cassummaryparser']),
    version='0.1.4',
    description='Cas summary parser',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Nethish Rajendran',
    author_email='nethish259@gmail.com',
    install_requires=['tabula-py==2.9.0', 'jpype1==1.5.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.0.2'],
    test_suite='tests',
)
