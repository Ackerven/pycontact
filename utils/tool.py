# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 15:41
# @File: tool.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import re

import pandas as pd

import logging

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
        data.append(Contact(df.loc[i][1], df.loc[i][2], str(df.loc[i][3]), df.loc[i][4]))
    return data


def myLogger(level, msg):
    def showLog(func):
        def wrapper(*args):
            if level == 'DEBUG':
                logging.debug(msg=msg)
            elif level == 'INFO':
                print('INFO...')
                logging.info(msg=msg)
            elif level == 'WARNING':
                logging.warning(msg=msg)
            elif level == 'ERROR':
                logging.error(msg=msg)
            elif level == 'CRITICAL':
                logging.critical(msg=msg)
            # logging.log(level=level, msg=msg)

            if len(args) == 0:
                func()
            elif len(args) == 1:
                func(args[0])
            elif len(args) == 2:
                func(args[0], args[1])
            elif len(args) == 3:
                func(args[0], args[1], args[2])
            elif len(args) == 4:
                func(args[0], args[1], args[2], args[3])
            elif len(args) == 5:
                func(args[0], args[1], args[2], args[3], args[4])
            elif len(args) == 6:
                func(args[0], args[1], args[2], args[3], args[4], args[5])
            elif len(args) == 7:
                func(args[0], args[1], args[2], args[3], args[4], args[5], args[6])

        return wrapper
    return showLog