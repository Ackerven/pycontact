# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 2021/12/5 09:37
# @File: gui.py
# OS: Windows 10
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

import tkinter as tk

def gui():
    # 创建主窗口并设置属性
    root = tk.Tk()
    root.title('Contact')
    root['width'] = 542
    root['height'] = 442
    root.resizable(0, 0)

    root.mainloop()
