# -*- coding: utf-8 -*-
"""


@author: le thi ngoc tham
"""

import os
import sys
import string
import random
os.chdir('C:\\')
os.mkdir('hello')
size=0 #size của tổng các files(folder)
KB1000=1000*1024 #1000KB
MB1=1024**2
GB1=1024**3
m=0
size=random.randint(MB1,GB1+1)
while size > KB1000:
    n = random.randint(1, KB1000+1)
    b=''
    while sys.getsizeof(b) <= n:
        a = random.choice(string.ascii_letters)
        b = b + a
    k = "C:\\hello\\hello" + str(m) + ".txt"
    with open(k, 'w', encoding='utf-8') as f:
        f.write(b)
        f.close()
    size = size - n
    m = m + 1
print('ket thuc chuong trinh')