#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# The nth term of the sequence of triangle numbers
# is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number
# corresponding to its alphabetical position and adding 
# these values we form a word value. For example, the
# word value for SKY is 19 + 11 + 25 = 55 = t10. If
# the word value is a triangle number then we shall call
# the word a triangle word.
#
# Using p042-words.txt, a 16K text file containing nearly
# two-thousand common English words, how many are triangle words?
#
import math,sys,string

fh = open('./p042-words.txt','r')

words = map(string.strip,fh.readlines())
words = sorted(words[0].replace('"','').split(','))


alphabet = {}
for c in string.ascii_uppercase:
  alphabet[c] = (len(alphabet.keys()) + 1)

word_sums = []

for word in words:
  word_sum = 0
  for letter in list(word):
    word_sum += alphabet[letter]
  word_sums.append(word_sum)

word_sums.sort()

triangles = []
for n in range(1,word_sums[-1]):
  triangle = (n  * (n + 1)) / 2
  if triangle > word_sums[-1]:
    break
  else:
    triangles.append(triangle)

solution = 0
for x in word_sums:
  if x in triangles:
    solution += 1

print solution

