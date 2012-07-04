#!/usr/bin/python
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# check for modulus 0 in range 2,square(600851475143)
# starting with largest value check for any modulus in range 2,square(factor)
# first prime is answer
import math

def factors(x):
  results = []
  for product in range(2, math.trunc(math.sqrt(x))):
    if x % product == 0:
      results.append(product)
  return results

def is_prime(x):
  for product in range(2, math.trunc(math.sqrt(x))):
    if x % product == 0:
    	return False
  return True

for number in factors(600851475143)[::-1]:
 if is_prime(number):
   print number
   break
