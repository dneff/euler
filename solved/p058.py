#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom
# right diagonal, but what is more interesting is that 8 out of the 13
# numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
#
# If one complete new layer is wrapped around the spiral above, a
# square spiral with side length 9 will be formed. If this process
# is continued, what is the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below 10%?
#
# length to the corner from 1:
# 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6...
# m'thinks I see a pattern.

import math,sys

primes = [2]

def is_prime(x):
  if x in primes: return True
  max = math.trunc(math.sqrt(x)) + 1
  num_range = [p for p in primes if p < max]
  while num_range:
    if x % num_range.pop(0) == 0: return False
  primes.append(x)
  return True

def corner_distance(x):
  return 2 * ((x / 4) + 1)

seeking = True
diagonal_total = 1
corner_val = 1
corner_primes = 0
x = 0

print "priming..."
prime = 3
while primes[-1] < 40000:
  is_prime(prime)
  prime += 2

print "seeking..."
while seeking:
  corner_val += corner_distance(x)
  diagonal_total += 1
  if is_prime(corner_val):
    corner_primes += 1
  diagonal_ratio = float(corner_primes)/float(diagonal_total)
  print corner_primes, '/', diagonal_total,'=', diagonal_ratio, corner_val
  if corner_distance(x) > 9 and diagonal_ratio < .1:
    break
  x += 1

print 'solution: ', corner_distance(x) + 1
