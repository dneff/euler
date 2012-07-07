#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# We shall say that an n-digit number is pandigital if it makes
# use of all the digits 1 to n exactly once; for example, the 
# 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 * 186 = 7254,
# containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so
# be sure to only include it once in your sum.
#
# Look at the re-use fun. Awesome.
#
# Took way more code than expected.
#
import math,sys,itertools

factor_dict = {}
primes = [2]

def multiply(a,b):
  return a * b

def add(a,b):
  return a + b

def bitlist(number,size):
  if number.bit_length() > size: 
    print "Error: number needs more bits than size specified" 
    sys.exit(1)
  bits = '{0:0' + str(size) + 'b}'
  return list(bits.format(number))

def bit_array(size):
  bits = []
  for x in range(0,2**size):
    bits.append(bitlist(x,size))
  return bits

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

def divisors(prime_list):
  divisor_list = []
  for combo in range(1,2**len(prime_list)):
    filter = [x[0] for x in zip(prime_list,bitlist(combo,len(prime_list))) if int(x[1]) == 1]
    divisor_list.append(reduce(multiply,filter))
  divisor_list.append(1)
  return sorted(list(set(divisor_list)))

solution = []
x = 2
while (x < 9999):
  for factor in divisors(factors(x)):
    numfact = list(str(x) + str(x/factor) + str(factor))
    numfact.sort()
    numfact = [int(y) for y in numfact]
    if numfact == range(1,len(numfact) + 1):
      if numfact[-1] != 9:
        break
      if x not in solution:
        solution.append(x)
  x += 1

print reduce(add,solution)

