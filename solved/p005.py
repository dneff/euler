#!/usr/bin/python
#
# 2520 is the smallest number that can be 
# divided by each of the numbers from 1 to 10 
# without any remainder.
# 
# What is the smallest positive number that 
# is evenly divisible by all of the numbers from 1 to 20?

import math,sys

def multiply(x,y):
  return x*y

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

def list_difference(list1,list2):
  return_list = []
  tmplist = []
  tmplist.extend(list1)
  for x in list2:
    if x in tmplist:
      tmplist.remove(x)
    else:
      return_list.append(x)
  return return_list

flist = []

for i in range(1,20):
  for element in list_difference(flist,factors(i)):
    flist.append(element)

print str(reduce(multiply,flist))
