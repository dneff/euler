#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
#
import math,sys

fraction = ''
x = 1

while len(fraction) < 1000000:
  fraction += str(x)
  x +=1
solution = (int(fraction[0]) * int(fraction[9]) * int(fraction[99]) * int(fraction[999]) * int(fraction[9999]) * int(fraction[99999]) * int(fraction[999999]))
print solution

