#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?
#
# Number partitioning problem gives way to pentagonal number theorem gives way to code
#
import math,sys

memo = {}

def partition_count(x, y):
    if y == 1: return 1
    if y >= x: return 1 + partition_count(x, x - 1)
    if (x, y) not in memo:
        memo[(x, y)] = sum([partition_count(x - i,i) for i in range(1, y + 1)])
    return memo[(x,y)]

print partition_count(100, 99)
