# -*- coding: utf-8 -*-
"""
 2020

@author: acer
"""

import random,string
B=list()
m=random.randrange(1,50)
i=1
for i in range(m):
    n=random.randrange(4,15)
    R=dict()
    T=random.choice(string.ascii_uppercase)
    H=T+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
    R['name']=H
    A=random.randrange(1,100) 
    R['age']=A
    B.insert(0,R)
print("List là:",B)