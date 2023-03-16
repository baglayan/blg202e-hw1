# Student Name : Meriç Bağlayan
# Student ID   : 150190056
# Course       : BLG 202E Numerical Methods 2023 Spring
# Project      : Homework 1

def sign(x):
    return x / abs(x)

def f(x: float, cvar: float):
    result = float(x) ** (5) - cvar
    return result

def interval_halving(a: int, b: int, epsilon: float, cvar: float):
    u = f(a, cvar)
    v = f(b, cvar)
    diff = b - a

    midpoint = 0

    i = 1

    while True:
        if (sign(u) == sign(v)):
            break
        diff /= 2
        midpoint = a + diff
        w = f(midpoint, cvar)

        if (abs(w) <= epsilon):
            return midpoint

        if (sign(w) != sign(u)):
            b = midpoint
            v = w
        else:
            a = midpoint
            u = w
        
    return midpoint

a = float(input("a: "))
epsilon = float(input("epsilon: "))

print("x: " + str(interval_halving(-a, a, epsilon, a)) + " such that |a^⅕ - x| ≤ epsilon")