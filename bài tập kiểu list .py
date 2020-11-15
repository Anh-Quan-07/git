# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:20:23 2020

@author: quann
"""

x = ["apple", "banana", "cherry"]
x.clear()
print(x)
x.append(18)
x.append("Huế")
y = [12, 45, -1, -0.56, "abc"]
x.extend(y)
print(x)
print(x[::(len(x)-1)])
print(x[0:5])
print(x[2:])
