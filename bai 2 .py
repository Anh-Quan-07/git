# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:01:54 2020

@author: quann
"""
h=int(input("Nhập số lần lặp h= "))
a = float(input("Nhập hệ số bậc , a = "));
b = float(input("Nhập hệ số bậc 1, b = "));
while h>0:
    
    if a!=0:
        if b==0:
            print("PT có nghiệm duy nhất x=0")
        else:
            print("PT có nghiệm duy nhất x=",-b/a)
    else:
        if b==0:
            print("PT có vô số nghiệm!")
        else:
            print("PT vô nghiệm!")
    h-=1
    print("Kết thúc vòng lặp while")
h=int(input("Nhập số lần lặp h= "))
a=float(input("Nhập a="))
b=float(input("Nhập b="))
for i in range(h):
    
    if a!=0:
        if b==0:
            print("PT có nghiệm duy nhất x=0")
        else:
            print("PT có nghiệm duy nhất x=",-b/a)
    else:
        if b==0:
            print("PT có vô số nghiệm!")
        else:
            print("PT vô nghiệm!")
    print("Kết thúc vòng lặp For")
             