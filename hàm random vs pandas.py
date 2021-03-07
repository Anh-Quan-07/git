# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:27:23 2021

@author: quann
"""

import csv

# import file csv
with open('C:\danh-sach-sinh-vien.csv','rt')as f:
  tada = csv.reader(f)
  for row in tada:
        print(row)
        
#nhập gói cấu trúc gốc 
import pandas as pd
import numpy as np


# Chuyển từ điển thành DataFrame
df = pd.DataFrame(tada) 
#chon ngẫu nhiên 7 hàng với tham số n 
df.sample(n = 7)