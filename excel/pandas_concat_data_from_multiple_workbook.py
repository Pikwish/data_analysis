#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import glob
import os
import sys

# 使用pandas从多个工作簿中连接起来
# input_path = sys.argv[1]
# output_file = sys.argv[2]
input_path = '/Users/elpis/Downloads/库存'
output_file = '/Users/elpis/Downloads/库存/output.xlsx'

all_workbook = glob.glob(os.path.join(input_path, '*.xlsx'))
data_frames = []
if all_workbook:
    for workbook in all_workbook:
        work_sheet = pd.read_excel(workbook)
        data_frames.append(work_sheet)
    concat_result = pd.concat(data_frames, axis=0, ignore_index=False)
    # final_result = concat_result['货品条形码']
    # final_result = concat_result.loc[:, ['门店', '主销', '金重', '实收金额']]
    # final_result = concat_result.loc[:, '货品条形码']
    final_result = concat_result.loc[:,]
    writer = pd.ExcelWriter(output_file)
    final_result.to_excel(writer, index=False)
    writer.save()
else:
    dir_list = os.listdir(input_path)
    print(dir_list)
    for dir in dir_list:
        if dir == '.DS_Store':
            continue
        else:
            data_frames2 = []
            target_dir = input_path+dir
            # os.chdir(target_dir)
            curent_dir_workbooks = glob.glob(os.path.join(target_dir, '*.xlsx'))
            for work_book in curent_dir_workbooks:
                work_sheet = pd.read_excel(work_book)
                data_frames2.append(work_sheet)
            concat_result = pd.concat(data_frames2, axis=0, ignore_index=False)
            final_result = concat_result.loc[:, ['网点', '主销', '金重', '实收金额']]
            print(os.path.join(target_dir, 'output.xlsx'))
            writer = pd.ExcelWriter(os.path.join(target_dir, 'output.xlsx'))
            final_result.to_excel(writer, index=False)
            writer.save()


# 源代码
# for workbook in all_workbook:
#     work_sheet = pd.read_excel(workbook)
#     data_frames.append(work_sheet)
# concat_result = pd.concat(data_frames, axis=0, ignore_index=False)
# # final_result = concat_result['货品条形码']
# final_result = concat_result.loc[:, ['货品条形码']]
# writer = pd.ExcelWriter(output_file)
# final_result.to_excel(writer, index=False)
# writer.save()


result_file = '/Users/elpis/Downloads/output.xlsx'





