#!/usr/bin/env python3

import csv

#示例：保留大类和标签价两列

input_file = './goods_input.csv'
output_file = './goods_output.csv'
wanted_columns = [2,15]
with open(input_file,'r',encoding='gbk') as file_in_file:
    with open(output_file,'w',encoding='gbk') as file_out_file:
        file_reader = csv.reader(file_in_file)
        file_writer = csv.writer(file_out_file)
        for row in file_reader:
            result = []
            for column in wanted_columns:
                result.append(row[column])
            file_writer.writerow(result)
