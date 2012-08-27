#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# A number chain is created by continuously adding the
# square of the digits in a number to form a new number
# until it has been seen before.
#
# For example,
#
# 44 > 32 > 13 > 10 > 1 > 1
# 85 > 89 > 145 > 42 > 20 > 4 > 16 > 37 > 58 > 89
#
# Therefore any chain that arrives at 1 or 89 will become
# stuck in an endless loop. What is most amazing is that
# EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
#
import math,sys

def array_of_int(x):
  return [int(x) for x in list(str(x))]

def next_val(x):
  return sum([x**2 for x in array_of_int(x)])

max = 10000000

def is_89(x):
  if x == 89: return True
  if x == 1: return False
  return is_89(next_val(x))

count = 0

x = 1

while x < max:
  if is_89(x):
    count += 1
  x += 1

print 'solution:', count
