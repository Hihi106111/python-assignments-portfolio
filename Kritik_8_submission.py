import numpy as np
from mpl_toolkits import mplot3d #for 3D plots
import matplotlib.pyplot as plt #usual matplotlib


def gradient_descent(x0, y0,f, grad_f, alpha, num_iterations):
    x, y = x0, y0 # Initialize x and y with the initial point
    for i in range(num_iterations):
        grad_x, grad_y = grad_f(x,y)
        x = x - alpha * int(grad_x)  # YOUR CODE HERE
        y = y - alpha * int(grad_y) # YOUR CODE HERE
    return x, y

def fun_1(x,y):
    return x**2+y**2

def grad_f_1(x,y):
    grad_x = 2 * x
    grad_y = 2 * y
    return grad_x, grad_y

print(gradient_descent(0.1, 0.1, fun_1, grad_f_1, 0.1, 10))
print(gradient_descent(0, -1 , fun_1, grad_f_1, 0.01, 100))

import numpy as np
def fun_2(x,y):
    return 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)

def grad_f_2(x,y):
    grad_x = np.exp(-x**2-(y-2)**2) * (-2 * x) - 2*np.exp(-x**2-(y+2)**2) * (-2 * x)
    grad_y = np.exp(-x**2-(y-2)**2) * (-2 * ( -y + 2)) - 2*np.exp(-x**2-(y+2)**2) * (-2 * (y + 2))
    return grad_x, grad_y

print(gradient_descent(0, 1, fun_2, grad_f_2, 0.01, 10000))
print(gradient_descent(0, -1 , fun_2, grad_f_2, 0.01, 10000))

X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
x,y = np.meshgrid(X,Y)
z = gradient_descent(X, Y, fun_2, grad_f_2, 0.01, 10000)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
#x,y z are variable names.
