# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 18:48
# @File: csv.py
# OS: 
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import yaml

from contact.contact import Contact

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()


def init():
    pass


def loading(data, filePath=None):
    if filePath is None:
        filePath = config['File']['csv']
    with open(filePath, 'r', encoding='utf-8') as fp:
        fp.readline()   # title
        while True:
            line = fp.readline().strip()
            if line:
                tmp = line.split(',')
                data.append(Contact(tmp[1], tmp[2], tmp[3], tmp[4]))
            else:
                break
    print("Successfully loaded data from " + filePath)


def save(data, filePath = None):
    if filePath is None:
        filePath = config['File']['csv']
    with open(filePath, 'w', encoding='utf-8') as fp:
        fp.write('id,name,gender,phone,wx_code\n')
        for i in data:
            fp.write(str(i.id) + ','
                     + i.name + ','
                     + i.gender + ','
                     + i.phone + ','
                     + i.wx_code + '\n'
                     )
    print("Successfully saved to " + filePath)
