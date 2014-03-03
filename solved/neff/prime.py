
# prime fun
import itertools, math, random, sys


# After tweaking the prime number generator a few dozen times, I wanted an iterator
# I looked at mine, then read through a bunch of efficiency articles.
# This one (while slower) was understandable by my half brain, meaning I would have got here
#
# http://stackoverflow.com/questions/2211990

def generator():
  primes = {}
  yield 2
  for q in itertools.islice(itertools.count(3), 0, None, 2):
    p = primes.pop(q, None)
    if p is None:
      primes[q*q] = q
      yield q
    else:
      x = q + 2*p
      while x in primes:
        x += 2 *p
      primes[x] = p


# prime number tester that is less than O(n)
# spent a couple days trying to follow the logic
def MillerRabinTest(x):
  base_test = 5
  if x == 2:
    return True
  if x % 2 == 0:
    return False
  s = 0
  d = x - 1
  while True:
    q, r = divmod(d, 2)
    if r == 1:
      break
    s+= 1
    d = q
  assert(2**s * d == x - 1)

  def try_composite(a):
    if pow(a, d, x) == 1:
      return False
    for i in range(s):
      if pow(a, 2**i * d, x) == x - 1:
        return False
    return True

  for i in range(base_test):
    a = random.randrange(2, x)
    if try_composite(a):
      return False
  return True

def is_prime(x):
  return MillerRabinTest(x)

def is_prime_old(x):
  for y in generator():
    if x == y:
      return True
    if x % y == 0:
      return False
    if x < y:
      return False

def smallest_factor(x):
  if is_prime(x): return x
  for prime in generator():
    if x % prime == 0: return prime

def factors(x):
  results = []
  if is_prime(x):
    results.append(x)
    return results
  f1 = smallest_factor(x)
  results.append(f1)
  f2 = x/f1
  if is_prime(f2):
    results.append(f2)
  else:
    for ff in factors(f2):
      results.append(ff)
  return results
