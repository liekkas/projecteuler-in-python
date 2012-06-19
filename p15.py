# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=15
# @author liekkas.zeng
# @date 2012-6-19 9:51:58
# 思路：见http://mathschallenge.net/full/random_routes，这个就是帕斯卡三角形算法啊
# 知识：http://en.wikipedia.org/wiki/Binomial_coefficient  用到了二项式系数
# 这类题都有现成的公式 (R+C)! / R! * C!  其中R是行数，C是列数，所以这里是(20+20)! / 20! * 20!
# 号外：这个数列就是http://oeis.org/A001405，名叫Central binomial coefficients: C(n,floor(n/2)).

# 另外见一个论坛上的解释：
# If you think about it, you need to move 20 right and 20 down in any order. 
# You just need to find all the ways you can arrange 20 rights and 20 downs. 
# If we think of them as elements, we have 40 of them. 20 of them being R,
# and 20 of them being D. Say you have one combination. Swapping any of 
# the D's with each other will give you the same combination; same thing with R's.
# So first, you have 40! ways you can arrange them. There are 20! ways that you can arrange 
# the R's and 20! ways you can arrange the D's. Dividing 40! by each of these should give the answer:
# 40!/(20!*20!) = 137846528820

print reduce(lambda x,y:x*y,xrange(1,41))/((reduce(lambda x,y:x*y,xrange(1,21)))**2)

