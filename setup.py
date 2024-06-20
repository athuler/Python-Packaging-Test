from setuptools import setup, find_packages

with open("README.md", 'r') as f:
	long_description = f.read()

setup(
	name='Python Packaging Test',
	version='0.1.6.1',
	description='A test of the packaging',
	long_description=long_description,
	author='Andrei Thuler',
	author_email='info@andreithuler.com',
	url="https://github.com/athuler/Python-Packaging-Test",
	packages=find_packages(),
	py_modules=find_packages(),
	install_requires=["wheel"],
	
) #https://youtu.be/n2d_7RPTKlk?t=833