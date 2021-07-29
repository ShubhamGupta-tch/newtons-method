# import PyPlot as plt

@time begin
f(x) = x^2 + 9

function df(x, dx=1/1000000000)
    (f(x+dx) - f(x))/dx
end

xs = [x for x in 0:25]
ys = [df(3, 1/10^x) for x in 0:25]
zs = [2x for x in 0:25]
end
# plt.plot3D(xs, ys, zs)
# plt.scatter3D(xs, ys, zs)
# plt.show()
