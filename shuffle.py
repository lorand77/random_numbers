import lrng
import random
import matplotlib.pyplot as plt
import time

N_CARDS = 1000000

x = list(range(1, N_CARDS+1))


def shuffle_lorand(x):
    x = x.copy()
    y = []
    for i in range(len(x)):
        j = lrng.randint(0, len(x) - 1)
        # j = random.randint(0, len(x) - 1)
        y.append(x[j])
        del x[j]       # very slow for larger numbers n > 40000
    return y

def shuffle_FY(x):
    n = len(x)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        x[i], x[j] = x[j], x[i]

# start_time = time.time()
# y = shuffle_lorand(x)
# # print(y)
# end_time = time.time()
# print(end_time - start_time)


start_time = time.time()
y = list(x)
shuffle_FY(y)
# print(y)
end_time = time.time()
print(end_time - start_time)


start_time = time.time()
y.sort()
# print(y)
end_time = time.time()
print(end_time - start_time)


# plt.plot(x, y, "o", markersize = 10)
# plt.gcf().set_size_inches(6, 6)
# plt.xticks(range(min(x), max(x)+1, 3))
# plt.yticks(range(min(y), max(y)+1, 3))
# plt.grid(True)
# plt.show()
