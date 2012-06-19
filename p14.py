# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=14
# @author liekkas.zeng
# @date 2012-6-19 9:51:58
#思路一：暴力求解  不过效果太差，用了快三分钟 525 837799 163.495000124s
import time

start = time.time()

def rule_even(n):
	return int(n*0.5)

def rule_odd(n):
	return 3*n+1

r = []
def generate(n):
	
	if n == 1:
		return [1]
	elif n%2 == 0:
		n = rule_even(n)
	else:
		n = rule_odd(n)

	r.append(n)	
	generate(n)
	return r

m = 0
result = 0
for x in xrange(2,1000000):
	i = len(generate(x))+1
	if i > m:
		m = i
		result = x
	r = []		

print m,result,time.time()-start

#思路二：使用缓存,因为到1的路径是一致的，比如你算出来
#2 = [2,1]
#3 = [3,10,5,16,8,4,2,1]
#4 = [4,2,1]  看到没有，这里实际上在3的情况中已经算出来了，没必要重复计算，
#基于这一思路，能把时间缩短到4s
cache = {}
def collatz_sequence_len(n):
    if n == 1: return 1
    if n in cache: return cache[n]
    
    r = None #执行的次数就是路径长度
    if n % 2 == 0: 
        r = 1 + collatz_sequence_len(n / 2)
    else: 
        r = 1 + collatz_sequence_len(3 * n + 1)
    
    cache[n] = r
    return r

m = 0
max_n = 0

for n in xrange(1, 1000000):
    r = collatz_sequence_len(n)
    if r > m:
        m = r
        max_n = n
        
print max_n