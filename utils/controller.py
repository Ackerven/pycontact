# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 15/11/2021 14:49
# @File: controller.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import re
import os

import yaml

import utils.csv as csv
import utils.excel as excel
from model.contact import Contact

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()

defaultPath = config['File'][config['env']][config['mode']['data']]


def init():
    if os.path.isfile(defaultPath):
        data = []
        print("loading...")
        if config['mode']['data'] == 'csv':
            csv.loading(data)
        elif config['mode']['data'] == 'excel':
            data = excel.loading()
        print("Successfully loading project!")
        print("Enjoy yourself! ")
        return data
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
    elif config['mode']['data'] == 'excel':
        excel.save(data)


def importData(data, filePath, overlay=False):
    if overlay:
        data.clear()
    if config['mode']['data'] == 'csv':
        csv.loading(data, filePath)
    elif config['mode']['data'] == 'excel':
        for i in excel.loading(filePath):
            data.append(i)


def export(data, filePath):
    if config['mode']['data'] == 'csv':
        csv.save(data, filePath)
    elif config['mode']['data'] == 'excel':
        csv.save(data, filePath)

# NO FILE IO

def class_to_dict(data):
    dict_list = []
    for i in data:
        dict_list.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'phone': i.phone, 'wx_code': i.wx_code})
    return dict_list[:]


def queryID(data, cid):
    for i in data:
        if i.id == cid:
            return i
    return None


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


def queryPos(data, cid):
    for i in range(len(data)):
        if data[i].id == cid:
            return i
    return -1


def delete(data, cid):
    pos = queryPos(data, cid)
    if pos != -1:
        del data[pos]
        return True
    else:
        return False


def modify(data, cid, name, gender, phone, wx_code):
    pos = queryPos(data, cid)
    if pos != -1:
        data[pos] = Contact(name, gender, phone, wx_code, cid=cid)
        return True
    else:
        return False
