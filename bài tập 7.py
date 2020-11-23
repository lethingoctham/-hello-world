# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:17:23 2020

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
min=list1[0]
i=1
while i<n:
    if min>list1[i]:
        min=list1[i]
    i=i+1
print("giá trị nhỏ nhất là:",min)
print("kết thúc chương trình")