# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 2021/12/5 09:37
# @File: gui.py
# OS: Windows 10
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import tkinter as tk
import utils.controller as controller

field_dic = {'All': 'All', '姓名': 'name', '性别': 'gender', '电话': 'phone', '微信号': 'wx_code'}


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


class searchFrame(tk.Frame):
    def __init__(self, listBox, master=None):
        tk.Frame.__init__(self, master)
        self.listBox = listBox
        # self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.createWidgets()

    def createWidgets(self):
        # 添加控件
        # 添加多选框
        vom = tk.StringVar(self)
        vom.set('All')
        om = tk.OptionMenu(self, vom, 'All', '姓名', '性别', '电话', '微信号')
        om.place(relx=0.02, rely=0.2, relwidth=0.13, relheight=0.6)

        # 添加输入框
        vtext = tk.StringVar(self)
        w1 = tk.Entry(self, textvariable=vtext)
        w1.place(relx=0.16, rely=0.2, relwidth=0.6, relheight=0.6)

        # 添加复选框
        vcb = tk.BooleanVar(self)
        vcb.set(False)
        w = tk.Checkbutton(self, text='模糊搜索', onvalue=True, offvalue=False, variable=vcb)
        w.place(relx=0.77, rely=0.2, relwidth=0.15, relheight=0.6)

        # 添加事件
        # w1.bind("<KeyPress>", handlerAdaptor(search, field=vom.get(), key=vtext.get(), fuzzy=vcb.get()))
        w1.bind("<KeyPress>", lambda event: self.search(event.char, vom.get(), vtext.get(), vcb.get()))

    # 搜索框事件
    def search(self, lastChar, field, key, fuzzy):
        try:
            if lastChar.isalnum():
                key += lastChar
            elif ord(lastChar) == 8:
                key = key[0:-1]
        except:
            pass
        # print("field = {}, key = {}, fuzzy = {}".format(field_dic[field], key, fuzzy))
        # print(type(key))
        result = []
        # print(type(key), 'key=',key)
        if key == '':
            self.listBox.setData()
        else:
            if field == 'All':
                result = controller.search(self.listBox.data, key, fuzzy=fuzzy)
            else:
                result = controller.search(self.listBox.data, key, field_dic[field], fuzzy)
            self.listBox.setData(result)


# 数据框
class dataFrame(tk.Frame):
    def __init__(self, data, master=None):
        tk.Frame.__init__(self, master)
        self.listBox = tk.Listbox(self)
        self.labShow = tk.Label(self)
        self.data = data
        self.createWidgets()

    def createWidgets(self):
        # 列表框
        self.setData()
        self.listBox.place(relx=0.045, rely=0.03, relwidth=0.9, relheight=0.9)

        # 提示信息
        # self.labShow['bg'] = 'red'
        self.labShow['text'] = '{}个联系人'.format(len(self.data))
        self.labShow.place(relx=0.045, rely=0.95, relwidth=0.9, relheight=0.05)

    def setData(self, result=None):
        self.listBox.delete(0, tk.END)
        if result is None:
            for i in self.data:
                self.listBox.insert(tk.END, i.name)
            self.labShow['text'] = '{}个联系人'.format(self.listBox.size())
        else:
            for i in result:
                self.listBox.insert(tk.END, i.name)
            self.labShow['text'] = '{}个联系人'.format(self.listBox.size())

def gui():
    # 初始化
    data = []
    data = controller.init()

    # 创建主窗口并设置属性
    root = tk.Tk()
    root.title('Contact')
    root['bg'] = 'white'
    root['width'] = 542
    root['height'] = 442
    root.resizable(0, 0)

    # 添加菜单栏
    Meun(root)

    # 列表部分
    d = dataFrame(data, root)
    d.place(relx=0.02, rely=0.125, relwidth=0.45, relheight=0.85)

    # 搜索部分
    s = searchFrame(d, root)
    s.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    root.mainloop()