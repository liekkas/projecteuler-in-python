# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=8
# @author liekkas.zeng
# @date 2012-6-16 15:26:44
# 如下在1000位数字的字符串中找到连续5个数字，使得这5个数字乘积最大

# 思路一：首先排除有0和1的，然后找9开头的，生成含9的连续5个数字列表，再找到其中最大的乘积
# 代码多了点，但帮电脑少判断了很多

value = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

#返回最大值得乘积
def timesList(value):
    maxResult = 0
    for num in value:
        intList = []
        for i in num:
            intList.append(int(i))
        curResult = reduce(lambda x,y:x*y,intList)
        maxResult = max(maxResult, curResult)
    return maxResult

#找出某个字符在某个字符串中出现的位置
def findCharIndexs(v,char):
    result = []
    for x in range(len(v)):
        if(v[x] == char):
            result.append(x)
    return result

#生成不含0和1的列表
def generateList(v,idx,numOf):
    facts = []
    for index in idx:
        if index < numOf-1:
            idxStr = v[:index+numOf]
        else:
            idxStr = v[index-numOf-1:index+numOf]
        for x in xrange(numOf):
            fact = idxStr[x:x+numOf]
            if("0" not in fact and "1" not in fact):
                facts.append(fact)
    return facts

#通过此方法可以获得连续1到10最大数字的乘积
for x in xrange(1,10):
	print(x,timesList(generateList(value,findCharIndexs(value,"9"),x)))


#思路二：直接从头到尾进行判断
maxima = 0 
for i in range(0, len(value) - 5): 
    product = reduce(lambda x, y: x * y, [int(value[i+j]) for j in range(0, 5)])
    maxima = max(maxima, product)

print maxima	

#思路三：map(int,value[i:i+5]) 把字符串转换成int列表
p = 0
for i in range(0, len(value) - 4):
    p = max(reduce(lambda x, y: x * y, map(int, value[i:i+5])), p)
  
print p