#!/usr/bin/env python3
import csv


input_file = './goods_input.csv'
output_file = './goods_output.csv'

#示例：当处理多个文件但其标题行以及格式各不相同时，提高代码复用率。
# 要求：只保留工厂款号和实际成本两列数据

#需要的两列列名输入列表
my_columns = ['工厂款号','实际成本']
my_columns_index = []
with open(input_file,'r',encoding='gbk') as csv_in_file:
    with open(output_file,'w',encoding='gbk') as csv_out_file:
        file_reader = csv.reader(csv_in_file)
        file_writer = csv.writer(csv_out_file)
        header = next(file_reader,None)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        file_writer.writerow(my_columns)
        for row in file_reader:
            row_output = []
            for index_value in my_columns_index:
                row_output.append(row[index_value])
            file_writer.writerow(row_output)

