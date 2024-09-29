import time
import random
import lrng

N = 100000

x = list(range(N))

start_time = time.time()

# x = []
# for i in range(N):
#     x.append(i)

for i in range(N):
    # j = lrng.randint(0, len(x) - 1)
    # j = random.randint(0, len(x) - 1)

    j = N - 1 - i

    del x[j]


end_time = time.time()
print(end_time - start_time)