# TCI statistic library

This library is in Python3 and calculate various statistics.

Right now the Cronbach Alpha is available.

Example:

    from tcistats import cronbach_alpha
    cronbach_alpha([[1, 2, 3], [2, 3, 4], [3, 4, 5]])

[Read the tests](https://github.com/anthropedia/tci-stats/blob/master/test/__init__.py)
for further usage examples.


## Installation

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


## Running tests

    source venv/bin/activate
    pyhton3 -m unittest