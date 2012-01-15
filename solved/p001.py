#!/usr/bin/python

total = 0
multiples = [3,5]
for i in range(1,1000):
  for value in multiples:
    if i % value == 0:
      total = total + i
      break

print total
