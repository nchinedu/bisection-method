# Bisection Method for Square Root Approximation

This repository contains a simple and clean Python implementation of the **bisection method** (also known as binary search) to compute the square root of a non-negative real number.

The bisection method repeatedly narrows an interval containing the root of the equation `f(x) = x² - n = 0` until the desired accuracy is reached.

## Features
- Handles negative numbers with a clear error message.
- Exact results for `0` and `1`.
- Customizable tolerance (default: `1e-6`) and maximum iterations (default: `100`).
- Prints helpful messages during execution.
- Returns `None` if convergence fails within the iteration limit.
- No external modules imported (pure Python).

## Usage

Save the code in a file, e.g., `square_root_bisection.py`.

```python
def square_root_bisection(number, tolerance=1e-6, max_iterations=100):
    # ... (your function code here)
