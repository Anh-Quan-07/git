# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:16:24 2020

@author: quann
"""

h=int(input("Số lần lặp của thông báo  = "))
import time
import os 
while h>0:
      a=input("Bạn có muốn tắt máy hay không ? (có/không): ")
      if a=='có':
       os.system("shutdown /s /t 1") 
      else : 
       time.sleep(30)

