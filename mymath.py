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

#求素数
def findPrimeByIndex(index):
    count = 0
    i = 2
    while i > 0:
        if isPrime(i):
            count += 1
        if(count == index):
            return i
        i += 1   

#判断是否是素数
def isPrime(number):
    if number < 2:
        return False;
    elif number == 2:
        return True;
    else:
        for x in range(2,int(math.sqrt(number))+1):
            if(number%x == 0):
                return False;
    return True;

    
    


    
    
