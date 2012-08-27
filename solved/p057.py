#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
#  sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
#  By expanding this for the first four iterations, we get:
#
#  1 + 1/2 = 3/2 = 1.5
#  1 + 1/(2 + 1/2) = 7/5 = 1.4
#  1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
#  The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
#  In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
#
import math,sys

numerator = 1
denominator = 1

def int_length(x):
  return len(list(str(x)))

def next_number(n,d):
  return (n+d+d),(n+d)

count = 0

for iteration in range(1,1001):
  if int_length(numerator) > int_length(denominator):
    count += 1
  numerator,denominator = next_number(numerator,denominator)

print "solution: ",count
