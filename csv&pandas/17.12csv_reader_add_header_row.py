#!/usr/bin/env python3
import csv


input_file = './goods_data_no_header_row.csv'
output_file = './goods_output.csv'


#使用csv库为表格添加标题行
with open(input_file,'r',encoding='gbk') as file_in_csv:
    with open(output_file,'w',encoding='gbk') as file_out_csv:
        file_reader = csv.reader(file_in_csv)
        file_writer = csv.writer(file_out_csv)
        header_list = ['货品名称','款号','实际成本','标签价']
        file_writer.writerow(header_list)
        for row in file_reader:
            file_writer.writerow(row)

