#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# input_file = sys.argv[1]
# output_file = sys.argv[2]

with open('./input_file.csv','r') as filereader:
    with open('./output_file.csv','w') as filewriter:
        header = filereader.readline()                                  #使用readline读取第一行标题行并赋给header
        header = header.strip()                                         #清除空格
        header_list = header.split(',')                                 #使用逗号将元素分隔开
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')           #将header_list的元素按逗号连接起来写入output_file文件里
        for row in filereader:                                          #注意：因为第一行已经通过readline读取完了，此处的for循环则只读取剩下的内容
            row = row.strip()
            row_list = row.split('-')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
