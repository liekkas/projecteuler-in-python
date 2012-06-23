# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=21
# @author liekkas.zeng
# @date 2012-6-21 9:00:45
# 问：求10000内亲和数之和
# 知识：amicable numbers http://en.wikipedia.org/wiki/Amicable_numbers
# 数列在oeis上 http://oeis.org/A063990，
# 另见：http://mathworld.wolfram.com/AmicablePair.html，http://primes.utm.edu/glossary/page.php?sort=AmicableNumber
# 思路一：直接google这个数列，http://oeis.org/A063990，
# 	220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595,
#   17296, 18416, 63020, 66928, 66992, 67095, 69615, 71145, 76084, 79750, 87633, 88730....
print sum([220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368])

#思路二：找到因子之和，然后判断是否为亲和数，31626，速度1s以内
from mymath import findFactors

r = 0
for x in xrange(220,10000):
	s = sum(findFactors(x))
	t = sum(findFactors(s))
	if t == x and s != x:
		r += x
print r