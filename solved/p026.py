#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# Find the value of d < 1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.
#
# Hint: d-1 is the longest possible recurring cycle length
#
# We only care about prime values. Multiples won't yield
# longer results.
#
# Search through primes in descending order
#
# strategy: there's an array of decimals such that the first
# half of the array is equal to the second half of the array.
# However, this doesn't account for the inital decimals which may
# not be part of the pattern.
#
# Going to try thirds. Inefficient, but these calculations are fast
#
# Worked.
#

import math,sys

longest = 0
longest_cycle = []

def is_prime(x):
  for product in range(2, math.trunc(x/2)):
    if x % product == 0:
    	return False
  return True

for number in range(2,1001):
 if is_prime(number):
    decimal = []
    numerator = 10**(len(str(number)))

    while True:
      numerator *= 10
      remainder = numerator % number
      quotient = (numerator - remainder)/number

      thirds = math.trunc(len(decimal) / 3)
      second_third = decimal[(2 * thirds):]
      last_third = decimal[thirds:(2 * thirds)]

      if (second_third == last_third) and len(second_third) > 1:
        if len(second_third) > len(longest_cycle):
          longest_cycle = list(second_third)
          longest = number
        break
      else:
        decimal.append(quotient)

      numerator = remainder

print longest

