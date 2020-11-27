# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:02:04 2020

@author: quann
"""
#1
m=int(input("Sô phần tử của list  = "))
import random 
def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 
num = m  
start = 50
end = 1000 
print(Rand(start, end, num)) 
# 2
n=int(input("Sô phần tử của list  = "))
randomList = random.sample(range(-1000, 1000), n)

print("Printing list of 10 random numbers")
print(randomList)
#3
import random
f=int(input("Sô phần tử của list  = "))
randomFloatList = []
for i in range(0, f):
    x = round(random.uniform(-1000, 1000), 1)
    randomFloatList.append(x)
print("Các số thực ngẫu nhiên có f phần tử là")
print(randomFloatList)
