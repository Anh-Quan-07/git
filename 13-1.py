# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:37:53 2020

@author: quann
"""

#  1. Thư viên thao tác với cá tệp tin và thư muc là thư viên OS đối vs thư mục
#    Các hàm cơ bản của thư mục là: 
#         Hiển thị thư mục hiện tại :os.getcwd()
#         Thay đổi thư mục hiện tại :os.chdir()
#         Danh sách thư mục và file :os.listdir()
#         Tạo một thư mục mới       :os.mkdir()
#         Đổi tên thư mục hoặc tên file:os.rename()
#         Xóa bỏ thư mục hoặc file  :os.rmdir()
#    Các hàm cơ bản của file là
#         Mở file                   : fh = open(filepath, mode)
#         Đọc nội dung từ file      : read([count]) 
#         Ghi nội dung vào file     : write()
#         Đóng file đã mở           : close()
#         Đổi tên file              : os.rename(old, new)
#         Xóa file                  : os.remove(file)
# 2. Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và in kết quả ra màn hình

f1 = open('C:/', 'r')
print (f1.read())

import os
f2 = os.listdir('C:/')
print (f2.read())

# 3. Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và:
#      - Danh sách tập tin đưa vào List1
#      - Danh sách thư mục đưa vào List2
path='C:\\'
list1=list()
list2=list()
for b,c  in os.walk(path):
    for file in c:
        list1.append(file)
    for file in b:
        list.append(file)
print(' danh sách cá tệp tin của ổ đĩa c', list1)
print(' danh sách thư mục của ổ đĩa ' , list2 )



