# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=12
# @author liekkas.zeng
# @date 2012-6-18 17:13:43
import math
import time

#方法一：虽然求出了结果，但用时过多  76576500 6.84899997711

start = time.time()

def calcNumOfFactors(v):
	count = 0
	for x in xrange(1,int(math.sqrt(v))+1):
		if v % x == 0:
			count += 2
	return count

n = 1
while n:
	v = int(n*(n+1)*0.5) 
	if calcNumOfFactors(v) > 500:
		print v,time.time() - start
		break
	n += 1

#方法二：在论坛里看到这个方法，超级快啊,  Result: 76576500   0.0891316602373
def sieve_of_eratosthenes(max_number):
    primes = range(2, max_number)
    
    for prime in primes:
        if(prime):
            for multiples in range(prime**2, max_number, prime):
                primes[multiples - 2] = False

    return [prime for prime in primes if prime]

#根据素数求因子个数
def number_of_divisors(number, primes):
    exponents = []
    
    for prime in primes:
        
        exponents.append(0)
        
        while number % prime == 0:
            number /= prime
            exponents[-1] += 1
    
    result = 1
    
    for exponent in exponents:
        result *= (exponent + 1)
        
    return result        


if __name__ == '__main__':
    '''
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th
    triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    Let us list the factors of the first seven triangle numbers:
         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.
    
    What is the value of the first triangle number to have over five hundred divisors?
    '''
    
    start = time.clock()
    
    desired_number_of_divisors = 500
    
    max_primes = sieve_of_eratosthenes(int(desired_number_of_divisors**0.5))

    for n in range(1, 100000):
        triangle_number = n * (n + 1) / 2
        
        if(number_of_divisors(triangle_number, max_primes) > desired_number_of_divisors):
            break
    
    print('Result: %s\nElapsed time: %s' %(triangle_number, time.clock() - start))