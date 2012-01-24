#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# 
# You are given the following information, but 
# you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible 
# by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month 
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#

import math,sys

# strat: there's a list of numbers which represent all the firsts
# of the month as the number of days since 1/1/1901. If any are
# divisible by seven, it's a Sunday.

# Part of me wants the most efficient path possible, the other
# wants to use objects that have the shape and feel of the text
# above. The text approach offers a satisfaction the efficient 
# solution doesn't. What's that say?

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ('January', 31), ('February', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)

leap_February = 29

start_year = 1900
end_year = 2000

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      return False
    return True
  else:
    return False

first_of_month = []
sum_of_days = 1 

for y in range(start_year,end_year + 1):
  for month in months:
    if month[0] == "February":
      if is_leap(y):
        sum_of_days += leap_February
        first_of_month.append(sum_of_days)
        continue
    if month[0] == "December":
      if y == end_year:
        continue
    sum_of_days += month[1]   
    first_of_month.append(sum_of_days)

solution = 0

for value in first_of_month:
  if value < 366:
    continue
  if value % 7 == 0:
    solution += 1

print solution
