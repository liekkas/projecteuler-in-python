# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=18
# @author liekkas.zeng
# @date 2012-6-20 10:33:36
# 问题：求一个三角形顶到底最大的权重，具体见连接
# 思路：倒转三角形，然后从第二行开始记录最大的和值，逐行递进，最后存放的就是最大值
# 例如：  0：  2  4  3
#         1：    5  6
#  相加后 1： (7,9)(10,9) 
#  取最大 1：    9  10
#  从而第二行变成了 9  10，这样继续就是最大了
import string
f = open('p18.txt','r')
r = []
for line in f:
	r.append(map(int,string.strip(line).split(" ")))
f.close()

r.reverse()
for x in xrange(0,len(r)-1):
	for y in xrange(0,len(r[x+1])):
		r[x+1][y] = max(r[x][y]+r[x+1][y],r[x][y+1]+r[x+1][y])

print r[len(r)-1]