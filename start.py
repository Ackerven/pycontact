# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 20:32
# @File: start.py
# OS: 
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import yaml
from view.console import console
from view.gui import gui

# 启动程序，根据配置文件选择启动界面
# Console 控制台 console()
# GUI 图形界面 gui()
if __name__ == '__main__':
    config = yaml.load(open('config.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    if config['mode']['view'] == 'Console':
        console()
    elif config['mode']['view'] == 'GUI':
        gui()
