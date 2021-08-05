import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return (1 - (x**4))**(1/2)

def antif(x):
    return x**2

def graph_from_integral(a, b,  dx=0.001):

    dx = dx * (1 if b>a else -1)
    n_blocks = int((b - a)/dx)

    points = []

    for n in range(n_blocks):
        x = a + 0
        area_till_n = []
        for _ in range(n):
            area_till_n.append(f(x)*dx)

            x += dx

    for n in range(n_blocks):
        x = a + 0
        area_till_n = []
        for _ in range(n):
            area_till_n.append(f(x)*dx)

            x += dx

        points.append((x, sum(area_till_n)))

    xs = [point[0] for point in points]

    # plt.plot(xs, [antif(x) for x in xs])
    plt.plot(xs, [point[1] for point in points])
    plt.show()


graph_from_integral(-1, 1)
