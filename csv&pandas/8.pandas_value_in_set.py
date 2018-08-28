#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd

#练习：使用pandas将类别为“碗”和“手镯”的记录写入文件

input_file = './goods_input.csv'
output_file = './goods_output_by_pandas.csv'

my_favorite_class = ["手镯","碗"]

data_frame = pd.read_csv(input_file,encoding='gbk')
data_value_in_set = data_frame.loc[data_frame['品类名称'].isin(my_favorite_class),:]                #isin方法检测是否存在列表里
data_value_in_set.to_csv(output_file)                                                              #将结果写入
