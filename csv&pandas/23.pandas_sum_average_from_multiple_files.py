#!/usr/bin/env python3

import pandas as pd
import glob
import os


input_path = './group_files/'
output_file = './goods_output.csv'

all_files = glob.glob(os.path.join(input_path,'sale*'))
all_data_frame = []
for file in all_files:
    data_frame = pd.read_csv(file)
    # total_cost = pd.DataFrame([float(str(value) for value in data_frame.loc[:,'Sale Amount'] )])
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data_frame.loc[:,'Sale Amount']]).mean()
    average = pd.DataFrame([])
    # data_result = {'file_name':os.path.basename(input_path),'total_sale':total_sales}