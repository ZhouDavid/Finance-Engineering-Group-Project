#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import sys
import os


def write_out(dir,name,data):
	out_path = dir+'/'+name
	pass
def extract(data,num):
	small = data.iloc[range(num),:]
	return small

if __name__ == '__main__':
	cur_path = os.getcwd()
	par_path = os.path.dirname(cur_path)
	data_dir = par_path+'/data'
	raw_file_names = os.listdir(data_dir)
	csv_file_names = filter(lambda x:x.endswith('.csv'),raw_file_names)
	out_dir = par_path+'/data/small_set'
	#code time  ann_dt rep_prid tot_asset  tot_liab roe roa b2p  cur_tmv cur_cmv revenue
	i = 0
	for file in csv_file_names:
		print i
		data = pd.read_csv(data_dir+'/'+file)
		df = extract(data,10)
		name = 'small_'+file
		outpath = out_dir+'/'+name
		print outpath
		df.to_csv(index = False,path_or_buf = outpath)
		i+=1
	# df = pd.read_csv('../data/balancesheet_05_15.csv')
	# print df