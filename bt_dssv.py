# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:24:57 2021

@author: acer
"""

import pandas as pd
import csv
import random

file = pd.read_csv('C:/Users/acer/Downloads/danh-sach-sinh-vien.csv')
print(file.head(14))
print("-"*34)

#Chọn ngẫu nhiên 7 sv trong ds
files = file.sample(n=7)
#Lưu vào file csv mới tên DSSVmoi.csv
files.to_csv(r'C:/Users/acer/Downloads/DSSV_moi.csv', index = None, header=True)
print(files)