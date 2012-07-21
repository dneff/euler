#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
# increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing
# sequence.
#
# What 12-digit number do you form by concatenating the three terms in
# this sequence?
#
import math,sys

solution = ""

primes = [2]

def is_prime(x):
  if x in primes: return True
  max = math.trunc(math.sqrt(x)) + 1
  num_range = [p for p in primes if p < max]
  while num_range:
    if x % num_range.pop(0) == 0: return False
  primes.append(x)
  return True


for x in range(2,10000):
  is_prime(x)

four_digit = [list(str(x)) for x in primes]

combos = []

for x in range(0,len(four_digit)):
  y = 0
  combo = []
  combo.append(int("".join(four_digit[x])))
  while y < len(four_digit) - 1:
    y += 1
    if sorted(four_digit[x]) == sorted(four_digit[y]) and x != y:
      combo.append(int("".join(four_digit[y])))
  if len(combo) >= 3:
    combo.sort()
    if combo not in combos:
      combos.append(combo)

for combo in combos:
# print combo
  for x in range(0,len(combo)):
    y = x + 1
    while y < len(combo) - 1:
      test_val = combo[y] + (combo[y] - combo[x])
      if test_val > combo[-1]:
        y += 1
        continue
      if test_val in combo and combo[x] != 1487:
        solution = "".join([str(combo[x]),str(combo[y]),str(test_val)])
      y += 1

print solution
