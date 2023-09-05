# MLOPS_Activity2
Class Activity 2 for MLOPs
# Calculator App

A simple calculator app implemented in Python.

## Setup

1. Install the necessary packages:

    ```bash
    make init
    ```

2. To run tests:

    ```bash
    make test
    ```

## Usage

Import the Calculator class from `code.py` and create an instance to use it:

```python
from code import Calculator

calculator = Calculator()
result = calculator.add(1, 2)
print(result)  # Output: 3

