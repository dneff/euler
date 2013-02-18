#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# Description here
#
import math,sys,string,itertools

def minimum(x,y):
  if x < y:
    return x
  else:
    return y

fh = open('./p081-matrix.txt', 'r')
matrix = []
solution_matrix = []

for line in fh:
  matrix.append([int(x) for x in line.split(',')])
  solution_matrix.append([[] for x in line.split(',')])

for y in range(len(matrix) - 1,-1,-1):
  for x in range(len(matrix) - 1,-1,-1):
    down = False
    right = False
    if y+1 <= len(matrix) - 1:
      down = True
    if x+1 <= len(matrix) - 1:
      right = True

    if down and right:
      solution_matrix[y][x] = matrix[y][x] + minimum(solution_matrix[y+1][x],solution_matrix[y][x+1])
    elif down:
      solution_matrix[y][x] = matrix[y][x] + solution_matrix[y+1][x]
    elif right:
      solution_matrix[y][x] = matrix[y][x] + solution_matrix[y][x+1]
    else:
      solution_matrix[y][x] = matrix[y][x]
print(solution_matrix[0][0])
