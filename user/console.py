# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 20:20
# @File: console.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import utils.tool as tool
from contact.contact import Contact


def menu():
    print("---" * 10 + 'Contact by Ackerven' + '---' * 10)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 修改联系人")
    print("4. 查找联系人")
    print("5. 导入联系人")
    print("6. 导出联系人")
    print("0. 退出")

# TODO filePath

def addContact(data):
    name = input("请输入姓名: ")
    gender = input("请输入性别: ")
    while True:
        phone = input("请输入手机号码: ")
        if phone == '0':
            return
        elif not tool.isPhone(phone):
            print("格式错误，取消添加请输入0!")
        else:
            break
    wx_code = input("请输入微信号: ")
    data.append(Contact(name, gender, phone, wx_code))
    print("Add contact " + name)


def delContact():
    print("del")


def modifyContact():
    print("modify")


def searchContact():
    print("search")


def exportContact():
    print("export")


def importContact():
    print("import")


def showData(data):
    for i in data:
        print(i)

def console():
    data = []
    tool.init(data)
    while True:
        menu()
        choose = eval(input("请选择: "))
        if choose == 1:
            addContact(data)
        elif choose == 2:
            delContact()
        elif choose == 3:
            modifyContact()
        elif choose == 4:
            searchContact()
        elif choose == 5:
            importContact()
        elif choose == 6:
            exportContact()
        elif choose == 0:
            break
        else:
            print("输入错误！")
    tool.save(data)
