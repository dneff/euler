#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# Comparing two numbers written in index form like 2**11 and 3**7 is not difficult,
# as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187. However,
# confirming that 632382**518061 > 5194325**25806 would be much more difficult, as
# both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
# containing one thousand lines with a base/exponent pair on each line, determine
# which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.
#
# this felt like some log thing, but wasn't sure of the relationship
# reviewing wikipedia logarithm and natural logarithm articles yielded success
#

import math,sys
import string

fh = open('./p99-base_exp.txt','r')

pairs = map(string.strip,fh.readlines())

line = 0
winner = [0,0]
for pair in pairs:
    line += 1
    base,exponent = pair.split(',')
    log_result = float(exponent) * math.log(float(base))
    if log_result > winner[0]:
        winner = [log_result, line]

print winner[1]