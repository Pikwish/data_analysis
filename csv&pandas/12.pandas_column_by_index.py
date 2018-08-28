#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd

input_file = './goods_input.csv'
output_file = './goods_output_by_pandas.csv'



#示例：使用pandas选取两列数据并将其写入文件
data_frame = pd.read_csv(input_file,encoding='gbk')
#iloc方法根据列索引筛选列
data_frame_column_by_index = data_frame.iloc[:,[2,15]]
data_frame_column_by_index.to_csv(output_file,index=False)              #index=False，默认为True,意思为是否保留索引值
