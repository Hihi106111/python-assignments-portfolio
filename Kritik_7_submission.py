import numpy as np
from scipy.special import gamma
def t_distribution_pdf(x, nu):
    coeff = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2))
    density = coeff * (1 + x**2 / nu) ** (-0.5 * (nu + 1))
    return density
"""
Compute the probability density of the t-distribution
at a given point x with nu degrees of freedom.
Parameters:
x (float): The point at which to evaluate the density.
nu (int): The degrees of freedom of the t-distribution.
Returns:
density (float): The probability density at point x for
the t-distribution with nu degrees of freedom.
"""

s = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]
def mean(x):
    return sum(x) / len(x)
print("mean =" + str(mean(s)))

def dev(x):
    m = mean(x)
    s_v = []
    for i in range (len(x)):
        v = (x[i] - m)**2
        s_v.append(v)
    return ((1 / (len(x) - 1)) * sum(s_v))**(1/2)
print("standard deviation =" + str(dev(s)))

def t(x,mu_0):
    return (mean(x) - mu_0)/(dev(x)/np.sqrt(len(x)))
print("t_0 =" + str(t(s,75)))

def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):
# Define the x values
    x = np.linspace(x_start, x_end, num_points)
# Apply the density function to the x values
    y = t_distribution_pdf(x, nu)
# This next line is the integration (exercise: why does this work?)
    cdf = np.cumsum(y) * (x[1] - x[0])
# Find the t-value where the cumulative probability reaches half of the required probability
    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]
"""
Find the t-value t* for a given cumulative probability
and degrees of freedom.
Parameters:
prob (float): The cumulative probability (between 0 and 1).
nu (int): The degrees of freedom of the t-distribution.
x_start (float): The start point for numerical integration.
x_end (float): The end point for numerical integration.
20 will almost always be big enough.
num_points (int): The number of points to use in
the numerical integration.
Returns:
float: The t-value t* such that the area between [-t*, t*]
equals the given probability.
"""
print("t* =" + str(find_t_star(0.95, len(s)-1)))

def tf_test(x):
    if int(-(find_t_star(0.95, len(x) - 1))) < int(t(x, 75)) < int(find_t_star(0.95, len(x) - 1)):
        return True
    else:
        return False
print("t_0 is within the bounds [" + str(-(find_t_star(0.95, len(s)-1))) + "," + str(find_t_star(0.95, len(s)-1)) + "]: " + str(tf_test(s)))

print("For the new teaching style I do not think that the mu = 75. I think that it is higher given that t_0 is 2.29")
print("and if you substitute the mean of the student test scores for 75 you get a t value of 2.25")