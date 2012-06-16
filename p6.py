# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=6
# @author liekkas.zeng
# @date 2012-6-15 17:55:30
#
# 问题：前10个自然数的平方和为：1^2 + 2^2 + ... + 10^2 = 385
#       前10个自然数的和平方为：(1+2+...+10)^2 = 55^2 = 3025
#       两者相差3025 - 385 = 2640
# 求：前100个自然数的和平方与平方和之间的差值
from mymath import sumSquares,squaresSum

print(sumSquares(1,101) - squaresSum(1,101))