#!/usr/bin/env python3
import sys
import pandas as pd


# input_file = sys.argv[1]
# output_file = sys.argv[2]

input_file = './goods_input.csv'
output_file = './goods_output_by_pandas.csv'



#使用pandas将工厂款号开头为"KSB"的所有记录写入文件
data_frame = pd.read_csv(input_file,encoding='gbk')
# startswith方法为查找开头的指定字符
data_frame_value_matches_pattern = data_frame.loc[data_frame['工厂款号'].str.startswith('KSB'),:]
data_frame_value_matches_pattern.to_csv(output_file)
