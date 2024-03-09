# ANODI

This is the Python library **ANODI** for Time Series Anomaly Detection. It offers easy access to algorithms and benchmark data.

## Example Usage

- the core of the ANODI library is the algorithm class that wrapps an algorithm and the data that the algorithm should be fit on.
- the data and some meta arguments are set up in a DatasetSpecification in the ```data``` module.
- for example usage, have a look at the ```anodilib/tests/``` at [Branch 1](https://gitlab.fachschaften.org/timonius/anodi/-/tree/dev?ref_type=heads) and [Branch 2](https://gitlab.fachschaften.org/timonius/anodi/-/tree/dev-without-hosted-datasets?ref_type=heads) on our [Github Repository](https://gitlab.fachschaften.org/timonius/anodi/)

## Dev Installation

This package is built using poetry, run the following code to install an editable version of the package for development
```
pip install poetry
poetry install
```

## Extenstions installation

Look for VSCode Flake8 extension to make sure pipeline doesn't fail at the lint stage