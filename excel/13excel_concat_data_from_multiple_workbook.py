#!/usr/bin/env python3

from xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple
import glob
from datetime import date
import os

input_path = './xls_files/'
output_file = './xls_files/output_file.xls'

#连接多个工作簿
output_book = Workbook(output_file)
output_sheet = output_book.add_sheet('输出结果')
data = []
first_sheet = True
for file in glob.glob(os.path.join(input_path,'sales*')):
    print(os.path.basename(file))
    with open_workbook(file) as workbook:
        for sheet in workbook.sheets():
            if first_sheet:
                header = sheet.row_values(0)
                data.append(header)
                first_sheet = False
            for row_index in range(1,sheet.nrows):
                row_list = []
                for col_index in range(1,sheet.ncols):
                    cell_value = sheet.cell_value(row_index,col_index)
                    cell_type = sheet.cell_type(row_index,col_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                data.append(row_list)
for list_index,output_list in enumerate(data):
    for element_index in enumerate(output_list):
        output_sheet.write(list_index,element_index)
output_book.save()