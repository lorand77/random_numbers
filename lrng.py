import time

MAX_RAND_INT = 2 ** 31 - 1

def lgc(x):
    m = MAX_RAND_INT
    a = 1583458089
    c = 0
    return (x * a + c) % m

state = int(time.time()*1_000_000) % MAX_RAND_INT   ## seed 

def roll_die():
    global state
    state = lgc(state)
    return state % 6 + 1

def randint(a, b):
    if a > b or type(a) != int or type(b) != int:
        raise ValueError("a must be less or equal to b and both must be integers")
    global state
    state = lgc(state)
    return state % (b - a + 1) + a
