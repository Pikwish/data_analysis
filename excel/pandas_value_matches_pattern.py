#!/usr/bin/env python3
import pandas as pd
from re import findall


#使用正则表达式和pandas将匹配特定模式的数据筛选出来

input_file = './xls_files/2.xls'
output_file = './xls_files/pandas_output.xls'


#要求：将条形码开头为‘180211’的所有记录筛选出来
data_frame = pd.read_excel(input_file,sheet_name='素金入库')
result = data_frame[data_frame['货品名称'].str.startswith('足银999')]             #startswith方法为开头，相对应的为endswith
writer = pd.ExcelWriter(output_file)
result.to_excel(writer)
writer.save()
