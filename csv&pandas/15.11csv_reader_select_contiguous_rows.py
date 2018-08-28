#!/usr/bin/env python3
import csv

#示例：使用csv选取特定的行



input_file = './goods_data_unnecessary_header_footer.csv'
output_file = './goods_output.csv'

#使用迭代变量来实现
row_counter = 0
with open(input_file,'r',encoding='gbk') as csv_in_file:
    with open(output_file,'w',encoding='gbk') as csv_out_file:
        file_reader = csv.reader(csv_in_file)
        file_writer = csv.writer(csv_out_file)
        for row in file_reader:
            if row_counter>=1 and row_counter<=45:
                file_writer.writerow(row)
            row_counter+=1