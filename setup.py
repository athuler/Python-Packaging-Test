from setuptools import setup

with open("README.md", 'r') as f:
	long_description = f.read()

setup(
	name='Python Packaging Test',
	version='0.1.4',
	description='A test of the packaging',
	long_description=long_description,
	author='Andrei Thuler',
	author_email='info@andreithuler.com',
	url="https://github.com/athuler/Python-Packaging-Test",
	packages=['pythonPackagingTest'],
	install_requires=["wheel"],
)