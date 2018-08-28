#!/usr/bin/env python3

from xlrd import open_workbook
import glob
import os

#当要处理多个文件时，需要大概知道这些文件内的信息,比如文件数量，行数，列数

input_path = './xls_files/'
output_file = './xls_files/output_file.xls'

workbook_count = 0
for file in glob.glob(os.path.join(input_path,'sales*')):
    workbook = open_workbook(file)
    print('文件名：{0},工作表数量：{1}'.format(os.path.basename(file),workbook.nsheets))
    for sheet in workbook.sheets():
        print('行数：{0}，列数：{1}'.format(sheet.nrows,sheet.ncols))
    workbook_count+=1
print('\n文件数量：{0}'.format(workbook_count))



