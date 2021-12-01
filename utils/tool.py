# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 15:41
# @File: tool.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import re

import pandas as pd

from model.contact import Contact


# 通过正则表达式判断输入的电话号码是否正确
def isPhone(phone):
    pattern = re.compile(r'^[0-9]{11}$')
    return True if pattern.match(phone) else False


# 把对象列表转为DataFrame
def objectToDF(data):
    dic = {
        'id': [],
        'name': [],
        'gender': [],
        'phone': [],
        'wx_code': []
    }

    for i in data:
        dic['id'].append(i.id)
        dic['name'].append(i.name)
        dic['gender'].append(i.gender)
        dic['phone'].append(i.phone)
        dic['wx_code'].append(i.wx_code)

    return pd.DataFrame(dic)


# DataFrame转为对象列表
def dfToObject(df):
    data = []
    for i in range(len(df)):
        # print(df.loc[i])
        data.append(Contact(df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4]))
    return data
