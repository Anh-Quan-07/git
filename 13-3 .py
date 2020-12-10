# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:20:57 2020

@author: quann
"""

import sys
import os
path = 'C:\\'
os.chdir(path)
os.mkdir('tenthumuc')
a='' #ki tu
b='' #chuoi ti tu
c=0
import random
import string

n=random.randint(1024**2,1024**3)
while n>1024*1000:
    while sys.getsizeof(b)<=1024*1000:
        a=random.choice(string.ascii_letters)
        b=b+a
    k="C:\\tenthumuc\\tentaptin"+str(c)+".txt"
    with open(k,'w',encoding = 'utf-8') as f:
        f.write(b)
        f.close()
    n=n-1024*1000
    c=c+1