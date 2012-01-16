#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# 
# The sequence of triangle numbers is generated
# by adding the natural numbers. So the 7th triangle 
# number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
#
# Strat:
#   natural number generator
#   decompose number into prime factors
#   use bitmask to identify all combos (divisors)
#   count unique divisors
#
# Possible insight:
#  Need at least 9 prime factors to have 2^9 possible divisors 
#  

import math,sys

def bitlist(number,size):
  if number.bit_length() > size: 
    print "Error: number needs more bits than size specified" 
    sys.exit(1)
  bits = '{0:0' + str(size) + 'b}'
  return list(bits.format(number))

def add(x,y):
  return x + y

def multiply(x,y):
  return x * y

# DTN - improve here. Too slow
def triangle(x):
  return reduce(add,range(1,x+1))

def smallest_factor(x):
  if is_prime(x):
    return x
  for product in range(2,math.trunc(x/2) + 1):
    if x % product == 0:
      return product

def factors(x):
  results = []
  if is_prime(x):
    results.append(x)
    return results
  results.append(smallest_factor(x))
  f2 = x/smallest_factor(x)
  if is_prime(f2):
    results.append(f2)
  else:
    for ff in factors(f2):
      results.append(ff)
  return results

def is_prime(x):
  for product in range(2, math.trunc(x/2) + 1):
    if x % product == 0:
        return False
  return True

def divisors(prime_list):
  divisor_list = []
  for combo in range(1,2**len(prime_list)):
    filter = [x[0] for x in zip(prime_list,bitlist(combo,len(prime_list))) if int(x[1]) == 1]
    divisor_list.append(reduce(multiply,filter))
  divisor_list.append(1)
  return sorted(list(set(divisor_list)))

x = 1
while True:
  print len(divisors(factors(triangle(x))))
  if len(divisors(factors(triangle(x)))) > 500:
    print x
    print triangle(x)
    print divisors(factors(triangle(x)))
    sys.exit(0)
  x += 1
