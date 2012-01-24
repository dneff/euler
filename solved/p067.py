#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# By starting at the top of the triangle below and moving 
# to adjacent numbers on the row below, the maximum total 
# from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt 
# (right click and 'Save Link/Target As...'), a 15K text 
# file containing a triangle with one-hundred rows.
#
# ...copied the file locally, otherwise untouched. 
#

import math,sys,string

fh = open('./p067-triangle.txt','r')

tri_list = map(string.strip,fh.readlines())

triangle = []

for line in tri_list:
  int_line = line.split(' ')
  triangle.append(map(int, int_line))
  
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
