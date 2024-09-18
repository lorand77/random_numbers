import lrng
import matplotlib.pyplot as plt

def find_longest_streak(x):
    if len(x) == 0:
        return (0, 0)
    position = 0
    streak = 1
    i = 0
    while i < len(x) - 1:
        j = i + 1
        while j < len(x) and x[i] == x[j]:
            j += 1
        if j - i > streak:
            streak = j - i
            position = i
        i += j - i
    return (position, streak)

rolls = []
counts = [0] * 6
counts_pairs = [[0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6]
for i in range(10000000):
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

print(find_longest_streak(rolls))
