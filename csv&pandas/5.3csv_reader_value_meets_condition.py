#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import csv


input_file = './goods_input.csv'
output_file = './goods_output.csv'



with open(input_file,'r',encoding="gbk") as csv_in_file:                   #注意如果引入的文件是中文，要把编码改为gbk
    with open(output_file,'w',encoding="gbk") as csv_out_file:
        file_reader = csv.reader(csv_in_file)
        file_writer = csv.writer(csv_out_file)
        header = next(file_reader)                          #由于上一行已经读完第一行，所以此处读的则是第二行
        print(header)

        #将表头写入文件里
        file_writer.writerow(header)
        for row_list in file_reader:
            goods_name = str(row_list[3]).strip()
            goods_prices = int(row_list[15])
            if goods_prices >= 1000:                        #将大于标签价大于1000的货品写入文件
                file_writer.writerow(row_list)



