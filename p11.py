# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=9
# @author liekkas.zeng
# @date 2012-6-18 14:46:01
# 原题：在20*20的矩阵中找出连续4个数字相乘最大的数，这个连续可以使水平的、垂直的、对角的
# 我的思路，转换成一个个4*4矩阵，有10种相乘方式，再求其中最大值
import string
import time

start = time.time()
W,H = 20,20

#存为文本转换成二维列表
def initTxt():
	gridFile = open('p11.txt','r')
	gridList = []
	for line in gridFile:
		lineList = string.strip(line).split(" ")
		gridList.append(map(int,lineList))
	return gridList

#把原数据生成一个个4格矩阵
def generate4Grids(v):
	all4Grids = []
	for w in xrange(0,W-3):
		for h in xrange(0,H-3):
			t = []
			t.append(v[w][h:h+4])
			t.append(v[w+1][h:h+4])
			t.append(v[w+2][h:h+4])
			t.append(v[w+3][h:h+4])
			all4Grids.append(t)
	return all4Grids

# print all4Grids

#分解成4*4的小矩阵，一共有10种可能的相乘方式
def calcGrid(grid):
	r = 0
	s = []
	for x in xrange(0,4):
		s.append([grid[x][0],grid[x][1],grid[x][2],grid[x][3]])
		s.append([grid[0][x],grid[1][x],grid[2][x],grid[3][x]])
	s.append([grid[0][0],grid[1][1],grid[2][2],grid[3][3]])
	s.append([grid[0][3],grid[1][2],grid[2][1],grid[3][0]])

	for item in s:
		r = max(reduce(lambda m,n:m*n,item),r)
	return r

if __name__ == "__main__":
	grids = generate4Grids(initTxt())
	result = 0
	for grid in grids:
		result = max(calcGrid(grid),result)
	print result, time.time()-start

