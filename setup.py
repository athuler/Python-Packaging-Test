from setuptools import setup, find_packages
from pythonPackagingTest import __version__

with open("README.md", 'r') as f:
	long_description = f.read()

setup(
	name='Python Packaging Test',
	version=__version__,
	description='A test of the packaging',
	long_description=long_description,
	author='Andrei Thuler',
	author_email='info@andreithuler.com',
	url="https://github.com/athuler/Python-Packaging-Test",
	packages=find_packages(),
	py_modules=find_packages(),
	install_requires=[
		"wheel",
	],
	
)