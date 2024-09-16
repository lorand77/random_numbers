import lrng
import matplotlib.pyplot as plt

rolls = []
counts = [0] * 6
for i in range(6000):
    roll = lrng.die_roll()
    rolls.append(roll)
    counts[roll - 1] += 1

print(counts)

# print(rolls)
plt.hist(rolls, bins = 6)
plt.show()

