# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 11:49
# @File: model.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

class Contact:
    count = 0

    def __init__(self, name, gender, phone, wx_code):
        Contact.count += 1
        self.id = Contact.count
        self.name = name
        self.gender = gender
        self.phone = phone
        self.wx_code = wx_code

    def __str__(self):
        return "id: {}, name: {}, gender: {}, phone: {}, wx_code: {}". \
            format(self.id, self.name, self.gender, self.phone, self.wx_code)
