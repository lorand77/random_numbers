import random

p = 0.6
N = 11
M = 100000
win_player1 = 0

for i in range(M):
    win_game1 = 0
    for j in range(N):
        if random.uniform(0, 1) < p:
            win_game1 += 1
    if win_game1 > N / 2:
        win_player1 += 1

print(win_player1 * 100 / M)
