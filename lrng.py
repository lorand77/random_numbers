def lgc(x):
    m = 2 ** 16 + 1
    a = 75
    c = 74
    return (x * a + c) % m

state = 48698   ## seed 

def die_roll():
    global state
    state = lgc(state)
    return state % 6 + 1
