#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# Using names.txt, a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then
# working out the alphabetical value for each name, multiply
# this value by its alphabetical position in the list to obtain
# a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list.
#
# So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?
#

import string,math,sys

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letter_score = {}
for i in range(0,len(letters)):
  letter_score[letters[i]] = i + 1

def namescore(rank,name):
  sum = 0
  for letter in list(name):
    sum += letter_score[letter]
  return rank * sum

fh = open('./p022-names.txt','r')

names = map(string.strip,fh.readlines())
names = sorted(names[0].replace('"','').split(','))

sum_of_names = 0

for i in range(0,len(names)):
  rank = i + 1
  sum_of_names += namescore(rank,names[i])

print sum_of_names
