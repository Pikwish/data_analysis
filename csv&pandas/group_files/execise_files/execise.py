#!/usr/bin/env python3
#-*- coding:utf8 -*-
import os
import glob
import pandas as pd




#练习：将所有文件合并生成到一个新的csv文件


input_path = './'
output_file = '../execise_output/output_file.csv'


all_files = glob.glob(os.path.join(input_path,'*.csv'))
data_frame = []
for file in all_files:
    data = pd.read_csv(file,encoding='gbk')
    data_frame.append(data)
print(data_frame)


