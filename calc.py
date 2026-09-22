import test_calc

def add(x,y):
    return x + y

def subtracts(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"  