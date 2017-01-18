#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime
import time
from collections import defaultdict

def nesteddict():
	return defaultdict(nesteddict)

timeList = ['20050531','20050831','20051130','20060331',\
	'20060531','20060831','20061130','20070330',\
	'20070531','20070831','20071130','20080331',\
	'20080530','20080829','20081128','20090331',\
	'20090529','20090831','20091130','20100331',\
	'20100531','20100831','20101130','20110331',\
	'20110531','20110831','20111130','20120331',\
	'20120531','20120831','20121130','20130331',\
	'20130531','20130831','20131130','20140331',\
	'20140531','20140831','20141130','20150331',\
	'20150531','20150831','20151130','20160331',\
	'20160531','20160831','20161130']


if __name__ == '__main__':
	large_dict = nesteddict()
	cur_path = os.getcwd()
	par_path = os.path.dirname(cur_path)
	raw_file_names = os.listdir(par_path+'/data')
	csv_file_names = filter(lambda x:x.endswith('.csv'),raw_file_names)

	attr_list = ['code','date','tot_asset','tot_liab'\
				,'roe','ato','gpm','roa','p2b','cur_tmv','cur_cmv','cls_price','revenue']
	attr_list2 = ['code','date','p2b','cur_tmv','cur_cmv']
	#code time  ann_dt rep_prid tot_asset  tot_liab roe roa b2p  cur_tmv cur_cmv revenue
	i = 0
	for file in csv_file_names:
		read_path = par_path+'/data/'+file
		print read_path
		data = pd.read_csv(read_path)
		if i == 0:
			pass
			# for j in range(data.shape[0]):
			# 	code = str(data.iloc[j,0])
			# 	date = str(data.iloc[j,2])
			# 	large_dict[code][date]['date'] = date
			# 	large_dict[code][date]['code'] = code
			# 	# large_dict[code][date]['tot_asset'] = str(data.iloc[j,4])
			# 	# large_dict[code][date]['tot_liab'] = str(data.iloc[j,5])
		elif i == 1:
			pass
			# for j in range(data.shape[0]):
			# 	code = str(data.iloc[j,0])
			# 	date = str(data.iloc[j,2])
			# 	large_dict[code][date]['date'] = date
			# 	large_dict[code][date]['code'] = code
			# 	large_dict[code][date]['roe'] = str(data.iloc[j,3])
			# 	large_dict[code][date]['ato'] = str(data.iloc[j,4])
			# 	large_dict[code][date]['gpm'] = str(data.iloc[j,5])
			# 	large_dict[code][date]['roa'] = str(data.iloc[j,6])

		elif i >=2 and i<9:
			j=0
			for j in range(data.shape[0]):
				date = str(data.iloc[j,1])
				if date in timeList:
					code = str(data.iloc[j,0])
					large_dict[code][date]['date'] = date
					large_dict[code][date]['code'] = code
					large_dict[code][date]['p2b'] = data.iloc[j,2]
					large_dict[code][date]['cur_tmv'] = data.iloc[j,3]
					large_dict[code][date]['cur_cmv'] = data.iloc[j,4]
				# large_dict[code][date]['cur_tmv'] = str(data.iloc[j,3])
				# large_dict[code][date]['cur_cmv'] = str(data.iloc[j,4])
				# large_dict[code][date]['cls_price'] = str(data.iloc[j,5])

		else:
			pass
			# for j in range(data.shape[0]):
			# 	code = str(data.iloc[j,0])
			# 	date = str(data.iloc[j,2])
			# 	large_dict[code][date]['date'] = date
			# 	large_dict[code][date]['code'] = code
			# 	large_dict[code][date]['revenue'] = str(data.iloc[j,4])
		i+=1


	largeData = pd.DataFrame(columns = attr_list2)
	i = 0
	print 'forming dataframe...'
	for (k,v) in large_dict.items():
		outData = pd.DataFrame(columns = attr_list2)
		for (kk,vv) in v.items():
			outData = outData.append(vv,ignore_index = True)
		largeData = largeData.append(outData)
		i+=1
	
	print 'sorting...'
	largeData = largeData.sort_values(by = ['date','code'],ascending = [1,1])
	
	print 'groupbying...'
	gb = largeData.groupby('date',sort = False)
	#largeData.to_csv(index = False,path_or_buf = './result2/'+'inter.csv')
	for name,group in gb:
		group.to_csv(index = False,path_or_buf = './result3/'+name+'.csv')

