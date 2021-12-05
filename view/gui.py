# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 2021/12/5 09:37
# @File: gui.py
# OS: Windows 10
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import tkinter as tk

import utils.controller as controller
import utils.tool as tool

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
    def __init__(self, data, info, master=None):
        tk.Frame.__init__(self, master)
        self.listBox = tk.Listbox(self)
        self.labShow = tk.Label(self)
        self.data = data
        self.info = info
        self.tmpData = data
        self.createWidgets()
        self.listBox.bind("<Double-Button-1>", self.showDetail)
        # self.listBox.bind("<KeyPress-Up>", self.showDetail)
        # self.listBox.bind("<KeyPress-Down>", self.showDetail)

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
            self.tmpData = self.data
        else:
            self.tmpData = result
        for i in self.tmpData:
            self.listBox.insert(tk.END, i.name)
        self.labShow['text'] = '{}个联系人'.format(self.listBox.size())

    def showDetail(self,event):
        for i in self.listBox.curselection():
            # print(type(self.listBox.get(i)), self.listBox.get(i))
            self.info.setData(self.tmpData[i])





# 信息
class infoFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.add = tk.Button(self, text='添加', command=lambda: self.createEventWidgets('ADD'))
        self.update = tk.Button(self, text='修改', command=lambda: self.createEventWidgets('UPDATE'))
        self.delete = tk.Button(self, text='删除')
        self.addY = tk.Button(self, text='确定')
        self.addN = tk.Button(self, text='取消', command=lambda: self.cancel("ADD"))
        self.updateY = tk.Button(self, text='确定')
        self.updateN = tk.Button(self, text='取消', command=lambda: self.cancel("UPDATE"))
        self.data = None
        self.changeData = None
        self.name = None
        self.phone = None
        self.gValue = tk.StringVar(self)
        self.g1 = None
        self.g2 = None
        self.wx = None
        self.createDefaultWidgets()

    def createDefaultWidgets(self):
        name = tk.Label(self, text='姓名: ', anchor=tk.E)
        # name['bg'] = 'red'
        name.place(relx=0.02, rely=0.05, relwidth=0.15, relheight=0.1)
        gender = tk.Label(self, text='性别: ', anchor=tk.E)
        # gender['bg'] = 'blue'
        gender.place(relx=0.02, rely=0.25, relwidth=0.15, relheight=0.1)
        phone = tk.Label(self, text='电话: ', anchor=tk.E)
        # phone['bg'] = 'green'
        phone.place(relx=0.02, rely=0.45, relwidth=0.15, relheight=0.1)
        wx = tk.Label(self, text='微信: ', anchor=tk.E)
        # wx['bg'] = 'yellow'
        wx.place(relx=0.02, rely=0.65, relwidth=0.15, relheight=0.1)

        self.add.place(relx=0.04, rely=0.85, relwidth=0.25, relheight=0.1)
        self.update.place(relx=0.32, rely=0.85, relwidth=0.25, relheight=0.1)
        self.delete.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.1)

    def createEventWidgets(self, eventType):
        nameValue = tk.StringVar(self)
        self.name = tk.Entry(self, textvariable=nameValue)
        self.name.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.1)

        self.g1 = tk.Radiobutton(self, text='男', value='Male', variable=self.gValue)
        self.g2 = tk.Radiobutton(self, text='女', value='Female', variable=self.gValue)
        self.g1.place(relx=0.2, rely=0.25, relwidth=0.2, relheight=0.1)
        self.g2.place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.1)

        phoneValue = tk.StringVar(self)
        self.phone = tk.Entry(self, textvariable=phoneValue)
        self.phone.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.1)

        wxValue = tk.StringVar(self)
        self.wx = tk.Entry(self, textvariable=wxValue)
        self.wx.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)

        self.add.place(relx=0, rely=0, relwidth=0, relheight=0)
        self.update.place(relx=0, rely=0, relwidth=0, relheight=0)
        self.delete.place(relx=0, rely=0, relwidth=0, relheight=0)


        if eventType == 'ADD':
            self.addN.place(relx=0.20, rely=0.85, relwidth=0.25, relheight=0.1)
            self.addY.place(relx=0.50, rely=0.85, relwidth=0.25, relheight=0.1)
        elif eventType == 'UPDATE':
            nameValue.set(self.data.name)
            self.gValue.set(self.data.gender)
            phoneValue.set(self.data.phone)
            wxValue.set(self.data.wx_code)
            self.updateN.place(relx=0.20, rely=0.85, relwidth=0.25, relheight=0.1)
            self.updateY.place(relx=0.50, rely=0.85, relwidth=0.25, relheight=0.1)

    def createInfoWidgets(self):
        nameValue = tk.Label(self, text=self.data.name, anchor=tk.W)
        # name['bg'] = 'red'
        nameValue.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.1)
        genderValue = tk.Label(self, text=self.data.gender, anchor=tk.W)
        # gender['bg'] = 'blue'
        genderValue.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)
        phoneValue = tk.Label(self, text=self.data.phone, anchor=tk.W)
        # phone['bg'] = 'green'
        phoneValue.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.1)
        wxValue = tk.Label(self, text=self.data.wx_code, anchor=tk.W)
        # wx['bg'] = 'yellow'
        wxValue.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)

    def setData(self, data=None):
        if data is not None:
            self.data = data
        self.createInfoWidgets()

    def addContact(self):
        pass

    def updateContact(self):
        name = self.name.get()
        gender = self.gValue.get()
        phone = self.phone.get()
        wx = self.wx.get()


    def cancel(self, eventType):
        if eventType == 'ADD':
            self.addN.place(relx=0, rely=0, relwidth=0, relheight=0)
            self.addY.place(relx=0, rely=0, relwidth=0, relheight=0)
        elif eventType == 'UPDATE':
            self.updateN.place(relx=0, rely=0, relwidth=0, relheight=0)
            self.updateY.place(relx=0, rely=0, relwidth=0, relheight=0)
        self.setData()
        self.add.place(relx=0.04, rely=0.85, relwidth=0.25, relheight=0.1)
        self.update.place(relx=0.32, rely=0.85, relwidth=0.25, relheight=0.1)
        self.delete.place(relx=0.60, rely=0.85, relwidth=0.25, relheight=0.1)

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

    # details info
    i = infoFrame(root)
    i.place(relx=0.4, rely=0.125, relwidth=0.55, relheight=0.85)
    i.setData(data[0])

    # 列表部分
    d = dataFrame(data, i, root)
    d.place(relx=0.02, rely=0.125, relwidth=0.35, relheight=0.85)

    # 搜索部分
    s = searchFrame(d, root)
    s.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    root.mainloop()
