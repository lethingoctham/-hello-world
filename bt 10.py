# -*- coding: utf-8 -*-
"""


@author:le thi ngoc tham
"""

#Numpy
print("Tìm hiểu thư viện Numpy")
import numpy as np
A=[[6,1,4],[1,2,5],[4,3,-1]]
A=np.array(A)
print(A)
B=[[1,2,1],[5,1,6],[7,1,0]]
B=np.array(B)
print("Cộng hai ma trận A và B")
print(A+B)
print("Nhân hai ma trận A và B")
print(A.dot(B))

#Pandas
print("Tìm hiểu thư viện Pandas")
import pandas as pd
result = pd.read_csv('Dataasn.csv')
print(result.head(10))
td = 'https://data.cese.nsw.gov.au/data/dataset/f0880fef-1dc8-37e3-905b-d2b015375510/resource/f794e36a-91e3-422a-beda-9ba8d2e9a58e/download/table-21-2019-enrolments-in-year-10-subjects.csv'
data = pd.read_csv(td)
print(data.head(10))
js = 'https://data.cese.nsw.gov.au/data/dataset/1a8ee944-e56c-3480-aaf9-683047aa63a0/resource/64f0e82f-f678-4cec-9283-0b343aff1c61/download/headcount.json'
datat = pd.read_json(js)
print(datat.head(10))

# Matplotlib
print(" Tìm hiểu thư viện Matplotlib")
# Bar Chart
import matplotlib.pyplot as plt
y_values = [12, 49, 20]
data_labels = ['ngoc', 'mai', 'lan']
colors = [ "#fd79a8", "#273c75", "#e74c3c"]
xs = [i + 0.03 for i, _ in enumerate(data_labels)]
plt.bar(xs,y_values, color=colors)
plt.xticks([i+0.1 for i, _ in enumerate(data_labels)], data_labels)
plt.title("Giới hạn chịu đựng của sinh viên")
plt.xlabel('Tên')
plt.ylabel('gioi han')

plt.show()
# Column Chart
men_means, men_std = (10, 35, 30, 35, 27), (2, 3, 4, 1, 2)
women_means, women_std = (15, 32, 32, 12, 25), (3, 3, 6, 3, 3)

ind = np.arange(len(men_means))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                label='man')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                label='women')

ax.set_ylabel('Sức chịu đựng')
ax.set_title('So sánh sức chịu đựng của đàn ông và đàn bà qua từng nhóm')
ax.set_xticks(ind)
ax.set_xticklabels(('N1', 'N2', 'N3', 'N4', 'N5'))
ax.legend()

plt.show()

# Boxplot Chart
x = np.random.randn(100) + np.arange(0, 100) * 2
y = np.random.randn(100) + np.arange(0, 100) * 0.5 + 10
z = np.random.randn(100) + np.arange(0, 100) * 1 - 15

plt.boxplot([x, y, z], 
            labels = ['x', 'y', 'z'],
            showfliers = True)

plt.title('Biểu đồ Boxplot')
plt.xlabel('Các lớp')
plt.ylabel('Gía trị của x, y, z')