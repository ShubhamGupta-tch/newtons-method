import matplotlib.pyplot as plt

lenhash = {}

space = 1

mins = []
maxs = []

for i in range(1, 10):
    minx = 65*(2**i - 1)
    maxx = 122*(2**i - 1)

    mins.append(minx)
    maxs.append(maxx)

    lenhash[i] = [minx, maxx]

# print(lenhash)

for i, m in enumerate(zip(mins, maxs)):
    plt.plot([m[0], m[1]], [i*space, i*space])

# plt.grid()
plt.show()

