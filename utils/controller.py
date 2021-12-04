# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 15/11/2021 14:49
# @File: controller.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import os
import re

import yaml

import utils.csv as csv
import utils.excel as excel
import utils.mysql as db
from model.contact import Contact

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()

if config['mode']['data'] != 'db':
    defaultPath = config['File'][config['env']][config['mode']['data']]


# 程序启动初始化函数
def init():
    if config['mode']['data'] == 'db':
        data = db.queryAll()
        print("Successfully loading project!")
        print("Enjoy yourself! ")
        return data
    else:
        if os.path.isfile(defaultPath):
            data = []
            print("loading...")
            if config['mode']['data'] == 'csv':
                csv.loading(data)
            elif config['mode']['data'] == 'xlsx':
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



# 把用户列表数据写入文件
def save(data):
    if config['mode']['data'] == 'csv':
        csv.save(data)
    elif config['mode']['data'] == 'xlsx':
        excel.save(data)


# 从文件中导入数据
def importData(data, filePath, fileType, overlay=False):
    if overlay:
        data.clear()
    if fileType == 'csv':
        tmp = csv.loading(filePath)
    elif fileType == 'xlsx':
        tmp = excel.loading(filePath)

    if config['mode']['data'] == 'db':
        tmpId = db.getId()
        for i in tmp:
            tmpId += 1
            i.id = tmpId
            data.append(i)
        db.insert(tmp)
    else:
        for i in tmp:
            data.append(i)


# 导出数据到文件
def export(data, filePath, fileType):
    if fileType == 'csv':
        csv.save(data, filePath)
    elif fileType == 'xlsx':
        excel.save(data, filePath)


# NO FILE IO
# 把对象列表转为对象字典列表
def object_to_dict(data):
    dict_list = []
    for i in data:
        dict_list.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'phone': i.phone, 'wx_code': i.wx_code})
    return dict_list[:]


# 通过id查询用户是否存在
def queryID(data, cid):
    for i in data:
        if i.id == cid:
            return i
    return None


# 根据给定字段查找联系人
def search(data, key, field=None, fuzzy=False):
    result = []
    if fuzzy:  # True
        # 贪婪模式 djm -> '.*{}.*'.format(key)
        # 非贪婪模式 djm -> '.*?'.join(key)
        pattern = '.*{}.*'.format(key)
        regex = re.compile(pattern)
        if field:  # No None
            data_dict = object_to_dict(data)
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
            data_dict = object_to_dict(data)
            for i in data_dict:
                if i[field] == key:
                    result.append(queryID(data, i['id']))
        else:  # None
            for i in data:
                if i.name == key or i.gender == key or i.phone == key or i.wx_code == key:
                    result.append(i)
    return result


# 通过cid用户在列表中的位置
def queryPos(data, cid):
    for i in range(len(data)):
        if data[i].id == cid:
            return i
    return -1


# 删除用户
def delete(data, cid):
    pos = queryPos(data, cid)
    if pos != -1:
        del data[pos]
        db.delete(cid)
        return True
    else:
        return False


# 修改用户
def modify(data, cid, name, gender, phone, wx_code):
    pos = queryPos(data, cid)
    if pos != -1:
        tmp = Contact(name, gender, phone, wx_code, cid=cid)
        data[pos] = tmp
        db.update(cid, tmp)
        return True
    else:
        return False
