#!/usr/bin/env python3
import pandas as pd

input_file = './xls_files/2.xls'
output_file = './xls_files/pandas_output.xls'

#使用pandas筛选成本超过500的所有行

data_frame = pd.read_excel(input_file,'素金入库',index_col=None)
result = data_frame[data_frame['实际成本'] > 500]                       #筛选出data_frame里实际成本大于500的所有记录，返回一个data_frame
writer = pd.ExcelWriter(output_file)
result.to_excel(writer,index=False)
writer.save()