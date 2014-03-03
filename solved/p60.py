#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any
# order the result will always be prime. For example,
# taking 7 and 109, both 7109 and 1097 are prime. The sum
# of these four primes, 792, represents the lowest sum for
# a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any
# two primes concatenate to produce another prime.
#

from neff import *
import itertools, math, sys


def concat(x,y):
  return int(str(x) + str(y)), int(str(y) + str(x))

def test_concat(x,y):
  a,b = concat(x,y)
  if prime.is_prime(a) and prime.is_prime(b):
    return True
  return False

def concat_list(x, l):
  solution = []
  for num in l:
    if test_concat(x, num):
      solution.append(num)
  return solution

primes = []

for x in prime.generator():
  primes.append(x)
  if len(primes) > 10000:
    break

solution = []
for x1 in xrange(0, len(primes)):
  p1 = concat_list(primes[x1], [x for x in primes if x > primes[x1]])
  if len(p1) >= 4:
    for x2 in xrange(0, len(p1)):
      p2 = concat_list(p1[x2], [x for x in p1 if x > p1[x2]])
      if len(p2) >= 3:
        for x3 in xrange(0, len(p2)):
          p3 = concat_list(p2[x3], [x for x in p2 if x > p2[x3]])
          if len(p3) >= 2:
            for x4 in xrange(0, len(p3)):
              p4 = concat_list(p3[x4], [x for x in p3 if x > p3[x4]])
              if len(p4) >= 1:
                for x5 in xrange(0,len(p4)):
                  match = [primes[x1],p1[x2],p2[x3],p3[x4],p4[x5]]
                  if len(solution) == 0:
                      solution = match[:]
                  elif sum(solution) > sum(match):
                      solution = match[:]
                      print solution, sum(solution)
