#!/usr/bin/env python3

import pandas as pd

# 使用pandas选取特定的列
# 要求：选取“货品名称”，‘标签价’，‘实际成本’


input_file = './xls_files/2.xls'
outpu_file = './xls_files/pandas_output.xls'


data_frame = pd.read_excel(input_file,sheet_name=None)
column_output = []
for worksheet_name,data in data_frame.items():
    column_output.append(data.loc[:,['货品名称','标签价','实际成本']])

result = pd.concat(column_output,axis=1)
writer = pd.ExcelWriter(outpu_file)
result.to_excel(writer)
writer.save()
