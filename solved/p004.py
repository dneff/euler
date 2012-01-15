#!/usr/bin/python
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91  99.
# Find the largest palindrome made from the product of 
# two 3-digit numbers.
#
# smallest value is five digits
# largest value is six digits
import math,sys

max_int = 999*999
min_int = 100*100

def is_palindrome(number):
  if number == int(str(number)[::-1]):
    return True
  return False

def is_three_digit(number):
  if 99 < number < 1000:
    return True
  return False

def factors(x):
  results = []
  for product in range(math.trunc(math.sqrt(x)),2,-1):
    if x % product == 0:
      results.append(product)
  return results

for i in range(max_int,min_int,-1):
  if is_palindrome(i):
    for f1 in factors(i):
      if is_three_digit(f1):
        f2 = i / f1
        if is_three_digit(f2):
          print str(f1) + " * " + str(f2) + " = " + str(i)
          sys.exit(0)


