#!/usr/bin/env python3

import pandas as pd

#将指定文件的工作表内容写入目标工作表
input_file = './xls_files/3.xls'
output_file = './xls_files/pandas_output.xls'


data_frame = pd.read_excel(input_file, sheet_name='素金入库')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='sheet1', index=False)
writer.save()





