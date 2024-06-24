# Python Packaging Test

This is a test package to test out building and deploying a python application with self-updating capabilities

## Installation

Install the package with pip using:
`pip install git+https://github.com/athuler/Python-Packaging-Test.git@main`

## Running

### Normal Operations

Import and run the packaged application with the following:
```python
from pythonPackagingTest import run
run()
```

### Auto-Updating

Execute `run.py` which will automatically import and run the packaged application, while automatically keeping it up to date using `pip`:

https://github.com/athuler/Python-Packaging-Test/blob/90958bab9fca27c25e161f9e885c85d6d9d70c8f/run.py#L1-L23


## Updating

Manually update the package with:
`pip install --upgrade git+https://github.com/athuler/Python-Packaging-Test.git@main`
