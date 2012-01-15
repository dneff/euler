#!/usr/bin/python
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

import math,sys

def is_prime(x):
  for product in range(2, math.trunc(x/2) + 1):
    if x % product == 0:
        return False
  return True

not_prime = []
prime = [2]
x = 2

while x < 2000000:
  x = x + 1
  test_list = []
  test_list.extend(prime)

  while len(test_list) > 0:
    if x % test_list.pop(0) == 0:
      break

  if len(test_list) == 0:
    prime.append(x)

  if x % 10000 == 0:
     print x,len(prime) 

print sum(prime)
