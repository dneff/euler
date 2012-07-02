#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# 
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are 
# an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math,sys

max = 10001

numsum = {}


def sum_of_factors(x):
  results = []
  for product in range(1, math.trunc(x/2) + 1 ):
    if x % product == 0:
      results.append(product)
  return sum(results)

# ensure it's not a prime, nor equal to itself
for number in range(1,max):
  summed = sum_of_factors(number)
  if summed != 0:
    if summed != number:
      numsum[number] = summed

amicables = []
for key in numsum.keys():
  if numsum[key] in numsum.keys():
    if numsum[numsum[key]] == key:
      amicables.append(key)

print sum(amicables)
