#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
# import easygui

from tkinter.messagebox import *


def showHelloMessage():
    #    tkinter.messagebox.showinfo(title=None, message="text!!!!!!!!!!!!!")

    # Ask if operation should proceed; return true if the answer is ok
       tkinter.messagebox.askokcancel(title=None, message="立即生效?")

    # Ask a question
       tkinter.messagebox.askquestion(title=None, message="OK????")
    # Ask if operation should be retried; return true if the answer is yes
       tkinter.messagebox.askretrycancel(title=None, message=None)



# top = tkinter.Tk()

# frame1 = tkinter.Frame(top)
# top.title("MM32-LINK Configure Tool")

# CheckVar1 = tkinter.IntVar()
# C1 = tkinter.Checkbutton(top, text = "RUNOOB", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
# C1.pack()

# listbox1 = tkinter.Listbox()
# tkinter.Listbox()

# B = tkinter.Button(top, text ="click me", command = showHelloMessage)
# B.pack(padx=300,pady=150)

# 进入消息循环
# top.mainloop()

from tkinter import *
# 创建主窗口
win = Tk()
win.title("MM32-LINK TOOL")
win.geometry('400x200')
win.iconbitmap('./img/logo.ico')
# 创建列表选项
listbox1 =Listbox(win)
listbox1.pack()
# i表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(["Power off","5V","3.3V","BEEP ON","BEEP OFF"]):
    listbox1.insert(i,item)
# 显示窗口
win.mainloop()