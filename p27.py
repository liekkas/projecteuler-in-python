# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=27
# @author liekkas.zeng
# @date 2012-6-28 10:20:57
# 问题：

# I did not use a computer to solve this problem.
# The formula n^2-79n+1601 is nothing more than (n-40)^2+n-40+41 
# so that all the forty primes of n^2+n+41 are met twice that's why 80 primes are found, but only 40 different one's.
# So what I did was:
# take (n-p)^2+n-p+41, working out this formula gives:
# n^2-(2p-1)n+p^2-p+41.
# Now |2p-1|<1000 and |p^2-p+41|<1000.
# The second condition gives -30<=p<=31
# The value p=31 gives the most primes.
# So the numbers are -(2*31-1)=-61 and 31^2-31+41=971.
# See also: http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html		
import time
#解法2
t2 = time.time()
SIEVE_SIZE = 4096

def primes():
    s = [False] * 2 + [True] * (SIEVE_SIZE - 2)
    primel = []

    # Bootstrap sieve
    for i in xrange(SIEVE_SIZE):
        if s[i]:
            yield i
            primel.append(i)
            j = i
            while j < SIEVE_SIZE:
                s[j] = False
                j += i

    # Main loop
    seg = SIEVE_SIZE
    while True:
        s = [True] * SIEVE_SIZE
        for p in primel:
            j = (seg / p) * p - seg
            if j < 0:
                j += p
            while j < SIEVE_SIZE:
                s[j] = False
                j += p

        # Yield next set of primes
        for p in map(lambda x: x[0], filter(lambda x: x[1],
                enumerate(s, seg))):
            yield p
            primel.append(p)

        seg += SIEVE_SIZE

pg = iter(primes())
test_primes = []

p = next(pg)
while p < 1000:
    test_primes.append(p)
    p = next(pg)

ps = set(test_primes)
ps.add(p)
pm = p

def is_prime(n):
    global pm
    while pm < n:
        pm = next(pg)
        ps.add(pm)
    return n in ps

def get_formula_length(a, b):
    n = 1
    t = lambda n: n * n + a * n + b

    while t(n) > 0 and is_prime(t(n)):
        n += 1

    return n

print max((get_formula_length(a, b), a * b) for b in test_primes
    for a in xrange(-999, 1000))[1],time.time()-t2


# 解法3，速度最快了
from math import sqrt
t3 = time.time()
def primes_upto(n):
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, int(sqrt(n))+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    return [x for x in sieve if x !=0]


primes = primes_upto(300000)
pset = set(primes)
pos_primes = [i for i in primes if i < 1000]
abs_primes = [-i for i in pos_primes] + pos_primes

max_n = 0
max_m = ()
for b in pos_primes:
    for a in abs_primes:
        if a >= b: continue
        if abs(a)      not in pset: continue
        if (a + b + 1) not in pset: continue

        n = 0
        while (n * n + a * n + b) in pset:
            n += 1
            
        if n > max_n:
            max_n, max_m = n, (a,b)

print max_m, max_n,'=', max_m[0] * max_m[1],time.time()-t3
