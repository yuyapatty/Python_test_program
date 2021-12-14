# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:53:59 2021

@author: YY
"""
# 報名表1
# laout 框框
from tkinter import *
win = Tk()
win.title('研討會報名')
win.geometry('400x200')

label = Label(win, text='報名表', font='標楷體 18 bold').pack()
cvar1 = BooleanVar()
cvar2 = BooleanVar()
# 看有沒有打勾看cvar這個變數
c1 = Checkbutton(win, text='上午場', variable=cvar1, height=2).pack()
c2 = Checkbutton(win, text='下午場', variable=cvar1, height=2).pack()
submit = Button(win, text='送出', command=confirm).pack()
win.mainloop()

# 加入執行 報名表2
win = Tk()
win.title('研討會報名')
win.geometry('400x200')


def confirm():
    result = '您報名了'
    if cvar1.get():  # 或cvar1.get()== True
        result += '上午場'
    if cvar2.get():
        result += '下午場'
    if result == '您報名了':
        result = '您沒有報名任何場次'
    messagebox.showinfo('報名表', result)


label = Label(win, text='報名表', font='標楷體 18 bold').pack()
cvar1 = BooleanVar()
cvar2 = BooleanVar()
# 看有沒有打勾看cvar這個變數
c1 = Checkbutton(win, text='上午場', variable=cvar1, height=2).pack()
c2 = Checkbutton(win, text='下午場', variable=cvar2, height=2).pack()
submit = Button(win, text='送出', command=confirm).pack()
win.mainloop()

# 報名表3
win = Tk()
win.title('研討會報名')
win.geometry('400x200')


def confirm():
    result = '您報名了'
    if rvar.get() == 1:  # 或cvar1.get()== True
        result += '上午場'
    elif rvar.get() == 2:
        result += '下午場'
    else:
        result = '您沒有報名任何場次'
    messagebox.showinfo('報名表', result)


label = Label(win, text='報名表', font='標楷體 18 bold').pack()
rvar = IntVar()
# 看有沒有打勾看cvar這個變數
# Radiobutton共用一個變數
r1 = Radiobutton(win, text='上午場', variable=rvar, height=2, value=1).pack()
r2 = Radiobutton(win, text='下午場', variable=rvar, height=2, value=2).pack()
submit = Button(win, text='送出', command=confirm).pack()
win.mainloop()

# 選單1
win = Tk()
win.title('選單')
win.geometry('400x200')
menubar = Menu(win)
filemenu = Menu(menubar)
menubar.add_cascade(label='檔案', menu=filemenu)
filemenu.add_command(label='開新檔案')
filemenu.add_command(label='儲存檔案')
filemenu.add_command(label='另存新檔')
filemenu.add_command(label='結束')

win.config(menu=menubar)
win.mainloop()

# 選單2
win = Tk()
win.title('選單')
win.geometry('400x200')
menubar = Menu(win)
filemenu = Menu(menubar)
menubar.add_cascade(label='檔案', menu=filemenu)
filemenu.add_command(label='開新檔案')
filemenu.add_command(label='儲存檔案')
filemenu.add_command(label='另存新檔')
filemenu.add_command(label='結束')

win.config(menu=menubar)
win.mainloop()
