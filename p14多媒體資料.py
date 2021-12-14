# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 09:46:49 2021

@author: YY
"""
# 下載YouTube影片
from tkinter import *
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=tJM0yIbg8iQ')
print(yt.title)
print(yt.views)
print(yt.streams.filter(subtype='mp4', progressive=True).order_by('resolution').desc())
print(yt.caption['en'].generate_srt_caption())


print('開始下載...')
yt.streams.first().download()
print(yt.title, '...下載完成')

# 做一個讓使用者可下載YouTube影片的工具
win = Tk()
win.title('YouTube Download')
win.geometry('800x200')


def download():
    src = h_entry.get()
    des = h_entry.get()
    yt = YouTube(src)
    result.config(text='開始下載...')
    yt.streams.filter(subtype='mp4', progressive=True).order_by(
        'resolution').desc().first().download(des)
    result.config(text=yt.title + ' ...下載完成')


title = Label(win, text='Youtube下載器', font='微軟正黑體 18 bold', fg='BLUE')
title.pack()
hf = Frame(win)
hf.pack()
h_label = Label(hf, text='影片網址', height=2)
h_label.pack(side=LEFT)
h_entry = Entry(hf, width=60)
h_entry.pack(side=LEFT)
wf = Frame(win)
wf.pack()
w_label = Label(wf, text='儲存路徑', height=2)
w_label.pack(side=LEFT)
w_entry = Entry(wf, width=60)
w_entry.pack(side=LEFT)
btn = Button(win, text='下載', command=download)
btn.pack()
result = Label(win, height=5)
result.pack()

win.mainloop()
