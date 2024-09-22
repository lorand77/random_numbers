def find_longest_streak(x):
    if len(x) == 0:
        return {"position": 0, "streak": 0}
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
        i = j
    return {"position": position, "streak": streak}


def find_minimum(x):
    if x == []:
        raise ValueError("list should not be empty")
    minimum = x[0]
    for i in range(len(x)):
        if minimum > x[i]:
            minimum = x[i]
    return minimum
