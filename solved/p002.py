#!/usr/bin/python
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the 
# sum of the even-valued terms.

total = 0

def fiblist(max):
  fib = []
  a = 0
  b = 1
  latest = 0
  while b < max:
    fib.append(b)
    latest = b
    b = a + b
    a = latest
  return fib
   
for i in fiblist(4000000):
  if i % 2 == 0:
    total = total + i

print total
