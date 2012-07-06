#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# In England the currency is made up of pound, P, and pence, p, 
# and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
# It is possible to make P2 in the following way:
#
# 1 P1 + 1 50p + 2 20p + 1 5p + 1 2p + 3 1p
# How many different ways can P2 be made using any number of coins?
#
# Only additive...
# Seems like an base counting problem with an irregular base...
# let's do it that way.
# Surely there's a class called "Currency Math BS 101" somewhere...
# The Brute: create an array with the max for each type and
# increment your way through all combos. Hmmm...itertools?

import math,sys

combo = 0

for two_pound in range(0,1 + 1):
  for one_pound in range(0,2 + 1):
    if (two_pound * 200 + one_pound * 100) > 200:
      break
    for fifty_pence in range(0,4 + 1):
      if (two_pound * 200 + one_pound * 100 + fifty_pence * 50) > 200:
        break
      for twenty_pence in range(0,10 + 1):
        if (two_pound * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20) > 200:
          break
        for ten_pence in range(0,20 + 1):
          if (two_pound * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10) > 200:
            break
          for five_pence in range(0,40 + 1):
            if (two_pound * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5) > 200:
              break
            for two_pence in range(0, 100 + 1):
              if (two_pound * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 + two_pence * 2) > 200:
                break
              for one_pence in range(0, 200 + 1):
                sum = two_pound * 200 + one_pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 + two_pence * 2 + one_pence
                if sum == 200:
                  combo += 1
                  break
print combo
