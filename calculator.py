"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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
def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        print("Error: Can't log to zero!")

def exp(a, b):
    return a ** b


