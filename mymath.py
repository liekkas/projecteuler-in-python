# -*- coding:utf-8 -*- 
#常用数学工具

#求两个整数的最大公约数
def gcd(a,b):
    if a<=0 or b<=0:
        return -1;
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

    
    
