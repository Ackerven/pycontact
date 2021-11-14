# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 11:49
# @File: contact.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

class Contact:
    def __init__(self, name, gender, phone, wx_code):
        self.__name = name
        self.__gender = gender
        self.__phone = phone
        self.__wx_code = wx_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def wx_code(self):
        return self.__wx_code

    @wx_code.setter
    def wx_code(self, wx_code):
        self.__wx_code = wx_code
