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
