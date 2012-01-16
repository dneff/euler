#!/usr/bin/python
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# first pass: prove prime for each number by testing 
# all previous primes. The ratio of primes was ~1:10 
# at least to 200000, so finding a prime this
# way meant comparing n to n/10 numbers. Oof...
#
# after doing it the hard way, read up on primes and 
# let go of the need to test every number. Eritosthenes
# was pretty badass, however loops are slow-- removing lists
# at a time may work better..
#
# still slow-- pretty much just as slow.
# going to try the bit array...
#
# first try not manipulating the global array correctly
# real sol'n:

max = 2000001

numbers = range(3,max,2)
primes = [2]

while numbers:
    primes.append(numbers[0])
    numbers = sorted(set(numbers) - set(range(0,max,numbers[0])))

print sum(primes)
