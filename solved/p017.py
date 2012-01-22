#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there 
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) 
# inclusive were written out in words, how many letters would be used?
#
# Do not count spaces or hyphens. For example, 342 
# (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in 
# compliance with British usage.
#

import math,sys,string

ones = ["","one","two","three","four","five","six","seven","eight","nine","ten"]
teens = ["zero","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundreds = "hundred"
thousands = "thousand"
joins = "and"

master_list = []

def hundred(x):
  num_list = []
  if x != 0:
    short_prefix = ones[x] + hundreds
    prefix = ones[x] + hundreds + joins
    num_list.append(ones[x] + hundreds)
  else:
    short_prefix = '' 
    prefix = '' 
  for i in range(1,101):
    if i <= 10:
      num_list.append(prefix + ones[i])
    if 10 < i < 20:
      num_list.append(prefix + teens[(i % 10)])
    if 20 <= i < 100:
      if i % 10 == 0:
        num_list.append(prefix + tens[math.trunc(i / 10)])
      else:
        num_list.append(prefix + tens[math.trunc(i / 10)] + ones[(i % 10)])
  return num_list

for i in range(0,10):
  master_list.extend(hundred(i))

master_list.extend(["onethousand"])

total = 0

for number in master_list:
  total += len(number)
  print number,str(total)

print total
