# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 22:43:16 2020

@author: quann
"""
import random
n=int(input("Nhập n= "))
R=random.sample(range(1,1000),n)
print("List ngẫu nhiên là",R)
f=0
f=int(f)
i=0
i=int(i)
while i<n:
    if f<R[i]:
        f=R[i]
    i+=1       
print("Giá trị lớn nhất là",f)
