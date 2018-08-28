#!/usr/bin/env python3

import os
import csv
import glob

#使用csv将多个csv文件连接起来

input_path = './group_files/'
output_file = 'goods_output.csv'

first = True
for file in glob.glob(os.path.join(input_path,'*.csv')):
    print(os.path.basename(file))
    with open(file,'r') as file_in_csv:
        with open(output_file,'a') as file_out_csv:
            file_reader = csv.reader(file_in_csv)
            file_writer = csv.writer(file_out_csv)
            if first:
                header = next(file_reader)
                file_writer.writerow(header)
                for row in file_reader:
                    file_writer.writerow(row)
                    first = False
            else:
                header = next(file_reader)
                for row in file_reader:
                    file_writer.writerow(row)
