#! /usr/bin/env python
import numpy as np
import math

print("Gib die x1 ein")
x1 = float(input())
print("Gib die y1 ein")
y1 = float(input())
print("Gib die x2 ein")
x2 = float(input())
print("Gib die y2 ein")
y2 = float(input())
print("Gib die x3 ein")
x3 = float(input())
print("Gib die y3 ein")
y3 = float(input())

a = np.array([[1,-x1,-y1], [1,-x2,-y2], [1,-x3,-y3]])
erg1= -(x1**2+y1**2)
erg2= -(x2**2+y2**2)
erg3= -(x3**2+y3**2)
b = np.array([erg1, erg2, erg3])
x = np.linalg.solve(a,b)

x0 = x[1]/2
y0 = x[2]/2
r = math.sqrt(x0**2+y0**2-x[0])

print x
print x0
print y0
print r

l=0.07 #length of the car from front wheel to back wheel in m
gamma = math.atan(l/r)
print gamma
