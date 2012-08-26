#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# A googol (10100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a**b, where a,b < 100, 
# what is the maximum digital sum?
#
import math,sys

def sum_of_digits(x):
  return sum([int(y) for y in list(str(x))])

solution = 0
for a in range(1,101):
  for b in range(1,101):
    if sum_of_digits(a**b) > solution:
      solution = sum_of_digits(a**b)

print 'solution: ',solution
