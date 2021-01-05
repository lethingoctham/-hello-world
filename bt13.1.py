# -*- coding: utf-8 -*-
"""


@author:le thi ngoctham
"""

import os
path = 'C:\\'
files = list()
for r, d,f  in os.walk(path):
    for file in d:
        files.append(os.path.join(r, file))
for f in files:
    print(f)
print(' ket thuc bai ')
path = 'C:\\'
list1 = list()
list2 = list()
for r, d,f  in os.walk(path):
    for file in f:
        list1.append(file)
    for file in d:
        list2.append(file)
print('danh sach tap tin:',list1)
print('danh sach thu muc:',list2)
print('ket thuc bai ')