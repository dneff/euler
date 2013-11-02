#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
#

import math,sys

def cube_gen():
    x = 1
    while True:
        yield x**3
        x +=1

def ordered_string(number):
    return ''.join(sorted(list(str(number))))

cubes = {}
y  = cube_gen()

done = False
while done == False:
    this_cube = y.next()
    ordered_cube = ordered_string(this_cube)
    if ordered_cube in cubes:
        cubes[ordered_cube].append(this_cube)
    else:
        cubes[ordered_cube] = [this_cube]
    if len(cubes[ordered_cube]) == 5:
        print str(cubes[ordered_cube][0])
        done = True


