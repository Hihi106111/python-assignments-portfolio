import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

def normal_density(mean, variance, x):
    y = (1 / np.sqrt(2 * np.pi * (variance**2))) * (np.exp((-((x - mean) ** 2))/(2 * (variance ** 2))))
    return y

def integration(mean, variance, a,b):
    def y(x):
        r1 = 1 / (((variance**2) * 2 * np.pi) ** 0.5)
        r2 =   np.exp((-(x-mean)**2)/(2 * variance**2))
        return r1 * r2
    i = int.quad(y,a,b)
    return i[0]

def E(r,a,b):
    def g(x):
        if x<a or x>b:
            return 0
        elif x>a and x<b:
            return 1/(b-a)
    def t(o):
        d = r(o) * g(o)
        return d
    v = int.quad(t,a,b)
    print("4. a) On the arbitrary interval " + str(a) +"," + str(b) + " E(X) = " + str(v[0]))

def f(x):
    return x

def r_event(function,a,b, rate):
    def r(x):
        if x < 0:
            return 0
        elif x > 0 or x == 0:
            return rate * np.exp(-rate * x)
    def t(o):
        d = function(o) * r(o)
        return d
    v = int.quad(t, a, b)
    print("4. b) On the arbitrary interval " + str(a) + "," + str(b) + " E(X) = " + str(v[0]))

def dosage_estimate(function, mean, variance, a,b):
    def y(x):
        r1 = 1 / (((variance**2) * 2 * np.pi) ** 0.5)
        r2 =   np.exp((-(x-mean)**2)/(2 * variance**2))
        return r1 * r2
    def dose(o):
        return function(y(o))
    d_e = int.quad(dose,a,b)
    print("4. c) The average dose for a male of average height is " + str(d_e[0]))

def d(x):
    return 2.38 * (x)**2


print("3. " + str(integration(171,7.1,162,190)))
E(f,1,20)
r_event(f, 3, 20, 1/50)
dosage_estimate(d,171,7.1,162,190)