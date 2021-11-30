# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 29/11/2021 20:19
# @File: excel.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import yaml
import pandas as pd
from utils import tool
file = open('config.yaml', 'r', encoding='utf-8')
config = yaml.load(file, Loader=yaml.FullLoader)
file.close()

defaultPath = config['File'][config['env']]['xlsx']


def init():
    pass


def loading(filePath=None) -> list:
    if filePath is None:
        filePath = defaultPath
    df = pd.read_excel(filePath)
    try:
        df.drop(columns='Unnamed: 0', axis=1, inplace=True)
    except:
        pass
    print("Successfully loaded data from " + filePath)
    return tool.dfToObject(df)


def save(data, filePath=None):
    if filePath is None:
        filePath = defaultPath
    df = tool.objectToDict(data)
    df.to_excel(filePath)
    print("Successfully saved to " + filePath)