#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import csv


#data_frame = pd.read_csv('./input_file.csv')                    #使用pandas的read_csv方法读取csv文件
#print(data_frame)
#data_frame.to_csv('./output_file.csv',index=False)              #将内容写入csv文件




#引入csv模块来规范化数据，诸如上面例子，一旦数据里的数字本身包含一个逗号，则一个数字将会被python分隔成两个元素
#使用csv模块解决此问题

with open('./input_file.csv','r') as csv_in_file:
    with open('./output_file.csv','w') as csv_out_file:
        file_reader = csv.reader(csv_in_file,delimiter=',')                #delimite为指定分隔符
        file_writer = csv.writer(csv_out_file,delimiter = ',')
        for row in file_reader:
            print(row)
            file_writer.writerow(row)


