# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=9
# @author liekkas.zeng
# @date 2012-6-16 16:32:40
# 勾股数a,b,c满足：a<b<c  a^2 + b^2 = c^2
# 已知：a+b+c = 1000 求a*b*c

#方法一：程序直接求解
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a+b+c == 1000 and a+b>c:
                if (a**2) + (b**2) == (c**2):
                    print a*b*c
#方法二：搞懂勾股数的规律
#勾股定理的规律  a=m^-n^,b=2mn,c=m^+n^
# 
# 按此思路如下：
# a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
# a + b + c = 1000;

# 2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
# 2mn + 2m^2 = 1000;
# 2m(m+n) = 1000;
# m(m+n) = 500;

# m>n;

# m= 20; n= 5;

# a= 200; b= 375; c= 425; 
# 故：a*b*c = 200*375*425 = 31875000
