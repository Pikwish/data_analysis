#!/usr/bin/env python3

import pandas as pd

#使用pandas在多个工作表中读取指定的多个工作表
#要求：将第1，2个工作表内成本价低于500的记录筛选出来

input_file = './xls_files/2.xls'
output_file = './xls_files/pandas_output.xls'

my_sheets = [0,1]               #设置一个列表存储需要的工作表的索引值

data_frame = pd.read_excel(input_file,sheet_name=my_sheets)
row_list = []
for worksheet_name,data in data_frame.items():
    row_list.append(data[data['实际成本'] < 500])

result = pd.concat(row_list,axis=0,ignore_index=True)               #将多张表合并
writer = pd.ExcelWriter(output_file)
result.to_excel(writer,index=False)
writer.save()


