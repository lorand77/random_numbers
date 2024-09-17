import time

MAX_RAND_INT = 2 ** 16 + 1

def lgc(x):
    m = MAX_RAND_INT
    a = 75
    c = 74
    return (x * a + c) % m

state = int(time.time()*1_000_000) % MAX_RAND_INT   ## seed 

def roll_die():
    global state
    state = lgc(state)
    return state % 6 + 1
