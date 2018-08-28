#!/usr/bin/env python3
import pandas as pd

#当处理多个文件时，列的位置不同时，iloc方法将不再适用，此时可以使用loc方法来实现筛选出多个需要的列

input_file = './xls_files/1.xls'
output_file = './xls_files/pandas_output.xls'

data_frame = pd.read_excel(input_file)
result = data_frame.loc[:,['货品条形码','实际成本']]

writer = pd.ExcelWriter(output_file)
result.to_excel(writer,sheet_name='工作表1',index=False)
writer.save()
