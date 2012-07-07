#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# What's the upper bound? Looks like 9999999 > 7(9!),
import math,sys

def add(a,b):
  return a + b

def bang(a):
  return math.factorial(a)

max_number = 7 * math.factorial(9)

solution = 0

for num in range(3,max_number):
  if num == reduce(add,map(bang,[int(x) for x in str(num)])):
    solution += num

print solution
