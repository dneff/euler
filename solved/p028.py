#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# Starting with the number 1 and moving to the right in
# a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on
# the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 
# 1001 by 1001 spiral formed in the same way?
#
# There's 2 sine waves going on in the generation. Thinking...
#
# Cooking waffles-- figured there's a mathematical progression (+2,+4,+6...)
# Ah! (2n + 1)**2 is always a corner, then backpedal 3 spots by 2n for the others.
#
import math,sys

square_size = 1001
max_diag = (square_size - 1)/2 + 1
sum = 1
for x in range(1, max_diag):
  corner = (2 * x + 1)**2
  sum += corner
  # leaving expanded for readibility
  sum += (corner - 2 * x) + (corner - 4 * x) + (corner - 6 * x)

print sum
