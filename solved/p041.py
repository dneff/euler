#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# We shall say that an n-digit number is pandigital if it
# makes use of all the digits 1 to n exactly once. For 
# example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#
import math,sys,itertools

def is_pandigital(x):
  x_list = [int(x) for x in list(str(x))]
  if len(x_list) == len(set(x_list)):
    if set(range(1,len(x_list))).issubset(set(x_list)):
        return True
  return False

solution = 0

pandigitals = []


for x in range(1,10):
  combos = list(itertools.permutations(range(1,x + 1),x))
  for pd in combos:
    x = int("".join([str(x) for x in pd]))
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
      pandigitals.append(x)

while pandigitals:
    number = pandigitals.pop(-1)
    y = 3
    is_prime = True
    while y < (math.trunc(math.sqrt(number) + 1)):
      if number % y == 0:
        is_prime = False
        break
      y += 2
    if is_prime:
      solution = number
      break

print solution
