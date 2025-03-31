import matplotlib.pyplot as plt
import numpy as np

def gradient_descent(f, learning_rate, initial_point):

    def deriv(f, base_point): #estimate the derivative
                              #of the function f at base_point using the symmetric approx
        return (f(base_point+10**(-10))-f(base_point-10**(-10)))/(2*10**(-10))

    x_coords=[initial_point] #This list is where you will store the x_n's
    y_coords=[f(initial_point)] #This list is where you will store the y_n's
#PUT YOUR CODE HERE!
    i = 1
    while abs(deriv(f, x_coords[i-1]))>(10**(-10)) and i<10000:
        xi = x_coords[i-1] - learning_rate * deriv(f, x_coords[i-1])
        x_coords.append(xi)
        yi = f(x_coords[i])
        y_coords.append(yi)
        i += 1


    # Plotting portion. You may adjust as you please.
    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,10000) #to make look good

    function_range=[f(i) for i in plot_range]
    plt.plot(plot_range, function_range) #this plots the function f(x)
    plt.plot(x_coords, y_coords) #This will plot the
    plt.show()
    #sequence of points x_n, f(x_n)

    return round(x_coords[-1],3), round(y_coords[-1],3) #returns your
# last x_n and y_n, #rounded to three decimal places.

def function_1(number):
    return number**2

def function_2(number):
    return (number)**4 - 2*(number)**2

def funny_function(x):
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)

gradient_descent(function_1, 0.9, 5)

gradient_descent(function_2, 0.1, 0.1)

gradient_descent(funny_function, 0.1, 0.5)