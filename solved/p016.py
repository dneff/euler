#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#
import math,sys

x = 2**1000

sum = 0

while x:
  sum += x % 10
  x = math.trunc(x / 10)

print sum
