# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 20:20
# @File: console.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import utils.controller as controller
import utils.tool as tool
from model.contact import Contact
import utils.mysql as db


# 菜单
def menu():
    print("---" * 10 + 'Contact by Ackerven' + '---' * 10)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 修改联系人")
    print("4. 查找联系人")
    print("5. 导入联系人")
    print("6. 导出联系人")
    print("7. 列出所有联系人")
    print("0. 退出")


# 添加联系人
def addContact(data):
    name = input("请输入姓名: ")
    while True:
        print("1. Male\n2. Female")
        choose = eval(input("请选择性别: "))
        if choose == 0:
            return
        elif choose == 1:
            gender = 'Male'
            break
        elif choose == 2:
            gender = 'Female'
            break
        else:
            print("输入错误, 取消添加请输入0!")

    while True:
        phone = input("请输入手机号码: ")
        if phone == '0':
            return
        elif not tool.isPhone(phone):
            print("格式错误，取消添加请输入0!")
        else:
            break
    wx_code = input("请输入微信号: ")
    tmp = Contact(name, gender, phone, wx_code, db.getId())
    controller.add(data, tmp)
    print("成功添加联系人" + name)


# 删除联系人
def delContact(data):
    cid = eval(input("请输入需要删除的联系人的id: "))
    tmp = controller.queryID(data, cid)
    if tmp is None:
        print("联系人不存在!")
    else:
        if controller.delete(data, cid):
            print("删除" + tmp.name + '成功!')
        else:
            print("删除失败!")


# 修改字段
def mod_field(field):
    mod = input("是否修改" + field + "(y/n): ")
    if mod == 'y':
        tmp = input("请输入新的" + field + ": ")
        return tmp
    else:
        return None


# 修改联系人
def modifyContact(data):
    cid = eval(input("请输入需要修改的联系人的id: "))
    tmp = controller.queryID(data, cid)
    if tmp is None:
        print("联系人不存在!")
    else:
        # 姓名 性别 电话 微信号
        name = mod_field('姓名')
        if name is None: name = tmp.name
        mod = input("是否修改性别(y/n): ")
        gender = tmp.gender
        if mod == 'y':
            while True:
                print("1. Male\n2. Female")
                choose = eval(input("请选择新的性别(取消修改请输入0): "))
                if choose == 1:
                    gender = 'Male'
                    break
                elif choose == 2:
                    gender = 'Female'
                    break
                elif choose == 0:
                    break
        mod = input("是否修改手机号(y/n): ")
        phone = tmp.phone
        if mod == 'y':
            while True:
                temp = input("请输入新手机号码: ")
                if temp == '0':
                    break
                elif not tool.isPhone(temp):
                    print("格式错误，取消修改请输入0!")
                else:
                    phone = temp
                    break
        wx_code = mod_field('微信号')
        if wx_code is None: wx_code = tmp.wx_code
        if controller.modify(data, cid, name, gender, phone, wx_code):
            print('修改成功')
        else:
            print('修改失败')


# 查找联系人
def searchContact(data):
    key = input("请输入查找的关键字: ")
    isField = input("是否指定字段(y/n): ")
    field = ''
    if isField == 'y':
        field = input("请输入需要查找的字段: ")
    isFuzzy = input("是否开启模糊搜索(y/n): ")
    result = []
    if isFuzzy == 'y' and isField == 'y':
        result = controller.search(data, key, field=field, fuzzy=True)
    elif isFuzzy == 'n' and isField == 'y':
        result = controller.search(data, key, field=field)
    elif isFuzzy == 'y' and isField == 'n':
        result = controller.search(data, key, fuzzy=True)
    else:
        result = controller.search(data, key)

    if result:
        print("共找到{}条数据: ".format(len(result)))
        for i in result:
            print(i)
    else:
        print("共找到0条数据.")


# 到处联系人
def exportContact(data):
    try:
        while True:
            filePath = input("请输入导出文件路径(支持csv, xlsx): ")
            if filePath == '0':
                return
            else:
                fileType = filePath.split('.')[1]
                if fileType != 'csv' and fileType != 'xlsx':
                    print("文件类型错误! 取消请输入0.")
                else:
                    break
    except:
        print("文件路径错误!")
        return
    controller.export(data, filePath, fileType)
    print("导出文件" + filePath + "成功!")


# 导入联系人
def importContact(data):
    try:
        while True:
            filePath = input("请输入导入文件路径(支持csv, xlsx)")
            if filePath == '0':
                return
            else:
                fileType = filePath.split('.')[-1]
                if fileType != 'csv' and fileType != 'xlsx':
                    print("文件类型错误! 取消请输入0.")
                else:
                    break
    except:
        print("文件路径错误!")
        return
    overlay = input("是否覆盖原数据(y/n): ")
    try:
        if overlay == 'y':
            controller.importData(data, filePath, fileType, overlay=True)
        else:
            controller.importData(data, filePath, fileType)
        print("导入文件" + filePath + "成功!")
    except:
        print("导入文件" + filePath + "失败!")


# 显示所有联系人
def showData(data):
    if data is None:
        print()
    else:
        for i in data:
            print(i)


def console():
    data = controller.init()
    while True:
        menu()
        choose = eval(input("请选择: "))
        if choose == 1:
            addContact(data)
        elif choose == 2:
            delContact(data)
        elif choose == 3:
            modifyContact(data)
        elif choose == 4:
            searchContact(data)
        elif choose == 5:
            importContact(data)
        elif choose == 6:
            exportContact(data)
        elif choose == 7:
            showData(data)
        elif choose == 0:
            break
        else:
            print("输入错误！")
    controller.save(data)
