# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 15:41
# @File: tool.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import os
import re

import yaml

import utils.csv as csv

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()

defaultPath = config['File'][config['env']]['csv']


def init(data):
    if config['mode']['data'] == 'csv':
        if os.path.isfile(defaultPath):
            print("loading...")
            csv.loading(data)
            print("Successfully loading project!")
        else:
            print("Initializing...")
            if not os.path.exists('source'):
                print("mkdir source")
                os.mkdir('source')
            print("Successfully initialized project!")
    print("Enjoy yourself! ")


def save(data):
    if config['mode']['data'] == 'csv':
        csv.save(data)


def isPhone(phone):
    pattern = re.compile(r'^[0-9]{11}$')
    return True if pattern.match(phone) else False


def importData(data, filePath, overlay=False):
    if config['mode']['data'] == 'csv':
        if overlay:
            data.clear()
            csv.loading(data, filePath)
        else:
            csv.loading(data, filePath)


def export(data, filePath):
    if config['mode']['data'] == 'csv':
        csv.save(data, filePath)


def class_to_dict(data):
    dict_list = []
    for i in data:
        dict_list.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'phone': i.phone, 'wx_code': i.wx_code})
    return dict_list[:]


def queryID(data, id):
    for i in data:
        if i.id == id:
            return i


def search(data, key, field=None, fuzzy=False):
    result = []
    if fuzzy:  # True
        # 贪婪模式 djm -> '.*{}.*'.format(key)
        # 非贪婪模式 djm -> '.*?'.join(key)
        pattern = '.*{}.*'.format(key)
        regex = re.compile(pattern)
        if field:  # No None
            data_dict = class_to_dict(data)
            for i in data_dict:
                match = regex.search(i[field])
                if match:
                    result.append(queryID(data, i['id']))
        else:  # None
            for i in data:
                f1 = regex.search(i.name)
                f2 = regex.search(i.gender)
                f3 = regex.search(i.phone)
                f4 = regex.search(i.wx_code)
                if f1 or f2 or f3 or f4:
                    result.append(i)
    else:  # False
        if field:  # No None
            data_dict = class_to_dict(data)
            for i in data_dict:
                if i[field] == key:
                    result.append(queryID(data, i['id']))
        else:  # None
            for i in data:
                if i.name == key or i.gender == key or i.phone == key or i.wx_code == key:
                    result.append(i)
    return result
