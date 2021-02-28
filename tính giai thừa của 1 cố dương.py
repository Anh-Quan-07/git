# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:47:44 2021

@author: quann
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Nhập một số để tính giai thừa : "))
print(factorial(n))