# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=67
# @author liekkas.zeng
# @date 2012-6-20 17:40:44
# 思路同p18,代码一样
import string
f = open('p67.txt','r')
r = []
for line in f:
	r.append(map(int,string.strip(line).split(" ")))
f.close()

r.reverse()
for x in xrange(0,len(r)-1):
	for y in xrange(0,len(r[x+1])):
		r[x+1][y] = max(r[x][y]+r[x+1][y],r[x][y+1]+r[x+1][y])

print r[len(r)-1]