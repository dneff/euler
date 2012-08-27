#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The 5-digit number, 16807=7**5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
#
# Why doesn't this have an infinite result set?
# Ah, can't be greater than 10, as 10**x will always always have a result one larger than x.
# Can't quite make out the limiter for the other variable, but limiting to 100 works.
#
import math,sys

def int_length(x):
  return len(list(str(x)))

count = 0

x = 1
while x < 10:
  integer = 1
  while integer:
    if int_length(x**integer) == integer:
      print x,integer,x**integer
      count +=1
    if int_length(x**integer) > integer or integer > 100:
      break
    integer += 1
  x += 1

print 'solution: ',count
