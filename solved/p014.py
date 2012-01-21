#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The following iterative sequence is defined for the set of positive integers:
#
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# DTN - solved the long way (took a couple min)

import math,sys

max_val = 1000000

def cook_even(x):
  return x / 2

def cook_odd(x):
  return (3 * x) + 1

def solution():
  cooked = {} 
  for i in range(1,max_val + 1):
    print i
    number = i
    chain = []
    chain.append(number)
    while number != 1:
      if number % 2 == 0:
        number = cook_even(number)
        chain.append(number)
      else:
        number = cook_odd(number)
        chain.append(number)

    cooked[chain[0]] = len(chain)
  return max(cooked, key=cooked.get)

print solution()

