import  numpy as np

a = 0
b = 2


def f(x):
    return np.arctan(x) - (x)**2

def roots(f, a, b):
    tolerance = 1e-11
    if a ==0:
        a = 1e-100
    while tolerance < (b-a):
        if f((a+b)/2) == 0:
            return (a+b)/2
        if f((a+b)/2) * f(a) < 0:
            b = (a+b)/2
        else:
            a = (a+b)/2
    return (a + b) / 2

print(roots(f, a, b))