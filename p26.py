# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=26
# @author liekkas.zeng
# @date 2012-6-25 15:40:19
# 问题1到1000中的倒数小数点最多的是哪个数？循环的不算，如1/3=0.3333只算一位
import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            print r,i,seen  
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)
           

len,i = max((recur_len(i),i) for i in range(2,10))
print len,i
