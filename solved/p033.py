#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The fraction 49/98 is a curious fraction, as an
# inexperienced mathematician in attempting to
# simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 
# 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this 
# type of fraction, less than one in value, and containing
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in
# its lowest common terms, find the value of the denominator.
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

def is_nontrivial(x,y):
    x_list = list(str(x))
    y_list = list(str(y))
    if len(x_list) == 1 or len(y_list) == 1:
      return False
    if int(x_list[0]) != 0 and  int(y_list[1]) != 0:
      if (x / float(y)) == int(x_list[0]) / float(y_list[1]):
        if x % 11 == 0 or y % 11 == 0:
          return False
        if x_list[1] != y_list[0]:
          return False
        return True
    if int(x_list[1]) != 0 and  int(y_list[0]) != 0:
      if (x / float(y)) == int(x_list[1]) / float(y_list[0]):
        if x % 11 == 0 or y % 11 == 0:
          return False
        if x_list[0] != y_list[1]:
          return False
        return True


def have_common(list_a,list_b):
  for x in list_a:
    if x in list_b:
      return True
  return False

def common(list_a,list_b):
  return [x for x in list_a if x in list_b]

n_factors = []
d_factors = []

for x in range(1,100):
  for y in range(x,100):
    if is_nontrivial(x,y):
      n_factors.extend(factors(x))
      d_factors.extend(factors(y))

common_factors = common(n_factors,d_factors)
for f in common_factors:
  if f in n_factors:
    n_factors.pop(n_factors.index(f))
  if f in d_factors:
    d_factors.pop(d_factors.index(f))

print reduce(multiply,d_factors)
