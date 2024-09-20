import lrng
import matplotlib.pyplot as plt
import utils
import random

rolls = []
counts = [0] * 6
counts_pairs = [[0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6]
for i in range(1000000):
    roll = lrng.roll_die()
    # roll = random.randint(1, 6)
    rolls.append(roll)
    counts[roll - 1] += 1   
    if i != 0:
        r1 = rolls[i - 1]
        r2 = rolls[i]
        counts_pairs[r1-1][r2-1] += 1

print(counts)
print(counts_pairs)

# print(rolls)

#plt.hist(rolls, bins = 6)
# plt.plot([1,2,3,4,5,6],counts,'o-')
# plt.show()

print(utils.find_longest_streak(rolls))
