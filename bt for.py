# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:27:47 2020

@author: acer
"""

list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}),
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}),
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}),
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for index, (a,b) in enumerate(list2):
   print(a,"---",b)
   for i in a:
       print("phần tử 1: ",a['name'],"-----","phần tử 2: ",a['age'])
   for j in b:
       print("phần tử 1: ",b['name'],"-----","phần tử 2: ",b['age'])
    
    