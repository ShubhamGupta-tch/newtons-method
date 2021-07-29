import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3

def df(x, dx=1/1000000000):
    return (f(x+dx) - f(x))/dx

m = 0
c = 0
xs = np.arange(-20, 20, 0.1)
plt.plot(xs, m*xs+c) # mx + c
plt.plot(xs, f(xs)) # f(x)

def y(x):
    return m*x + c

def root(n=10):
    x = 1
    xs = []
    ys = []
    for _ in range(n):
        xs.append(x)
        ys.append(y(x))
        xs.append(x)
        ys.append(f(x))

        x = (df(x)*x - f(x) + c)/(df(x) - m)

    plt.plot(xs, ys)

    return x

ansx = root()
print(ansx)
plt.scatter(ansx, m*ansx + c)

plt.show()

