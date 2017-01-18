#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import time
import math
# start_date = datetime.strptime('20100101','%Y%m%d')
# end_date = datetime.strptime('20151201','%Y%m%d')
timeList = ['20050531','20050831','20051130','20060331',\
	'20060531','20060831','20061130','20070330',\
	'20070531','20070831','20071130','20080331',\
	'20080531','20080831','20081130','20090331',\
	'20090531','20090831','20091130','20100331',\
	'20100531','20100831','20101130','20110331',\
	'20110531','20110831','20111130','20120331',\
	'20120531','20120831','20121130','20130331',\
	'20130531','20130831','20131130','20140331',\
	'20140531','20140831','20141130','20150331',\
	'20150531','20150831','20151130','20160331',\
	'20160531','20160831','20161130']

def day_plus(date):
	std_date = date+timedelta(days=90)
	return std_date
def time2int(date):
	return date.strftime("%Y%m%d")
def extract(data,spercent,epersent):
	total_rows = data.shape[0]
	begin_index = int(math.floor(total_rows*spercent))-1
	end_index = int(math.ceil(total_rows*epersent))+1
	return data.iloc[begin_index:end_index,:]
def trans(date):
	date = str(date)
	year = date[0:4]
	month = date[4:6]
	day = date[6:8]
	return year+'/'+month+'/'+day
def intercept(code):
	print code[0:6]
	return code[0:6]

if __name__ == '__main__':
	attr_list = ['time','code','weight']
	portfolio = pd.DataFrame(attr_list)

	for time in timeList:
		filename = './result3/'+time+'.csv'
		try:
			cur_data = pd.read_csv(filename)
			cur_data = cur_data.sort_values(by='p2b',ascending = False)
			top_p2b = extract(cur_data,0,0.1)		#取出前10%
			bottom_p2b = extract(cur_data,0.9,1)
			candidate = top_p2b.append(bottom_p2b)
			sum = candidate['cur_tmv'].sum()
			weight = candidate['cur_tmv'].apply(lambda x:(x/sum)*100)
			date = candidate['date'].apply(lambda x:trans(x))
			code = candidate['code'].apply(lambda x:intercept(x))
			tmp = pd.DataFrame({'code':code,'date':date,'weight':weight})
			portfolio = portfolio.append(tmp,ignore_index = True)
		except:
			print filename +'not found'
	portfolio.to_csv(index = False,path_or_buf = './result3/'+'port3.csv')