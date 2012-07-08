#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The number, 197, is called a circular prime because
# all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#
# let's get all the primes below a million, then start testing...
#

import math,sys

max_number = 1000000

primes = [2]
circular_primes = []

def is_prime(x):
  if x in primes: return True
  max = math.trunc(math.sqrt(x) + 1)
  i = 0
  while primes[i] < max:
   if x % primes[i] == 0: return False
   i += 1
  primes.append(x)
  return True

for num in range(3,max_number,2):
  is_prime(num)

for prime in primes:
  int_list = list(str(prime))
  if len(int_list) == 1:
    circular_primes.append(prime)
  primo = True
  for i in range(0,len(int_list)):
    rotated = int("".join(int_list[i:] + int_list[:i]))
    if not is_prime(rotated):
      primo = False
  if primo and prime not in circular_primes:
    circular_primes.append(prime)

print len(circular_primes)
