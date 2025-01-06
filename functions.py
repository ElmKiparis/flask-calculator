def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


ACTIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power
}
