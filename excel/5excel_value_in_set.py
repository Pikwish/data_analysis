#!/usr/bin/env python3

from xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple

input_file = './xls_files/1.xls'
output_file = './xls_files/output_file.xls'

#示例：筛选指定款号'KSB214'的记录
output_book = Workbook()
output_sheet = output_book.add_sheet('输出结果表')
wanted = ['KSB214','KB077']
wanted_col_index = 5
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('素金入库')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    # for row_index in range(1,worksheet.nrows):
        # wanted_row = xldate_as_tuple(worksheet.cell_value(row_index,wanted_col_index,workbook.datemode))
