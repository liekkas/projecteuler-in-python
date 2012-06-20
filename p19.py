# -*- coding:utf-8 -*-
# 原题连接: http://projecteuler.net/problem=19
# @author liekkas.zeng
# @date 2012-6-20 11:16:22
import datetime

print len([datetime.date(year,month,1) for year in xrange(1901,2001) for month in xrange(1,13) 
	if datetime.date(year,month,1).weekday()==6])