# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=24
# @author liekkas.zeng
# @date 2012-6-21 15:55:29
# 字典排序：如0,1,2 按字典排序为：012,021,102,120,201,210
# 问题：求0,1,2,3,4,5,6,7,8,9组合的排序中第1000000个数字是多少？

# 思路1：论坛看到一哥们手算出来了，牛b 
# Let's enumerate the permutations starting with index 0. Then were going to find the permutation with index 999999.
# The  permutation with index 0 is 0123456789.

# We shall also enumerate the digits "available for use" in the same way, i.e. starting with index 0. 
# At the beginning, those digits will be 0123456789 (in that order).

# We now write 999999 = 2 * 9! + 274239.
# The quotient 2 gives the index (in 0123456789) of the first digit: 2.
# Remove that digit from the available digits: 013456789.

# Next, we write 274239 = 6 * 8! + 32319.
# The quotient 6 again gives the index (now in 013456789) of the second digit: 7.
# Remove that digit from the available digits: 01345689.

# Continue in this way, dividing by n!, until (including) n=0.
# The quotients will be (from the beginning): 2, 6, 6, 2, 5, 1, 2, 1, 1 and 0, giving the 
# digits 2, 7, 8, 3, 9, 1, 5, 4, 6 and 0.

# The searched-for permutation thus is: 2783915460.

# 思路2：速度嗖嗖的
n=1000000-1
seq = list('0123456789')
idx = []
ret = ''
for d in range(1, len(seq)+1):
    idx = [n%d] + idx
    n = n/d
for i in idx:
    ret += str(seq.pop(i))
print ret

# 思路3：
from math import factorial
lst = range(0,10)
fac = [factorial(i) for i in range(9,0,-1)]
t = 1000000
result=[]
for k, i in enumerate(range(9,0,-1)):
    idx = t/fac[k]
    if t%fac[k] == 0:
        idx -= 1
    result.append( lst.pop(idx))
    t -= idx*fac[k]
result.append( lst[0])
print ''.join(str(i) for i in result)

# 思路4，Python内置方法，比上面两个慢了点
from itertools import permutations as perm
from string import digits

print ''.join(list(perm(digits))[999999])

# 另外一个用内置方法解决的
from itertools import permutations, islice
print next(islice(permutations("0123456789"), 999999, 999999 + 1))