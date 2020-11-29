# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:18:50 2020

@author: quann
"""

import random
import string
n=random.randint(50,100)
NTAQ =list()
i=1
for i in range(n):
    m=random.randint(2,5)
    y = dict()
    g = random.choice(string.ascii_uppercase)
    p = g + ''.join(random.choice(string.ascii_lowercase) for _ in range(m - 1))
    y['name'] = p
    h = random.randint(1, 100)
    y['age'] =h
    NTAQ.append(y)
print(NTAQ)


