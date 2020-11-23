# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:21:44 2020

@author: acer
"""

print( "viết phương trình lặp giải phương trình bậc nhất n lần với các tham số được nhập vào từ bàn phím")
i=1
n=int(input("n="))
while i <= n :
    a = int(input("a="))
    b = int(input("b="))
    if a==0:
        if b==0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        print("phương trình có nghiệm là",(-b/a))
    i+=1
i=1
for i in range(n):
    a = int(input("a="))
    b = int(input("b="))
    if a == 0:
        if b == 0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        print("phương trình có nghiệm là", (-b / a))
print("chương trình kết thúc")