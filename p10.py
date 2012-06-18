# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=10
# @author liekkas.zeng
# @date 2012-6-16 16:45:44
#求和：200,0000以内的素数之和

from mymath import findPrimers,isPrimer,findPrimerByIndex

print sum(findPrimers(2000000))		

#网上找的第二种筛选方法实现
def sieve_method(num):
    prime_data = [x for x in xrange(num + 1)]
    for i in xrange(2,int(math.sqrt(num) + 1)):
        if prime_data[i]:
            start = i**2
            step  = i
            prime_data[start::step]=((num-start)/step + 1) * [0]
    print sum(prime_data) -1#1 is not prime number