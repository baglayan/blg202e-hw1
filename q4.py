# Student Name : Meriç Bağlayan
#  Student ID   : 150190056
# Course       : BLG 202E Numerical Methods 2023 Spring
# Project      : Homework 1

import sys


def sign(x):
    return x / abs(x)


def f(x: float, cvar: float):
    try:
        result = float(x) ** (5) - cvar
    except OverflowError as err:
        print("Overflowed: " + str(err))
        quit()
    return result


def interval_halving(a: float, b: float, steps: int, very_small_number: float, allowed_margin: float, cvar: float):
    u = f(a, cvar)
    v = f(b, cvar)
    error = b - a

    midpoint = a + error

    i = 1

    for k in range(1, steps):
        if (sign(u) == sign(v)):
            break
        error /= 2
        midpoint = a + error
        w = f(midpoint, cvar)

        if (abs(w) < very_small_number or abs(error) <= allowed_margin):
            return midpoint

        if (sign(w) != sign(u)):
            b = midpoint
            v = w
        else:
            a = midpoint
            u = w

    return midpoint


try:
    a = float(input("a: "))
    epsilon_input = float(input("epsilon: "))
except ValueError as err:
    print("Invalid input: " + str(err))
    quit()

print("x =  " + str(interval_halving(-a, a, sys.maxsize, sys.float_info.epsilon, epsilon_input, a)) + " such that |a^⅕ - x| ≤ epsilon")
