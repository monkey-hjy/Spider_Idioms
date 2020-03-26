# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Spider
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  : 抓取成语的信息
import requests
from lxml import etree
import pandas as pd


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    return html


def get_info(url, idioms):
    print(url)
    the_html = get_html(url)
    # 把成语放进列表
    idioms += get_idioms(the_html)
    # 判断是否有下一页
    if the_html.xpath('//div[@class="gclear pp bt center f14"]//a[last()]/text()')[0] == '下一页':
        next_url = 'https://chengyu.911cha.com/' + the_html.xpath('//div[@class="gclear pp bt center f14"]//a[last()]/@href')[0]
        get_info(next_url, idioms)
    return idioms


def get_idioms(html):
    idioms = html.xpath('//ul[@class="l5 center f14"]//li/a/text()')
    return idioms


if __name__ == '__main__':
    # 网站链接
    url = 'https://chengyu.911cha.com/'
    html = get_html(url)
    # 获取到不同拼音的成语的链接
    idioms_list_url = html.xpath('//div[@class="mcon f14 noi"]//p[last()]//a/@href')

    # 遍历不同拼音的成语的链接
    for i in range(len(idioms_list_url)):
        idioms = []
        first = []
        # 拼接出正确的链接
        the_url = 'https://chengyu.911cha.com' + idioms_list_url[i]
        idioms += get_info(the_url, idioms)
        # 取出每个成语的第一个字
        for j in range(len(idioms)):
            first.append(idioms[j][0])
        # 存储
        data = pd.DataFrame({
            'idioms': idioms,
            'first': first
        })
        if i == 0:
            data.to_csv('f://SpiderData//idioms.csv', encoding='ANSI', index=False, mode='a')
        else:
            data.to_csv('f://SpiderData//idioms.csv', encoding='ANSI', index=False, header=False, mode='a')
