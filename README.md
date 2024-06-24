# Python Packaging Test

This is a test package to test out building and deploying a python application.

## Installation

Install the package with pip using:
`pip install git+https://github.com/athuler/Python-Packaging-Test.git@main`

## Running

### Normal Operation

Import and run the packaged application with the following:
```python
from pythonPackagingTest import run
run()
```

### Auto-Updating

Execute `run.py` which will automatically import and run the packaged application, while automatically keeping it up to date using `pip`.


https://github.com/athuler/Python-Packaging-Test/blob/90958bab9fca27c25e161f9e885c85d6d9d70c8f/run.py


## Updating

Update the package with:
`pip install --upgrade git+https://github.com/athuler/Python-Packaging-Test.git@main`
