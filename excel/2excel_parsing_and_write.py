#!/usr/bin/env python3
from xlrd import open_workbook
from xlwt import Workbook






# 处理单个工作表(sheet)

input_file = './xls_files/2.xls'
output_file = './xls_files/output_file.xls'


output_book = Workbook()
output_worksheet = output_book.add_sheet('输出结果表')               #在输出的excel文件里新增一个专门保存结果的工作表，使用add_sheet

with open_workbook(input_file) as workbook:
    work_sheet = workbook.sheet_by_name('素金入库')                 #使用输入文件里表名为'素金入库'的表并生成一个实例对象
    for row_index in range(work_sheet.nrows):
        for col_index in range(work_sheet.ncols):
            output_worksheet.write(row_index,col_index,work_sheet.cell_value(row_index,col_index))
            # print(work_sheet.cell_value(row_index,col_index))
output_book.save(output_file)
