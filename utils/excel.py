# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 29/11/2021 20:19
# @File: excel.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import yaml

file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()

defaultPath = config['File'][config['env']]['csv']


def init():
    pass


def loading(data, filePath=None):
    pass


def save(data, filePath=None):
    pass
