#!/usr/bin/env python3

import pandas as pd


# 使用pandas取出需要的列
input_file = './xls_files/3.xls'
output_file = './xls_files/pandas_output.xls'

data_frame = pd.read_excel(input_file)
result = data_frame.iloc[:,[3,10]]                       #使用iloc传入列索引

writer = pd.ExcelWriter(output_file)
result.to_excel(writer,index=False)
writer.save()
