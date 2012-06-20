# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=20
# @author liekkas.zeng
# @date 2012-6-20 11:23:56
# 求100！的各数字之和
# 思路：直接拿起python就上啊
print sum(map(int,str(reduce(lambda x,y:x*y,xrange(1,101)))))