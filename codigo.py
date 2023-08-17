from math import *

def funcion(x):
    return sin(x) + cos(1 + x**2) - 1

a = -2
b = 4
i = 0

while i<100:
    i += 1

    c = (a + b) / 2
    fc = funcion(c)

    if (fc>0):
        b = c
    elif (fc<0):
        a = c

print(c)