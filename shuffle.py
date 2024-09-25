import lrng
import random

x = list(range(1, 53))
print(x)

def shuffle(x):
    y = []
    for i in range(len(x)):
        j = lrng.randint(0, len(x) - 1)
        # j = random.randint(0, len(x) - 1)
        y.append(x[j])
        del x[j]
    return y

print(shuffle(x))