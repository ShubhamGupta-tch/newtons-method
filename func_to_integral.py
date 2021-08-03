import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return math.log(x)

def graph_from_integral(a, b,  dx=0.01):
    dx = dx * (1 if b>a else -1)
    n_blocks = int((b - a)/dx)
    F = []
    xs = []

    for n in range(n_blocks):
        x = a + 0
        area_till_n = []
        for _ in range(n):
            area_till_n.append(f(x)*dx)
            x += dx
        F.append(sum(area_till_n))

    for _ in range(n_blocks):
        xs.append(a+dx)
        a += dx

    plt.plot(xs, F)
    plt.show()




graph_from_integral(1.1, 5)




