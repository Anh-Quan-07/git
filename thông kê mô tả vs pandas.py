#!/usr/bin/env python
# coding: utf-8

# THỰC HÀNH THỐNG KÊ MÔ TẢ VỚI DỮ LIỆU ĐỊNH LƯỢNG
# 
# Sử dụng tập dữ liệu microbiome.csv được cung cấp để hoàn thành các bài tập sau

# Câu 1: Tải tập dữ liệu microbiome.csv vào bộ nhớ (sử dụng pandas)

# In[2]:


import numpy as np
import pandas as pd
import csv

a = pd.read_csv('microbiome.csv')
a


# NHÓM CÁC CÂU LỆNH THỰC HIỆN CÁC PHÉP TÍNH HƯỚNG TÂM
# 
# Câu 2: Hãy tính trung bình cộng của cột Patient

# In[3]:


b = a['Patient'].mean()
b


# Câu 3: Hãy tính trung bình cộng (mean) đồng thời cho 3 cột Patient, Tissue và Stool

# In[4]:


c = a.mean()
c


# Câu 4: Hãy tính trung vị (median) cho 2 cột Tissue và Stool

# In[5]:


d = a['Tissue'].median()
e = a['Stool'].median()
print("median(Tissue) = ", d)
print("median(Stool) = ", e)


# Câu 5: Hãy tính số yếu vị (mode) cho 3 cột Patient, Tissue và Stool

# In[6]:


f = a.mode()
f


# NHÓM CÂU LỆNH TÍNH PHƯƠNG SAI - ĐỘ LỆCH CHUẨN
# 
# Câu 6: Hãy tính phương sai (variance) của cột Tissue

# In[7]:


a.var()['Tissue']


# Câu 7: Hãy tính phương sai của 3 cột Patient, Tissue và Stool

# In[8]:


a.var()


# Câu 8: Hãy tính độ lệch chuẩn (standard deviation) của 3 cột Patient, Tissue và Stool

# In[9]:


a.std()


# NHÓM CÂU LỆNH TÍNH PHÂN VỊ (PERCENTILE)

# Câu 9: Tính Q1 Q2 và Q3 cho cột Tissue
# 
# Tham khảo:
# 
# 1) https://www.geeksforgeeks.org/python-pandas-dataframe-quantile/
# 
# 2) https://stackoverflow.com/questions/45926230/how-to-calculate-1st-and-3rd-quartiles/45926291

# In[10]:


print(a.Tissue.quantile([0.25,0.5,0.75]))


# Câu 10: Hãy tính z-score cho cột Tissue
# 
# Gợi ý: sử dụng hàm zscore của thư viện scipy
# 
# Tham khảo: https://stackoverflow.com/questions/24761998/pandas-compute-z-score-for-all-columns

# In[14]:


from scipy.stats import zscore
k = (a - a.mean())/a.std()
print(k)


# NHÓM CÂU LỆNH TỔNG HỢP
# 
# Câu 11: (bổ sung) Hãy tính giá trị lớn nhất và nhỏ nhất của 3 cột Patient, Tissue và Stool

# In[15]:


print("GTLN = ", a.max())
print("GTNN= ", a.min())


# Câu 12: Hãy thực thi hàm describe đối với data frame chứa dữ liệu của microbiome.csv
# 
# Tham khảo: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

# In[16]:


a.describe()


# NHÓM CÂU LỆNH ĐỒ HỌA
# 
# Câu 13: Hãy vẽ biểu đồ box plot cho cột Tissue

# In[17]:


a.boxplot('Tissue')


# Câu 14: Hãy vẽ biểu đồ box plot cho cả 2 cột Tissue và Stool chung 1 hình (gồm có 2 box plot)

# In[18]:


a.boxplot(['Tissue','Stool'])


# Câu 15: Hãy vẽ lại câu 14 với các box plot nằm ngang

# In[19]:


a.boxplot(['Tissue', 'Stool'], vert = False)


# Câu 16: Hãy sử dụng thư viện seaborn để vẽ biểu đồ box plot cho Tissue và Stool

# In[20]:


import seaborn
seaborn.boxplot(data=a[['Tissue', 'Stool']])


# In[ ]:




