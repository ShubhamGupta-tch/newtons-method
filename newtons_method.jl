import PyPlot as plt

f(x) = x^2 - 25

m = 0
c = 0

y(x) = m*x + c

xs = -20:20

plt.plot(xs, f.(xs))
plt.plot(xs, y.(xs))

function df(x, dx=1/1000000000)
    (f(x+dx) - f(x))/dx
end

function root(n=10)
    x = 1

    for _ in 1:n
        x = (df(x)*x - f(x) + c)/(df(x) - m)
    end

    return x
end

ansx = root()
println(ansx)
plt.scatter(ansx, y(ansx))

plt.grid()
plt.show()
