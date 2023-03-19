# Student Name : Meriç Bağlayan
# Student ID   : 150190056
# Course       : BLG 202E Numerical Methods 2023 Spring
# Project      : Homework 1

import sys

class NegativeAbsoluteValueError(Exception):
    "Exception raised when the value of absolute value is inferred to be negative."
    pass

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

    for k in range(1, steps):
        if (sign(u) == sign(v)):
            break
        error /= 2.0
        midpoint = a + error
        w = f(midpoint, cvar)

        if (abs(w) < very_small_number or ((b - a) / 2) <= allowed_margin):
            return midpoint

        if (sign(w) != sign(u)):
            b = midpoint
            v = w
        else:
            a = midpoint
            u = w
        k += 1

    return midpoint


try:
    a = float(input("a: "))
    epsilon_input = float(input("epsilon: "))
    if (epsilon_input < 0):
        raise NegativeAbsoluteValueError(epsilon_input)
except (ValueError, NegativeAbsoluteValueError) as err:
    print("Invalid input: " + str(err))
    quit()

if (a >= 0):
    result = interval_halving(-a, a, 1000000, sys.float_info.epsilon, epsilon_input, a)
    # print ("absolute value evaluated to " + str(abs(pow(a, 1/5) - result)))
    # print ("epsilon is: " + str(epsilon_input))
else:
    result = interval_halving(a, -a, 1000000, sys.float_info.epsilon, epsilon_input, a)

print()
print("x = " + str(result) + " such that |a^(1/5) - x| <= epsilon")
