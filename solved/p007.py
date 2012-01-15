#!/usr/bin/python
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?

import math,sys

def is_prime(x):
  for product in range(2, math.trunc(x/2) + 1):
    if x % product == 0:
        return False
  return True

prime = [2]

x = 2

while len(prime) < 10001:

  x = x + 1

  test_list = []

  test_list.extend(prime)

  while len(test_list) > 0:
    y = test_list.pop(0)
    if y != 1:
      if x % y == 0:
        break

  if len(test_list) == 0:
    prime.append(x)

  if len(prime) % 500 == 0:
     print len(prime)

print prime[-1]
