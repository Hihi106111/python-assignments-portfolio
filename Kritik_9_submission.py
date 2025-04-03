import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x,y = sp.symbols( 'x y')

dxx = sp.diff(sp.cos(x),x,x)

# a)
f = sp.exp(x) * sp.sin(y) + y**3

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
print(df_dx.subs({x : 1, y : -1}))

# b)

g = x **2 * y + x * y ** 2

def magnitude_of_gradient(func, p1, p2):
    x,y = sp.symbols( 'x y')
    dfunc_dx = sp.diff(func, x)
    dfunc_dy = sp.diff(func, y)


    return sp.sqrt((dfunc_dx.subs({x:p1,y:p2}) ** 2 + dfunc_dy.subs({x:p1,y:p2}) ** 2))
print(magnitude_of_gradient(g, 1,-1))

# c)

h = sp.ln(x**2 + y**2)

dh_dxx = sp.diff(h,x,x)
dh_dyx = sp.diff(h,y,x)
dh_dxy = sp.diff(h,x,y)
dh_dyy = sp.diff(h,y,y)
print(dh_dxx)
print(dh_dyx)
print(dh_dxy)
print(dh_dyy)

# d)

"""j = x**3 - 3*x*y + y**3
j_func = sp.lambdify((x, y), j, 'numpy')
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
"""

k = (sp.sin(x**3 - y**2))
k_func = sp.lambdify((x, y), k, 'numpy')
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = k_func(X, Y)
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $k(x, y) = sin(x^3 - y^2)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()