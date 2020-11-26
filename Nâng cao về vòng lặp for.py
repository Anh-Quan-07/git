# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:00:47 2020

@author: quann
"""
list2  = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for i in list2:
   for x in i :
     print(x)
   for index ,y in enumerate(x,0):
       print(index ,y,"",x[y])