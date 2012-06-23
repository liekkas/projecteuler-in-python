# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=22
# @author liekkas.zeng
# @date 2012-6-21 10:39:03
# 原题：p22.txt里面有5000个名字，先排序这些名字，然后求名字的权重
# 权重算法：比如COLIN,字母换成数字后相加得分为： 3 + 15 + 12 + 9 + 14 = 53
# 另外它处在第938位，然后COLIN的最后得分为938*53 = 49714.
# 思路：貌似没什么复杂的，直接读取排序，求解，这里用到ord-64来获取数字，真是方便
f = open('p22.txt','r')
r = f.read().replace("\"","").split(",")
# r = eval('[' + open('p22.txt').read() + ']') #第二种读取方法
f.close()

def count_score(v):
	m = 0
	for c in v:
		m += ord(c)-64
	return m

r.sort()
result = 0
for x in xrange(0,len(r)):
	result += (x+1)*count_score(r[x])

print result	