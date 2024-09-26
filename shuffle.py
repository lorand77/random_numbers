import lrng
import random
import matplotlib.pyplot as plt

x = list(range(1, 53))
print(x)

def shuffle(x):
    x = x.copy()
    y = []
    for i in range(len(x)):
        j = lrng.randint(0, len(x) - 1)
        # j = random.randint(0, len(x) - 1)
        y.append(x[j])
        del x[j]
    return y

y = shuffle(x)
print(y)

plt.plot(x, y, "o", markersize = 10)
plt.gcf().set_size_inches(6, 6)
plt.xticks(range(min(x), max(x)+1, 3))
plt.yticks(range(min(y), max(y)+1, 3))
plt.grid(True)
plt.show()