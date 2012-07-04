#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#

import math,sys

a = 0
b = 1
latest = 0
# starting with the first term
term = 1
while len(list(str(b))) < 1000:
  term += 1
  latest = b
  b = a + b
  a = latest

print term
