#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# It was proposed by Christian Goldbach that every odd composite 
# number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2 * 1**2
# 15 = 7 + 2 * 2**2
# 21 = 3 + 2 * 3**2
# 25 = 7 + 2 * 3**2
# 27 = 19 + 2 * 2**2
# 33 = 31 + 2 * 1**2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as 
# the sum of a prime and twice a square?
#
import math,sys

primes = [2]

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

x = 2

seeking = True
while seeking:
  x += 1
  if not is_prime(x) and x % 2 == 1:
    seeking = False
    for y in range(1,math.trunc(math.sqrt(x))):
      if (2 * y**2) < x and is_prime(x - (2 * y**2)):
        seeking = True

print x

