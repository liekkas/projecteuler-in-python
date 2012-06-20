# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=16
# @author liekkas.zeng
# @date 2012-6-20 9:31:44
# 2^15 = 32768，各数字之和为3+2+7+6+8=26，求2^1000的各数字之和
# 思路：用左移，轻松解决
print sum(map(int,str(2 << 999)))
