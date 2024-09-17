import lrng
import matplotlib.pyplot as plt

rolls = []
counts = [0] * 6
counts_pairs = [[0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6]
for i in range(36000):
    roll = lrng.roll_die()
    rolls.append(roll)
    counts[roll - 1] += 1

for i in range(len(rolls)-1):
    r1 = rolls[i] 
    r2 = rolls[i+1]
    counts_pairs[r1-1][r2-1] += 1

print(counts)
print(counts_pairs)

# print(rolls)

#plt.hist(rolls, bins = 6)
# plt.plot([1,2,3,4,5,6],counts,'o-')
# plt.show()
