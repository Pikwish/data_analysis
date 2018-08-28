#!/usr/bin/env python3
import csv
from re import findall

#练习：保留款号开头为“KSB”的行，将其写入文件,使用正则表达式

input_file = './goods_input.csv'
output_file = './goods_output.csv'

with open(input_file,'r',encoding='gbk') as csv_in_file:
    with open(output_file,'w',encoding='gbk') as csv_out_file:
        file_reader = csv.reader(csv_in_file)
        file_writer = csv.writer(csv_out_file)
        header = next(file_reader)
        file_writer.writerow(header)
        print(header)
        for row_list in file_reader:
            style_number = row_list[7]
            if findall("KSB*",style_number):
                file_writer.writerow(row_list)


