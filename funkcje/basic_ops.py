import math
import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Pierwiastek z liczby ujemnej!")
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        raise ValueError("Silnia z liczby ujemnej!")
    return math.factorial(n)

def logarithm(a, base=10):
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Niepoprawne dane do logarytmu!")
    return math.log(a, base)

def random_number(start, end):
    return random.randint(start, end)
