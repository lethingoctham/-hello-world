# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:11:54 2020

@author: acer
"""

import random
n=int(input("n="))
list1=[]
i=1
while i<=n:
    a=random.random()
    list1.append(a)
    i=i+1
print(list1)
max=list1[0]
i=1
while i<n:
    if max<list1[i]:
        max=list1[i]
    i=i+1
print("gia tri lon nhat la:",max)
print("ket thuc chuong trinh")
