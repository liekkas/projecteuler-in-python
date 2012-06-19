# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=13
# @author liekkas.zeng
# @date 2012-6-19 9:34:29
# 求和100个50位的数，然后找出前10个数字是多少
# 思路：直接保存为文本，然后直接求，貌似过于简单了
f = open('p13.txt','r')
print str(sum(map(int,[t for t in f])))[:10]