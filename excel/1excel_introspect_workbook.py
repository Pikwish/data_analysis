#!/usr/bin/env python3
from xlrd import open_workbook

#读取工作表的信息
input_file = './xls_files/1.xls'
workbook = open_workbook(input_file)
for work_sheet in workbook.sheets():
    print('表名：{0},\t行数：{1},\t列数：{2}'.format(work_sheet.name,work_sheet.nrows,work_sheet.ncols))
