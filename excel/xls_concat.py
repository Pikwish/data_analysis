#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'elpis'
__date__ = '2018/6/22 13:14'







# 源代码

for workbook in all_workbook:
    work_sheet = pd.read_excel(workbook)
    data_frames.append(work_sheet)
concat_result = pd.concat(data_frames, axis=0, ignore_index=False)
# final_result = concat_result['货品条形码']
# final_result = concat_result.loc[:, ['货品条形码']]
writer = pd.ExcelWriter(output_file)
concat_result.to_excel(writer, index=False)
writer.save()


result_file = '/Users/elpis/Downloads/output.xlsx'