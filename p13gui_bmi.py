# 計算BMI互動視窗
from tkinter import *

win = Tk()
win.title('新尖兵訓練班')
win.geometry('400x200')


def find_BMI():
    height = float(h_entry.get())
    weight = float(w_entry.get())
    bmi = round(weight/(height/100)**2, 2)
    if bmi < 18.5:
        status = ', 體重太輕, 要多吃一點'
        result.config(fg='GREEN')
    elif bmi >= 24:
        status = ', 體重過重, 需要控制一下'
        result.config(fg='RED')
    else:
        status = ', 體重適中, 請繼續保持'
        result.config(fg='BLUE')
    result.config(text='你的BMI為 '+str(bmi)+status)


title = Label(win, text='BMI計算器', font='微軟正黑體 18 bold', fg='BLUE')
title.pack()
hf = Frame(win)
hf.pack()
h_label = Label(hf, text='身高(公分)', height=2)
h_label.pack(side=LEFT)
h_entry = Entry(hf, width=30)
h_entry.pack(side=LEFT)
wf = Frame(win)
wf.pack()
w_label = Label(wf, text='體重(公斤)', height=2)
w_label.pack(side=LEFT)
w_entry = Entry(wf, width=30)
w_entry.pack(side=LEFT)
btn = Button(win, text='計算BMI', command=find_BMI)
btn.pack()
result = Label(win, height=2)
result.pack()

win.mainloop()
