#!/usr/bin/env python3
# -*- coding:utf-8 -*-




# 在哪里搜索多个表格
filelocation = "/Users/elpis/Downloads/123/"
# 当前文件夹下搜索的文件名后缀
fileform = "xls"
# 将合并后的表格存放到的位置
filedestination = "/Users/elpis/Downloads/123/"
# 合并后的表格命名为file
file = "output.xlsx"

# 首先查找默认文件夹下有多少文档需要整合
import glob
from numpy import *

filearray = []
for filename in glob.glob(filelocation + "*." + fileform):
    filearray.append(filename)
# 以上是从pythonscripts文件夹下读取所有excel表格，并将所有的名字存储到列表filearray
print("在默认文件夹下有%d个文档哦" % len(filearray))
ge = len(filearray)
matrix = [None] * ge
# 实现读写数据

# 下面是将所有文件读数据到三维列表cell[][][]中（不包含表头）
import xlrd

for i in range(ge):
    fname = filearray[i]
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print("在文件%s中没有找到sheet1，读取文件数据失败,要不你换换表格的名字？" % fname)
    nrows = sh.nrows
    matrix[i] = [0] * (nrows - 1)

    ncols = sh.ncols
    for m in range(nrows - 1):
        matrix[i][m] = ["0"] * ncols

    for j in range(1, nrows):
        for k in range(0, ncols):
            matrix[i][j - 1][k] = sh.cell(j, k).value
        # 下面是写数据到新的表格test.xls中哦
import xlwt

filename = xlwt.Workbook()
sheet = filename.add_sheet("hel")

# 求和前面的文件一共写了多少行
zh = 1
for i in range(ge):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            sheet.write(zh, k, matrix[i][j][k])
        zh = zh + 1
print("我已经将%d个文件合并成1个文件，并命名为%s.xls.快打开看看正确不？" % (ge, file))
filename.save(filedestination + file + ".xls")



# if all_workbook:
#     for workbook in all_workbook:
#         work_sheet = pd.read_excel(workbook)
#         data_frames.append(work_sheet)
#     concat_result = pd.concat(data_frames, axis=0, ignore_index=False)
#     # final_result = concat_result['货品条形码']
#     writer = pd.ExcelWriter(output_file)
#     concat_result.to_excel(writer, index=False)
#     writer.save()
# else:
#     dir_list = os.listdir(input_path)
#     print(dir_list)
#     for dir in dir_list:
#         if dir == '.DS_Store':
#             continue
#         else:
#             data_frames2 = []
#             target_dir = input_path+dir
#             # os.chdir(target_dir)
#             curent_dir_workbooks = glob.glob(os.path.join(target_dir, '*.xls'))
#             for work_book in curent_dir_workbooks:
#                 work_sheet = pd.read_excel(work_book)
#                 data_frames2.append(work_sheet)
#             concat_result = pd.concat(data_frames2, axis=0, ignore_index=False)
#             final_result = concat_result.loc[:]
#             print(os.path.join(target_dir, 'output.xlsx'))
#             writer = pd.ExcelWriter(os.path.join(target_dir, 'output.xlsx'))
#             final_result.to_excel(writer, index=False)
#             writer.save()


# 源代码
# for workbook in all_workbook:
#     work_sheet = pd.read_excel(workbook)
#     data_frames.append(work_sheet)
# concat_result = pd.concat(data_frames, axis=0, ignore_index=False)
# # final_result = concat_result['货品条形码']
# # final_result = concat_result.loc[:, ['货品条形码']]
# writer = pd.ExcelWriter(output_file)
# concat_result.to_excel(writer, index=False)
# writer.save()


# result_file = '/Users/elpis/Downloads/output.xlsx'





