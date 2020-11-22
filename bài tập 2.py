# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:39:47 2020

@author: quann
"""


h=int(input("Nhập số lần lặp h= "))
while h>0:
    a = float(input("Nhập hệ số bậc , a = "));
    b = float(input("Nhập hệ số bậc 1, b = "));
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
for i in range(h):
    a=float(input("Nhập a="))
    b=float(input("Nhập b="))
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