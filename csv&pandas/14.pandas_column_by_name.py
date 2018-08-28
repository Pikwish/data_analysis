#!/usr/bin/env python3

import pandas as pd


input_file = './goods_input.csv'
output_file = './goods_output_by_pandas.csv'

#使用pandas通过指定的列标题筛选数据
data_frame = pd.read_csv(input_file,encoding='gbk')
data_frame_column_by_name = data_frame.loc[:,['工厂款号','标签价']]
data_frame_column_by_name.to_csv(output_file,index=False)
