#!/usr/bin/env python3
import pandas as pd

input_file = './goods_data_no_header_row.csv'
output_file = './goods_output_by_pandas.csv'


#使用pandas为表格添加标题行
header_list = ['货品名称','款号','实际成本','标签价']
data_frame = pd.read_csv(input_file,header=None,names=header_list,encoding='gbk')           #在读取文件时加上name，即首行
data_frame.to_csv(output_file)


#本节新内容：name属性，即首行
