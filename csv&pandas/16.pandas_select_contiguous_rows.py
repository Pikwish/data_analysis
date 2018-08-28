#!/usr/bin/env python3

import pandas as pd

input_file = './goods_data_unnecessary_header_footer.csv'
output_file = './goods_output_by_pandas.csv'
#示例：使用pandas提取需要的行


data_frame = pd.read_csv(input_file,header=None,encoding='gbk')
data_frame = data_frame.drop([0,46,47,48])                  #使用drop方法删除所有4行不需要的行
data_frame.columns = data_frame.iloc[0]                     #将删除后的第一行作为表格的列索引
data_frame = data_frame.reindex(data_frame.index.drop(1))   #删除多余的一行并重新生成索引
data_frame.to_csv(output_file,index=False)
print(data_frame)




#本节新内容：
# drop：删除指定行
# data_frame.columns ：此为表格的列索引
# data_frame.index : 此为表格的索引
# data_frame.reindex : 重新生成索引
