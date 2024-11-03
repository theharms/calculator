def add(a, b):
    return a+b

def substract(a, b):
    return a-b


def multiplay(a, b):
    return a*b


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "you can't devide by zero"
