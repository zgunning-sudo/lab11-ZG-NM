import math

def square_root(a):
    try:
        math.sqrt(a)
    except ValueError:
        print("Invalid Number")

def hypotenuse(a, b):
    try:
        math.hypot(a, b)
    except:
        print("Invalid")

def add(a, b):
    return a + b

def subtact(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a < 0 or a == 1:
        raise ValueError
    elif b <= 0:
        raise ValueError
    else:
        return math.log(b, a)

def exponent(a, b):
    return a**b