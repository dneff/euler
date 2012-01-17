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
#  Need to create a prime factors array for each number for lookup purposes
#  

import math,sys
# handy for profiling
# import cProfile
# cProfile.run('solution()')

primes = [2]
factor_dict = {}

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

# corrected function.
# show more care/focus.
def triangle(x):
  return (x * (x + 1))/2 

def smallest_factor(x):
  if x in factor_dict: return factor_dict[x][0]
  if is_prime(x): return x
  for prime in primes:
    if x % prime == 0: return prime

def is_prime(x):
  if x in factor_dict: return False 
  if x in primes: return True
  max = math.trunc(x/2)
  num_range = [p for p in primes if p < max]
  while num_range:
    if x % num_range.pop(0) == 0: return False
  primes.append(x)
  return True

def factors(x):
  if x in factor_dict: return factor_dict[x]
  results = []
  if is_prime(x):
    results.append(x)
    return results
  f1 = smallest_factor(x)
  results.append(f1)
  f2 = x/f1
  if is_prime(f2): results.append(f2)
  else:
    for ff in factors(f2):
      results.append(ff)
  factor_dict[x] = results
  return results

# insight - if you have an array, you can use a 
# bit array of the same length to help find all
# the combinations of elements.
# came to me while driving with my daughter (AFK).
def divisors(prime_list):
  divisor_list = []
  for combo in range(1,2**len(prime_list)):
    filter = [x[0] for x in zip(prime_list,bitlist(combo,len(prime_list))) if int(x[1]) == 1]
    divisor_list.append(reduce(multiply,filter))
  divisor_list.append(1)
  return sorted(list(set(divisor_list)))

# by making a solution function, you can use the code profiler
# much easier
def solution():
  x = 2
  while True:
    candidate = factors(triangle(x))
    # need at least 9 factors
    if len(candidate) > 8: 
      if len(divisors(candidate)) > 500:
        return reduce(multiply,candidate)
    x += 1

# real	0m25.564s
# user	0m25.526s
# sys	0m0.016s
print solution()
