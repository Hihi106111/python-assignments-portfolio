import numpy as np

def f(number):
    return (number)**2
c = 1
E = 0.1
dx = 10**(-8)
def fp(number):
    return (f(number+dx) - f(number-dx))/(2*dx)
def L(number):
    return f(c) + fp(c)*(number-c)
def find_x1(number):
    x = number
    while np.abs(f(x)-L(x)) < E:
        x -= 0.001
    return x
def find_x2(number):
    x = number
    while np.abs(f(x) - L(x)) < E:
        x += 0.001
    return x

print("Function:" + str(f(c)))
print("Derivative:" + str(fp(c)))
print("Linear Approximation:" + str(L(c)))
print("x1:" + str(find_x1(c)))
print("x2:" + str(find_x2(c)))