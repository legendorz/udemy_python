#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:40:13 2018

@author: glenn
"""

#題目一:找出list中最大值
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
#題目二：找出成績第二高的人
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
#題目三：紀錄購買商品及件數
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

#挑戰：體驗使用Python做金融研究：連續三天上漲，買進；反之，賣出；其他狀況，觀望
data =  [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
def three_days(data):
    info = []
    for i in range(len(data)):
        if i < 3:
            info.append(0)
        elif data[i] > data[i-1] and data[i-1] > data[i-2] and data[i-2] > data[i-3]:
            info.append(1)
        elif data[i] < data[i-1] and data[i-1] < data[i-2] and data[i-2] < data[i-3]:
            info.append(-1)
        else:
            info.append(0)
    return info


#挑戰二：實際運用策略計算報酬總金額計每次成交狀況繪製圖

import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file):
    # converters 那邊是告訴它Adj Close那欄 我要讀取成float，否則他預設會是字串。
    df = pd.read_csv(file) 
    df = df['Adj Close'].astype('float') # 我只要Adj Close那欄的資料
    return df.tolist() # 轉換回python內建的list物件


def calc_profit(data, signal):
    pos = 0 # 持有方向
    entry = 0 # 進場價
    trades = [] # 裝著每筆交易的損益
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == -1: # 原本持有空單，現在遇到買進訊號
                # 因為要把空單出場，換成多單
                # 要先計算 此筆單出場的獲利
                profit = entry - data[i] # 空單的獲利是 成本價 - 現在價格
                trades.append(profit)
                entry = data[i]
            pos = 1 # 把持有方向 設為 1
        elif signal[i] == -1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == 1: # 原本持有多單，現在遇到賣出訊號
                # 因為要把多單出場，換成空單
                # 要先計算 此筆單出場的獲利
                profit = data[i] - entry  # 空單的獲利是 成本價 - 現在價格
                trades.append(profit)
                entry = data[i]
            pos = -1 # 把持有方向 設為 1

    return trades


def calc_equity(trades):
    equities = []
    equity = 0
    for trade in trades:
        equity += trade
        equities.append(equity)
    return equities


def graph_equity(equity):
    plt.plot(equity)
    plt.ylabel('equity')
    plt.xlabel('trades')
    plt.show()


def main():
    data = read_csv('2330.csv')
    signal = three_days(data)
    trades = calc_profit(data, signal)
    total = sum(trades) * 1000 # 放大一千倍因為每次交易都是一張(1000股)
    print('總共損益為', total)
    print('一共有', len(trades), '筆交易')
    equity = calc_equity(trades)
    graph_equity(equity)


main()


#挑戰三：比較各國指數


import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as pdr

import fix_yahoo_finance as yf
yf.pdr_override()
import matplotlib.pyplot as plt
import datetime as dt
from datetime import timedelta
from pandas_datareader import data, wb

day_entry = 120
start = (dt.datetime.now() - timedelta(days= int(day_entry)))
end = dt.datetime.now()
dji = data.get_data_yahoo(['^DJI'], start, end)
twii = data.get_data_yahoo(['^TWII'], start, end)
stocks = pd.DataFrame({"^DJI": dji['Close'].pct_change().cumsum(),"^TWII": twii["Close"].pct_change().cumsum()})

from matplotlib import style
import pylab
from pylab import rcParams

style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
rcParams['figure.figsize'] = 12, 8
DJI = stocks['^DJI'].plot(color='Blue', label='DJI')
plt.title('台灣加權指數與美國道瓊指數之比較')
plt.ylabel('指數漲跌幅百分比')
TWII = stocks['^TWII'].plot(color='Red', label='TWII' )
plt.legend()
plt.show()


