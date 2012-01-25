#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# 
# Find the sum of the digits in the number 100!
#

import math,sys

factorial_list = range(1,100 + 1)
add_list = []

def add(x,y):
  return x + y

def multiply(x,y):
  return x * y

factorial = reduce(multiply,factorial_list)

while factorial:
  add_list.append(factorial % 10)
  factorial = math.trunc(factorial/10)

print reduce(add,add_list)
