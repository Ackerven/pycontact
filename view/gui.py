# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 2021/12/5 09:37
# @File: gui.py
# OS: Windows 10
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import tkinter as tk
import utils.controller as controller

field_dic = {'姓名': 'name', '性别':'gender', '电话':'phone', '微信号':'wx'}

def handlerAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


# 菜单栏
def Meun(root):
    # 创建主菜单栏
    menubar = tk.Menu(root)

    # 创建菜单 tearoff 为 1 时可以独立出来
    menufile = tk.Menu(menubar, tearoff=0)
    menuset = tk.Menu(menubar, tearoff=0)
    menuhelp = tk.Menu(menubar, tearoff=0)

    # 把菜单作为层叠菜单添加到主菜单
    menubar.add_cascade(label='文件', menu=menufile)
    menubar.add_cascade(label='设置', menu=menuset)
    menubar.add_cascade(label='帮助', menu=menuhelp)

    # 添加菜单项到菜单
    menufile.add_command(label='导入')
    menufile.add_command(label='导出')
    menuset.add_command(label='数据源')
    menuhelp.add_command(label='关于')

    # 把菜单栏添加到根窗口
    root['menu'] = menubar


def searchFrame(root):
    # 定义框架
    frame = tk.Frame(root, bg='gray')
    frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    # 添加控件
    # 添加多选框
    vom = tk.StringVar(frame)
    vom.set('All')
    om = tk.OptionMenu(frame, vom, 'All', '姓名', '性别', '电话', '微信号')
    om.place(relx=0.02, rely=0.2, relwidth=0.13, relheight=0.6)

    # 添加输入框
    vtext = tk.StringVar(frame)
    w1 = tk.Entry(frame, textvariable=vtext)
    w1.place(relx=0.16, rely=0.2, relwidth=0.6, relheight=0.6)

    # 添加复选框
    vcb = tk.BooleanVar(frame)
    vcb.set(False)
    w = tk.Checkbutton(frame, text='模糊搜索', onvalue=True, offvalue=False, variable=vcb)
    w.place(relx=0.77, rely=0.2, relwidth=0.15, relheight=0.6)

    # 添加事件
    # w1.bind("<KeyPress>", handlerAdaptor(search, field=vom.get(), key=vtext.get(), fuzzy=vcb.get()))
    w1.bind("<KeyPress>", lambda event: search(event.char, vom.get(), vtext.get(), vcb.get()))


# 搜索框事件
def search(lastChar, field, key, fuzzy):
    if lastChar.isalnum():
        key += lastChar

    print("field = {}, key = {}, fuzzy = {}".format(field_dic[field], key, fuzzy))

def gui():
    # 创建主窗口并设置属性
    root = tk.Tk()
    root.title('Contact')
    root['bg'] = 'white'
    root['width'] = 542
    root['height'] = 442
    root.resizable(0, 0)

    # 添加菜单栏
    Meun(root)

    # 搜索部分
    searchFrame(root)

    root.mainloop()
