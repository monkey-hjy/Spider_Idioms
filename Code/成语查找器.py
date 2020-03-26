# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Spider
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  :
import pandas as pd

data = pd.read_csv('f://SpiderData//CSV//idioms.csv', encoding='ANSI')
idioms = list(data['idioms'])
first = list(data['first'])
idioms_dict = {}
for i in range(len(first)):
    if first[i] not in idioms_dict.keys():
        idioms_dict[first[i]] = [idioms[i]]
    else:
        idioms_dict[first[i]].append(idioms[i])
f = input('请输入成语开头的文字：')
try:
    result = idioms_dict[f]
    print(f'以“{f}”开头的成语有{len(result)}个，如下所示：')
    print('-'*50)
    for i in range(len(result)):
        print(f'-->{result[i]}')
except:
    print(f'抱歉，未找到以“{f}”开头的成语')

