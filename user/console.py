# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 20:20
# @File: console.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import utils.tool as tool


def menu():
    print("---" * 10 + 'Contact by Ackerven' + '---' * 10)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 修改联系人")
    print("4. 查找联系人")
    print("5. 导入联系人")
    print("6. 导出联系人")
    print("0. 退出")


def addContact():
    print("add")


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


def console():
    data = []
    tool.init(data)
    while True:
        menu()
        choose = eval(input("请选择: "))
        if choose == 1:
            addContact()
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
