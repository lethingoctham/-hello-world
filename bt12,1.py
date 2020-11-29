# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:56:43 2020

@author: acer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
#ma trận----------------------------------------------------
x = np.array([[1, 3,5],[43,5,7],[6,8,0]])
y = np.array([[4,6,9],[2,25,6],[-5,6,16]])
print("tong hai ma tran la: ")
print(x+y) 
print("")
print("tich hai ma tran la: ")
print(x*y) 
print("chuyen vi ma tran x la: ")
#chuyển vị ma trận
print(x.transpose())      
print("chuyen vi ma tran y la: ")
#chuyển vị ma trận
print(y.transpose())      
#đọc file--------------------------------------------------
#đọc file csv từ máy tính
n = pd.read_csv("test.csv")
n = n.head(10)
print('file từ máy')
print(n)
#đọc file csv từ internet
data = pd.read_csv('')
data = data.head(10)
print('file từ internet')
print(data)
#đọc file JSON từ internet
js = pd.read_json('', orient='records')
print("file JSON từ internet")
for i in range(10):
    print(js[i])
#đồ thị------------------------------------------------------------------------
name = ["A",'B','C','D']
gt = [70,82,50,60]

mp.barh(name, gt, color='blue')
mp.title("đồ thị hình bar")
mp.xlabel("giá trị")
mp.ylabel("name")
mp.show()

mp.bar(name, gt, color='green')
mp.title("đồ thị hình column")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()

mp.plot(name, gt, color='red')
mp.title("đồ thị hình line")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()

mp.boxplot(gt)
mp.title("đồ thị hình boxplot")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()