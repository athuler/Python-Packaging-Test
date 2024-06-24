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

https://github.com/athuler/Python-Packaging-Test/blob/main/run.py


## Updating

Update the package with:
`pip install --upgrade git+https://github.com/athuler/Python-Packaging-Test.git@main`