#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The first known prime found to exceed one million digits
# was discovered in 1999, and is a Mersenne prime of the form
# 269725931; it contains exactly 2,098,960 digits. Subsequently
# other Mersenne primes, of the form 2**p - 1, have been found which
# contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime
# which contains 2,357,207 digits: (28433 * 2**7830457)+1.
#
# Find the last ten digits of this prime number.
#
import math,sys

def int2array(x):
  return list(str(x))

def array2int(x):
  return int(('').join(x))

solution = 28433
for x in range(1,7830458):
 if x % 100000 == 0:
  print x
 solution *= 2
 if len(int2array(solution)) > 10:
   solution = array2int(int2array(solution)[-10:])

print 'solution: ',array2int(int2array(solution + 1))
