# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:09:23 2020

@author: quann
"""
 # numpy
import numpy as np
A = np.array([(4,5), (1,-3)], dtype = int)
B = np.array([[9, -3], [3, 6]],dtype = int)
V = A + B 
C = A.dot(B)
print(V)
print(C)
print(A.transpose())

  #pandas
import csv
with open('C:/Users/quann/Downloads/annual-enterprise-survey-2019-financial-year-provisional-csv.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
      print(row.head(10))
 # Matplotlib     
     #box plot   
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')
plt.show()
     # bar
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()
  
    