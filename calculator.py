"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
import math

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Can't divide by zero!")
def exp(a, b):
    return a ** b

def log(a, b):
    if a <= 0 or b == 1:
        return ValueError
    return math.log(a, b)








