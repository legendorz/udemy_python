#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:40:13 2018

@author: glenn
"""

#題目一
def find_max(a_list):
    # 首先我們要先檢查清單是不是空的
    if not a_list: # 請看底下講解
        return 0 # 既然是空的，我們就提早結束function, 回傳0
    max_num = a_list[0] # 先宣告一個變數出來儲存"目前看過的最大數"，先設成清單中的第一個東西
    for num in a_list: # 清單中的每一個東西，一個一個叫出來
        if num > max_num: # 如果此數字比目前最大數還大
            max_num = num # 那就把目前最大數變成此數字
    return max_num # 最後回傳看過的最大數
   
print(find_max([1, -10, 81]))
#題目二
students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]

def second_highest(students):
    grades = [s[1] for s in students] # 只把成績拿出來
    grades = sorted(grades, reverse=True)
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    # 再下來找誰是這個分數
    # 底下這句話的意思是拿到 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
    # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)
        
second_highest(students)    
#題目三
data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
def count_products(data):
    products = {}
    for sth in data:
        item, count = sth.split()
        count = int(count)
        if item in products:
            products[item] += count
        else:
            products[item] = count
    return products

count_products(data)

#挑戰：體驗使用Python做金融研究
data =  [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
def three_days(data):
    info = []
    for i in range(0,3):
        info.append(0)
    for i in range(3, len(data)-2):
        if data[i-1] > data[i-2] and data[i-2] > data[i-3]:
            info.append(1)
        elif data[i-1] < data[i-2] and data[i-2] < data[i-3]:
            info.append(-1)
        else:
            info.append(0)
    return info




