# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:22:18 2020

@author: acer
"""

import random
n=random.randrange(50,1000)
print(n)
print('kết thúc bài ')
apple=list()
for i in range(n):
    apple.append(random.randrange(-1000,1000))
print(apple)
print('kết thúc bài ')
apple1=list()
for i in range(n):
    apple.append(random.triangular(-1000.0,1000.0))
print(apple)
print('kết thúc bài')