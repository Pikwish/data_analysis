#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import csv

input_file = './goods_input.csv'
output_file = './goods_output.csv'

#练习：将品类是手镯和碗的记录写入文件
my_favorite_class = ['手镯','碗']
with open(input_file,'r',encoding="gbk") as csv_in_file:                   #注意如果引入的文件是中文，要把编码改为gbk
    with open(output_file,'w',encoding="gbk") as csv_out_file:
        file_reader = csv.reader(csv_in_file)
        file_writer = csv.writer(csv_out_file)
        header = next(file_reader)
        file_writer.writerow(header)
        for row in file_reader:
            small_class = row[5]
            if small_class in my_favorite_class:
                file_writer.writerow(row)

