#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import pandas as pd

input_file = './goods_input.csv'
output_file = './goods_output_by_pandas.csv'

data_frame = pd.read_csv(input_file,encoding='gbk')

#使用强大的loc将需要达到条件的记录筛选出来
# 条件：货品名称包含“手镯”字符或者标签价大于200


data_frame_value_condition = data_frame.loc[(data_frame['货品名称'].str.contains("手镯")) | (data_frame['标签价'] >200),:]        #注意冒号前有一个逗号
data_frame_value_condition.to_csv(output_file)
print(data_frame_value_condition)

# data_test = data_frame.loc[data_frame['标签价']>500,:]
# print(data_test)


#本节新内容：loc