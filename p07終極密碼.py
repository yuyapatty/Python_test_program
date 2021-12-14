# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:40:12 2021

@author: YY
"""
# 終極密碼1 執行一次
import tkinter as tk
from calendar import month
import random
# randint包含最後一個數
min = 0
max = 100
passwd = random.randint(1, 99)
print('終極密碼 %d ~ %d:' % (min, max), end='')
n = eval(input('輸入猜測:'))
if n <= min or n >= max:
    print('輸入範圍錯誤')
elif n > passwd:
    max = n
elif n < passwd:
    min = n
else:
    print('猜中了')

# 終極密碼2 加入迴圈
# randint包含最後一個數
min = 0
max = 100
passwd = random.randint(1, 99)
n = 0
while n != passwd:
    print('終極密碼 %d ~ %d' % (min, max), end='')
    n = eval(input('輸入猜測:'))
    if n <= min or n >= max:
        print('輸入範圍錯誤')
    elif n > passwd:
        max = n
    elif n < passwd:
        min = n
    else:
        print('猜中了')

# 終極密碼3 是否再玩一次
# randint包含最後一個數
min = 0
max = 100
passwd = random.randint(1, 99)
n = 0
while n != passwd:
    print('終極密碼 %d ~ %d' % (min, max), end='')
    n = eval(input('輸入猜測:'))
    if n <= min or n >= max:
        print('輸入範圍錯誤')
    elif n > passwd:
        max = n
    elif n < passwd:
        min = n
    else:
        print('猜中了')
        ans = input('是否再玩一次?(Y/N):')
        if ans.upper() == 'Y':
            # upper把答案轉成大寫，再來比
            min = 0
            max = 100
            passwd = random.randint(1, 99)
            n = 0

# GUI
# 日曆
print(month(2020, 7))

# 挑出視窗
win = tk.Tk()
win.title('新尖兵')
win.geometry('400x200')
win.mainloop()

# 跳出視窗2
win = tk.Tk()
win.title('新尖兵')
win.geometry('200x100')


def sayhello():
    label1['text'] = 'Hello World!'


label1 = tk.Label(win, text='大家好')
btn1 = tk.Button(win, text='Say Hello', command=sayhello)
label1.pack()
btn1.pack()
win.mainloop()

# 跳出視窗3
win = tk.Tk()
win.title('新尖兵')
win.geometry('200x100')


def sayhello():
    label1['text'] = 'Hello' + entry1.get()


    # .get
label1 = tk.Label(win, text='請輸入姓名:')
entry1 = tk.Entry(win, width=30)
btn1 = tk.Button(win, text='確定', command=sayhello)
label2 = tk.Label(win)
label1.pack()
entry1.pack()
btn1.pack()
label2.pack()
win.mainloop()

# 跳出視窗4
win = tk.Tk()
win.title('新尖兵')
win.geometry('200x100')


def sayhello():
    messagebox.showinfo('Greeting', 'Hello' + entry1.get())


    #
label1 = tk.Label(win, text='請輸入姓名:')
entry1 = tk.Entry(win, width=30)
btn1 = tk.Button(win, text='確定', command=sayhello)

label1.pack()
entry1.pack()
btn1.pack()

win.mainloop()
