#!/usr/bin/env python3
import pandas as pd
import os
import glob


# 使用pandas将路径下所有表格合并成一个连续的表格


input_path = '/Users/elpis/Desktop/库存/'
output_file = '/Users/elpis/Desktop/库存/output.csv'


all_files = glob.glob(os.path.join(input_path, '*.csv'))
all_data_frame = []
for file in all_files:
    data_frame = pd.read_csv(file)
    all_data_frame.append(data_frame)

data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=False)
print(data_frame_concat)
data_frame_concat.to_csv(output_file, index=False)
