#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

f = open('raw.txt',encoding="utf-8")
text = f.read()
all_data = text.split("主題1")[1:]
file_list = list()
for data in all_data:
    qu_text = data.split("A.")[0]
    print(qu_text)
    try:
        A_data = data.split("A.")[1]
    except:
        A_data = data.split("A、")[1]

    A_text = A_data.split("B.")[0]
    # print(qu_text)
    # print(A_data)
    try:
        B_data = A_data.split("B.")[1]
    except:
        B_data = A_data.split("B、")[1]

    # B_data = A_data.split("B.")[1]
    B_text = B_data.split("C.")[0]

    try:
        C_data = B_data.split("C.")[1]
    except:
        C_data = B_data.split("C、")[1]
    # C_data = B_data.split("C.")[1]
    C_text = C_data.split("D.")[0]

    try:
        D_data = C_data.split("D.")[1]
    except:
        D_data = C_data.split("D、")[1]
    # D_data = C_data.split("D.")[1]
    if "答案：" in D_data:
        D_text = D_data.split("答案：")[0]
    else:
        D_text = D_data.split("正確答案")[0]
    file_list.append([qu_text, "", A_text, B_text, C_text, D_text])
print(file_list)

with open('output.csv', 'w', newline='', encoding="utf-8") as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(['題目', '正確答案', '選項一', '選項二', '選項三', '選項四'])
  for i in file_list:
    writer.writerow(i)















f.close