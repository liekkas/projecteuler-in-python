# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=23
# @author liekkas.zeng
# @date 2012-6-21 11:13:03
# 完美数：其因子之和为其本身的数，如28 -> 1 + 2 + 4 + 7 + 14 = 28
# 不足数：其因子之和小于其本身的数，如4 -> 1 + 2 = 3
# 多余数：其因子之和大于其本身的数，如12 ->  1 + 2 + 3 + 4 + 6 = 16
# 最小的多余数就是12，最小的能表达成两个多余数的数字是24，数学分析表明：
# 所有大于28123的数都可以写成两个多余数之和。
# 问题：找出所有不能写成两个多余数之和的数，然后相加求值？
# 思路1：蛮力求解，先找出所有的多余数，然后再两两相加存放到d，遍历1-28123，如果不在d就符合要求，最后求和，但太慢

# 思路2：不必先刻意求多余数，直接遍历，因为这个数既然能由两个多余数组成，
# 那么设a为其中一个多余数，x-a则为另外一个多余数，只要一个满足就行，
# 核心算法：if not any((x-a) in abundants for a in abundants): 大概3s左右
# 另外python里set()比list貌似高效很多啊
from mymath import findFactors

r = 0
abundants = set()
for x in xrange(1,28123):
	if x < sum(findFactors(x)):
		abundants.add(x)
	if not any((x-a) in abundants for a in abundants):
		r += x

print r
