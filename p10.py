# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=10
# @author liekkas.zeng
# @date 2012-6-16 16:45:44
#求和：200,0000以内的素数之和

from mymath import findPrimers,isPrimer,findPrimerByIndex

print sum(findPrimers(2000000))		
