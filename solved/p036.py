#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
import math,sys

def int_palindrome(a):
  reversed_list = list(str(a))
  reversed_list.reverse()
  if list(str(a)) == reversed_list:
    return True
  return False

def bin_palindrome(a):
  reversed_bin = list(a)[2:]
  reversed_bin.reverse()
  if list(a)[2:] == reversed_bin:
    return True
  return False

sum = 0

for number in range(1,1000001):
  if int_palindrome(number):
    if bin_palindrome(bin(number)):
      sum += number

print sum
