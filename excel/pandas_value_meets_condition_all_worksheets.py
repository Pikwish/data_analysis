#!/usr/bin/env python3

import pandas as pd

input_file = './xls_files/2.xls'
output_file = './xls_files/pandas_output.xls'

#通过pandas筛选特定行
#要求：筛选出标签价小与1500的记录
data_frame = pd.read_excel(input_file,sheet_name=None)              #此处sheet_name=None即可以读取文件中所有工作表
row_output = []
for worksheet_name,data in data_frame.items():
    row_output.append(data[data['标签价'] < 1500])

form_concat = pd.concat(row_output,axis=0)

writer = pd.ExcelWriter(output_file)
form_concat.to_excel(writer,index=False)
writer.save()
