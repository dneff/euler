#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 
#
# Note-- brute force will work, but for larger triangles
# it's a fail.
#
# Brute force it is! :) Will optimize after green...
#
# strategy, let's work our way up from the bottom creating 
# a hash of path lists. It'll get longer as we go...
#
# discussed this problem with Mike, when the challenge
# about "the best" path and the triangle prompted the
# "NCAA March Madness" strategy. What if I go to the bottom
# row and work my way up, keeping the winning sums and
# tossing the losing ones? Shouldn't the "winning" sum
# be the best path? This strategy seems sound as at any
# given node, the highest value path is always obvious.
# if I pull this off, I'll probably knock out 67 as well
# as it was hinted at as being the same problem only larger.

import math,sys

triangle = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,03,34],
[88,2,77,73,07,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

def cook_row(short,long):
  cooked = []
  for i in range(0,len(short)):
    value1 = short[i] + long[i]
    value2 = short[i] + long[i + 1]
    if value1 > value2:
      cooked.append(value1)
    else:
      cooked.append(value2)
  return cooked

solution = triangle.pop() 

while triangle:
  solution = cook_row(triangle.pop(),solution)

print solution[0]
