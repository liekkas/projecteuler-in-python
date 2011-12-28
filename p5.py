# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=5
# @author liekkas.zeng
# @date 2011.12.28

# 解1、纯数学方法：
# 根据standard factored form定义，每个整数都能表达成以下形式：
#     n = p1^e1*p2^e2*p3^e3*...pk^ek 
# 其中(n>1;p1,p2,p3,...pk是素数;e1,e2,e3...ek都是正整数;p1<p2<p3<...<pk)
# 首先看1-10：
#             2 = 2^1
#             3 = 3^1
#             4 = 2^2
#             5 = 5^1
#             6 = 2^1*3^1
#             7 = 7^1
#             8 = 2^3
#             9 = 3^2 
#            10 = 2^1*5
# 取最高的幂，所以1-10的最小公倍数就是：2^3 * 3^2 * 5 * 7 = 2520
# 同理：容易得知，11-20这几个数中素数有11、13、17、19，合数里只有16 = 2^4的幂
# 比8多一，所以求1-20的最小公倍数 = 2520 * 11 * 13 * 2 * 17 * 19 = 232,792,560 

# 解2、通过程序算最小公倍数
import mymath 
def main():
    result = 1
    for i in range(1,21):
        result = mymath.lcm(result,i)
    print result  # 232792560

if __name__ == "__main__":
    main()


