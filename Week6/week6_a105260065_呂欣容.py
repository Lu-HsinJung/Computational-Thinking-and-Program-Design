# -*- coding: utf-8 -*-
"""Week6_A105260065_呂欣容.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15DwATohvhzJKlW1xYFo9BBHAXQ2kouWa

隨堂練習：判斷身分證字號的尾數是否為奇數
"""

id_last_digit = input("請輸入您身分證字號的尾數：")
id_last_digit = int(id_last_digit)
modulo = id_last_digit % 2
ans = modulo == 1
print(ans)