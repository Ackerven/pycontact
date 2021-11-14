# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 15:41
# @File: tool.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import os

import yaml

import utils.csv as csv

file = open('../config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()


def init(data):
    if config['mode'] == 'csv':
        if os.path.isfile(config['File']['csv']):
            print("loading...")
            csv.loading(data)
            print("Successfully loading project!")
        else:
            print("Initializing...")
            csv.init()
            print("Successfully initialized project!")
    print("Enjoy yourself! ")


def save(data):
    if config['mode'] == 'csv':
        csv.save(data)

