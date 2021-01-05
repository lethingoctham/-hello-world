# -*- coding: utf-8 -*-
"""


@author:le thi ngoc tham
"""

import os
fo=input('Nhap ten thu muc: ')
fi=input('Nhap ten tap tin: ')
os.chdir('C:\\')
os.mkdir(fo)
os.chdir(fo)
open(fi,mode='a+')
print('kết thúc bài ')