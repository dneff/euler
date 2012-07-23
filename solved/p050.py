#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the
# most consecutive primes?
#
import math,sys,time

max = 1000000

primes = [2]

def is_prime(x):
  prime = True
  if x not in primes:
    max = math.trunc(math.sqrt(x)) + 1
    num_range = [p for p in primes if p < max]
    while prime and len(num_range) > 0:
      if x % num_range.pop(0) == 0:
        prime = False
  if prime:
    primes.append(x)
  return prime

def add(x,y):
  return x + y

for x in range(3,max,2):
  if x > 11 and x % 3 == 0 and x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
    continue
  is_prime(x)

solution = []

for start_point in range(0,len(primes)):
  end_point = start_point + 1
  if end_point > len(primes) - 1:
    continue
  total = list(primes[start_point:end_point])
  while sum(total) < max:
    if is_prime(sum(total)):
      if len(total) > len(solution):
        solution = list(total)
    end_point += 1
    total = list(primes[start_point:end_point])

print sum(solution)
