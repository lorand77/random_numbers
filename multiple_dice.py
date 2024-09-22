import matplotlib.pyplot as plt
import utils

n = 1000000
m = 2
rolls = []
for i in range(n):
    rolls.append(utils.sum_of_n_rolls(m))

plt.hist(rolls, bins = m * 10 + 1)
plt.show()
