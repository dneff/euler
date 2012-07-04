#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# A perfect number is a number for which the sum
# of its proper divisors is exactly equal to the
# number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
# means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its
# proper divisors is less than n and it is called
# abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However,
# this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import math,sys

max_number = 28123

def sum_two(a,b):
  return a + b

def is_less(list,number):
  return [x for x in list if x < number]

def is_abundant(x):
  results = []
  for product in range(1, math.trunc(x/2) + 1 ):
    if x % product == 0:
      results.append(product)
  if sum(results) > x:
    return True
  else:
    return False

abundants = []

for i in range(12,max_number + 1):
  if is_abundant(i):
    abundants.append(i)

sum_of_abundants = []

# create an array of sums of abundants under max_number
ab1 = list(abundants)
ab2 = list(abundants)

while (len(ab1) != 0):
  summed = map(sum_two, ab1, ab2)
  sum_of_abundants.extend(is_less(summed,(max_number + 1)))
  sum_of_abundants = list(set(sum_of_abundants))
  ab1.pop(0)
  ab2.pop(-1)

sum_of_nonabundants = 0

for x in range(1, max_number + 1):
  if x not in sum_of_abundants:
    sum_of_nonabundants += x

print sum_of_nonabundants
