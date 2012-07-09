# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=25
# @author liekkas.zeng
# @date 2012-6-21 17:54:42
# 找出第一位上千的Fibonacci数列
from mymath import findFibonacciByIndex
from itertools import count
for x in count(100):
	if len(str(findFibonacciByIndex(x))) > 1000:
		print x
		break

# 思路2：
li = [1, 1]
while 1:
    li.append(li[-2] + li[-1])
    if len(str(li[-1])) >= 1000:
        print len(li)
        break	

# 思路3：
a = 1
b = 1
pos = 2
while len(str(b)) != 1000:
    a, b = b, a + b
    pos += 1
print pos        