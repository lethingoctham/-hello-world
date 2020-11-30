# -*- coding: utf-8 -*-
"""
2020

@author: acer
"""

import os,time
shutdown = True 
while shutdown:
    shutdown = input("Bạn có muốn tắt máy tính không? (có / không): ")
    if shutdown == 'có':
        os.system("shutdown /s /t 5") 
        shutdown = False
    else:
        print("Chờ 1 lát rồi được hỏi lại")
        time.sleep(30)
        shutdown = True