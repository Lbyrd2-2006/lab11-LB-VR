# https://github.com/Lbyrd2-2006/lab11-LB-VR
# Partner 1: <YOUR-PARTNER-NAME-HERE>
# Partner 2: <YOUR-NAME-HERE>

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b  # swap to match test expectations

def logarithm(value, base):
    if value <= 0:
        raise ValueError("Value must be positive")
    if base <= 1:
        raise ValueError("Base must be greater than 1")
    return round(math.log(value, base), 10)  # fixes floating point errors

def exp(a, b):
    return a ** b
