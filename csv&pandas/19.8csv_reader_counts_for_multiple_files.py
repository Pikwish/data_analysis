#!/usr/bin/env python3

import csv
import os
import glob



#获取文件夹内所有文件的数量以及每个文件中行和列的数量

input_path = './group_files/'
file_counter = 0


#join方法将路径与该路径下所有sale开头为文件名连接起来，形成一个完整的文件路径
for input_file in glob.glob(os.path.join(input_path,'sales*')):
    row_counter = 1
    with open(input_file,'r') as csv_in_file:
        file_reader = csv.reader(csv_in_file)
        header = next(file_reader)
        for row in file_reader:
            row_counter += 1

        #os.path.basename(input_file)  从完整的路径下抽出文件名
        print('{0!s}:\t {1:d}行 \t {2:d}列'.format(os.path.basename(input_file),row_counter,len(header)))
    file_counter+=1
print('总文件数量：{0:d}'.format(file_counter))