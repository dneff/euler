#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
#
import math,sys

def last_ten(x):
  return x % 10000000000

solution = 0

for x in range(1,1001):
  solution += x**x
  solution = last_ten(solution)

print solution
