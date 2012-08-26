#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# By replacing the 1st digit of *3, it turns out that 
# six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest 
# prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight
# prime value family.
#
# strategy: climb through the primes, stopping off at every power of 10 to check
# for eight primes via a bit filtered array. brutish. Interested in see the optimal
# approach
#
# insight: if we roll the last digit, half the results will be even (thus non-prime).
#
# strategy two: it's a wildcard search. verify a number has matching digits in the
# wildcard slots, then check for primes against the 10 wildcard numbers (nine if the lead
# digit is a wildcard, as the first value cannot be zero). Seems like there's a lamda
# solution...

import math,sys

primes = [2]

def is_prime(x):
  if x in primes:
    return True
  else:
    max = math.trunc(math.sqrt(x)) + 1
    num_range = [p for p in primes if p < max]
    while len(num_range) > 0:
      if x % num_range.pop(0) == 0:
        return False
    primes.append(x)
    return True

def bitlist(number,size):
  if number.bit_length() > size: 
    print "Error: number needs more bits than size specified"
    sys.exit(1)
  bits = '{0:0' + str(size) + 'b}'
  return list(bits.format(number))

def bit_array(size):
  bits = []
  for x in range(1,2**size):
    bits.append(bitlist(x,size))
  return bits

def filterable_number(x,bf):
  matched = []
  for i in range(0,len(x)):
      if bf[i] == '1':
         matched.append(x[i])
  if len(set(matched)) > 1:
    return False
  return True

def match_count(x,bf):
  count = 0
  start = 0
  if bf[0] == '1':
    start = 1
  for digit in range(start,10):
    digit_check = []
    for i in range(0,len(x)):
      if bf[i] == '0':
        digit_check.append(x[i])
      else:
        digit_check.append(str(digit))
    if int(('').join(digit_check)) in primes:
      count += 1
  print ('').join(x),('').join(bit_filter),count
  return count

solution = []

seeking = True
i = 3
checkpoint = 10
while seeking:
  if i > 11 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 11 == 0:
    pass
  else:
     print 'priming ',i
     is_prime(i)
  if i == checkpoint + 1:
    prime_range = [list(str(x)) for x in primes if checkpoint/10 < x < checkpoint]
    for bit_filter in bit_array(int(math.log10(i)) - 1):
      bit_filter.append("0")
      for tester in prime_range:
        if not filterable_number(tester,bit_filter):
          continue
        if match_count(tester,bit_filter) == 8:
          seeking = False
          print 'solution:',('').join(tester),('').join(bit_filter)
          sys.exit(0)
    checkpoint *= 10
  i += 2
