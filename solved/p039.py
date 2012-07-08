#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# If p is the perimeter of a right angle triangle with 
# integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p >= 1000, is the number of solutions maximised?
#
import math,sys

max = 1000

solutions = []
p = 0
def pyth_solns(x):
  solutions = []
  for c in range(1,(x/2)):
    for a in range(1,x - c):
      b = x - c - a
      if (a**2 + b**2) == c**2:
        if sorted([a,b,c]) not in solutions:
          solutions.append(sorted([a,b,c]))
  return solutions

for x in range(1,max + 1):
  if len(pyth_solns(x)) > len(solutions):
    solutions = list(pyth_solns(x))
    p = x

print p
