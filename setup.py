from setuptools import setup, find_packages

TOGGLPY_VERSION = '0.0.2'

setup (
    name='toggl',
    version=TOGGLPY_VERSION,
    packages=find_packages(),
    include_package_data = True,
    description='TogglPy forked from matthewdowney/TogglPy'
)
