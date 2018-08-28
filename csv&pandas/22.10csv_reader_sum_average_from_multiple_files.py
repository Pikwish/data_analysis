#!/usr/bin/env python3

import csv
import os
import glob

input_path = './group_files/'
output_file = './goods_output.csv'

#计算路径下所有文件里的数据的业绩总和以及平均值
output_header_list = ['file_name', 'total_sales', 'average_sales']
csv_out_file = open(output_file,'a')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
for input_file in glob.glob(os.path.join(input_path,'*.csv')):
    with open(input_file,'r') as csv_in_file:
        file_reader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(file_reader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in file_reader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',',''))
            number_of_sales += 1
        average_sales = total_sales/number_of_sales
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)