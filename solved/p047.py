#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 * 7
# 15 = 3 * 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2**2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.
#
# Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
#
import math,sys

factor_dict = {}
primes = [2]

def multiply(a,b):
  return a*b

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

def prime_count(prime_list):
  count_dict = {}
  for x in prime_list:
    if x in count_dict:
      count_dict[x] += 1
    else:
      count_dict[x] = 1

  return count_dict

seeking = True
x = 2
consecutive = 0

while seeking:
  x += 1
  if len(prime_count(factors(x)).keys()) == 4:
    consecutive += 1
  else:
    consecutive = 0

  if consecutive >= 4:
    solution = {}
    seeking = False
    for y in range(x - 3,x + 1):
      solution[y] = prime_count(factors(y))
    sol_keys = solution.keys()
    while sol_keys:
      x = sol_keys.pop(0)
      for key in sol_keys:
        common = set(solution[x]).intersection(set(solution[key]))
        if len(common) > 0:
          for i in common:
            if solution[x][i] == solution[key][i]:
              seeking = True

print x - 3

