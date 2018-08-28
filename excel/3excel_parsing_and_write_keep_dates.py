#!/usr/bin/env python3

import xlrd
import xlwt
from datetime import date



input_file = './xls_files/2.xls'
output_file = './xls_files/output_file.xls'
output_workbook = xlwt.Workbook()
output_worksheet = output_workbook.add_sheet('输出表')
with xlrd.open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('素金入库')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index,col_index) == 3:
                date_cell = xlrd.xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
                print(date_cell)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index,col_index,date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index,col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index,col_index,non_date_cell)
# output_workbook.save(output_file)
