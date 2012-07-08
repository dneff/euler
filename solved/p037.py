#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#

import math,sys

primes = [2]
truncatable = []

def is_prime(x):
  if x == 1: return False
  if x in primes: return True
  max = math.trunc(math.sqrt(x) + 1)
  i = 0
  while primes[i] < max:
   if x % primes[i] == 0: return False
   i += 1
  primes.append(x)
  return True

def is_truncatable(x):
  x_list = list(str(x))
  while x_list:
    if not is_prime(int("".join(x_list))):
      return False
    x_list.pop(-1)
  x_list = list(str(x))
  while x_list:
    if not is_prime(int("".join(x_list))):
      return False
    x_list.pop(0)
  return True

sum = 0

i = 3
while len(truncatable) < 11:
  if is_prime(i) and i > 7:
    if is_truncatable(i):
      truncatable.append(i)
      sum += i
  i += 2

print sum
