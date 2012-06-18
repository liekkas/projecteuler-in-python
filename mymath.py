# -*- coding:utf-8 -*- 
#常用数学工具
import math

#求两个整数的最大公约数
def gcd(a,b):
    if a<=0 or b<=0:
        return -1
    if a < b:
        t = a
        a = b
        b = t
    while b:
        t = b
        b = a%b
        a = t
    return a

#求最小公倍数
def lcm(a,b):
    return a*(b/gcd(a,b))

#判断是否是吸血鬼数字 如1827=21*87
#所谓“吸血鬼数字”就是指位数为偶数的数字(我们算得是4位的)，可以由一对数字相乘而得到，
#而这对数字各包含乘积的一半位数字，其中从偶数位数字中选取的数字可以任意排列。以两个0截尾的数字是不允许的
# def isVampire(n):
#     stringN = %d%n
#     if len(stringN)%2!=0:
#         return false

#求某一区间的和平方
def sumSquares(begin,end):
    return reduce(lambda x,y:x+y,xrange(begin,end))**2

#求某一区间的平方和
def squaresSum(begin,end):
    return sum(map(lambda x:x**2,xrange(begin,end)))    

# 求指定值以内[不包括该值]的所有素数，返回list
# 采用Sieve of Eratosthenes算法，效果较高
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# 求质数最经典的方法是Eratosthenes筛选法，一般都是利用一个布尔数组作为筛选器，将下标作为目标数，
# 元素作为该目标是否为质数的标志，并且对于给定范围1~n之间的数，只需要筛选掉1到sqrt(n)之间的质数的所有倍数，
# 剩下的就都是质数了。
def findPrimers(max_number):
    primes = range(2, max_number)
    
    for prime in primes:
        if(prime):
            for multiples in range(prime**2, max_number, prime):
                primes[multiples - 2] = False

    return [prime for prime in primes if prime]

#判断某个值是否是素数
def isPrimer(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    i = 3
    range = int( math.sqrt(n) ) + 1
    while( i < range ):
        if( n % i == 0):
            return False
        i += 1
    return True

#求第几个素数
def findPrimerByIndex(index):
    if index < 2:
        return 2
    N,T = 1,3
    while N < index:
        if isPrimer(T):
            N+=1
        T+=2 
    return T-2

    


    
    
