import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except:
        raise

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
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

def exp(a, b):
    return a**b