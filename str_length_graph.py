import matplotlib.pyplot as plt
import numpy as np
import math

lenhash = {}

space = 1

mins = []
maxs = []

for i in range(1, 200):
    minx = 48*(2**i - 1) + sum([(48**2)**p for p in range(i)])
    maxx = 122*(2**i - 1)+ sum([(122**2)**p for p in range(i)])

    mins.append(math.log(minx))
    maxs.append(math.log(maxx))

    lenhash[i] = [minx, maxx]

# print(lenhash)

for i, m in enumerate(zip(mins, maxs)):
    plt.plot([m[0], m[1]], [(i+1)*space, (i+1)*space])

# plt.grid()
plt.show()

