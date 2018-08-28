#!/usr/bin/env python3

import pandas as pd
import glob
import os

input_path = './xls_files/'
output_file = './xls_files/pandas_output.xls'

#使用pandas计算所有文件里数据的和以及平均值
all_workbook = glob.glob(os.path.join(input_path,'sales*'))
data_frame = []

for workbook in all_workbook:
    all_worksheets = pd.read_excel(workbook,sheet_name=None,index_col=None)
    workbook_total_sales = []                      #存放所有销售额总和
    workbook_number_of_sales = []                   #存放所有销售数量
    worksheet_data_frames = []
    worksheets_data_frame = None
    workbook_data_frame = None
    print(os.path.basename(workbook))
    for worksheet_name,data in all_worksheets.items():
        for value in data.loc[:,['Sale Amount']].sum():
            total_sales = pd.DataFrame([float(str(value).strip('$').replace(',',''))])
            number_of_sales = len(data.loc[:,'Sale Amount'])
            average_sales = pd.DataFrame(total_sales / number_of_sales)

            workbook_total_sales.append(total_sales)
            workbook_number_of_sales.append(number_of_sales)
            data = {'工作簿名': os.path.basename(workbook), '工作表名': worksheet_name,'销售总和': total_sales,'销售平均值': average_sales}
            worksheet_data_frames.append(pd.DataFrame(data,columns=['工作簿名','工作表名','销售总和','销售平均值']))


        # total_sales = pd.DataFrame([float(str(value))])


