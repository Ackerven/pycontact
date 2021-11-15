# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 15:41
# @File: tool.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import re

def isPhone(phone):
    pattern = re.compile(r'^[0-9]{11}$')
    return True if pattern.match(phone) else False
