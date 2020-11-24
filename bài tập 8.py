# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:58:41 2020

@author: quann
"""

import smtplib
server = smtplib.SMTP('oanhphuhau@gmail.com', 587)
server.starttls()
server.login("quannguyentien2612002@gmail.com"," nevergiveuppp ")
msg = "Chào thầy ạ "
for i in range(6):
    if i<6:
        server.sendmail("quannguyentien2612002@gmail.com","nevergiveuppp",msg)
        i+=1
server.quit()
