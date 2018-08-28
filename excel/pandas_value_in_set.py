#!/usr/bin/env python3


import pandas as pd

#用pandas将工厂款号包含KB077的记录筛选出来

input_file = './xls_files/2.xls'
output_file = './xls_files/pandas_output.xls'

data_frame = pd.read_excel(input_file,sheet_name='素金入库')
important = ['KSB214','KB077']

result = data_frame[data_frame['工厂款号'].isin(important)]             #使用isin方法检查是否在列表里
writer = pd.ExcelWriter(output_file)
result.to_excel(writer)
writer.save()