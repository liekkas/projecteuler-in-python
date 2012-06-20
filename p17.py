# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=17
# @author liekkas.zeng
# @date 2012-6-20 9:45:58
# 问题：假如把数字1-5写成英文：one,two,three,four,five，那么用到了3+3+5+4+4=19个字符
# 若1-1000写成英文，要用到多少个字符
# 思路一：笔算
# 1首先是1到9的总长度=3+3+5+4+4+3+5+5+4=36，然后是10到19总长度=3+6+6+8+8+7+7+9+8+8=70，
# 接着从20到99都有规律可循了，20到90所有10倍数的单词总长度=6+6+5+5+5+7+6+6=46，而个位都是1到9，
# 于是1到99的总长度=36×9+70+46×10=854。伴随1到999，1到99总是一轮轮出现的，总次数是10次，
# 因此十位和各位总长度=854×10=8540。接下来就是百位了，百位有点麻烦，虽然是1到9数字每个各出现了100次，
# 但是还有单词"hundred"，此外还有"and"，但是不影响计算，百位总长度=36×100+7×900+3×9×99=12573。
# 于是就得到了1到999的总长度=8540+12573=21113。最后加上单词"onethousand"，
# 那么我们得到的答案=21113+11=21114

# 思路二，预先一字典，把不同的字符加进来
D = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
    11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
    19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
  1000:"onethousand"}

for x in xrange(1,1000):
	if x not in D.keys():
		if x < 100: #21-99之间非10的倍数的数，如24 = 24/10*10 + 24%20 = 24
			D[x] = D[x//10*10]+D[x%10]
		else: #100-999的情况，如234 = 2 + hundred and 34
			D[x] = D[x//100]+'hundred'
			if x%100:
				D[x] += 'and' + D[x%100]
print sum(map(len,D.values()))				
