# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:56:13 2021

@author: YY
"""
# 網頁資料數據讀取
import json
from bs4 import BeautifulSoup
import requests

url = 'https://api.kcg.gov.tw/api/service/get/c55d9817-a7b9-45c9-82e8-fc542bc05d0f'
myweb = requests.get(url)
myweb.encoding = 'utf-8'
print(myweb.text)

# 網頁資料數據讀取並夾帶簡短的查詢參數（例如搜尋關鍵字等）
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/get'
myweb = requests.get(url, params=payload)
myweb.encoding = 'utf-8'
print(myweb.text)

# 網頁資料讀取，用BeautifulSoup抓取(lxml)

url = 'http://www.powenko.com/wordpress/'
myweb = requests.get(url)
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
print(myweb.title.text)

# 網頁資料讀取，用BeautifulSoup抓取(html.parser)

req = requests.get('http://www.powenko.com/wordpress/')
# myweb=requests.get(req)
# myweb.encoding='utf-8'
sp = BeautifulSoup(req.text.encode('utf-8'), 'html.parser')
print(sp.title)

# 網頁資料讀取，用BeautifulSoup抓取(lxml)，應用
# bit.ly/3cOLD1K
url = 'https://teacher2.kyu.edu.tw/wutopia/example.html'
myweb = requests.get(url)
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
ques = sp.find_all('a')
quess = []
for item in ques:
    quess.append(item.text)
print(quess)

# 網頁資料讀取，用BeautifulSoup抓取(lxml)，應用
# bit.ly/3cOLD1K
url = 'https://teacher2.kyu.edu.tw/wutopia/example.html'
myweb = requests.get(url)
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
ques = sp.find(id='q2')
print(ques.find_all(True))

# 大樂透

url = 'https://www.taiwanlottery.com.tw/'
myweb = requests.get(url)
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')  # lxml解析器
results = sp.find_all('div', class_='contents_box02')
# 因為有很多個<div>
print('大樂透')
# 抓出大樂透的區塊results[2]
# 按照想要的印出
print(results[2].find('span', class_='font_black15').text + '開獎結果')
# 印出串列的所有數字(一般號)class_='ball_tx ball_yellow'
balls = results[2].find_all('div', class_='ball_tx ball_yellow')
# print(balls[0].text)
print('開出順序:', end=' ')
for i in range(0, 6):
    print(balls[i].text, end='')
print('\n大小順序:', end=' ')
for i in range(6, len(balls)):
    print(balls[i].text, end='')
# 特別號，class="ball_red"
print('\n特別號:', results[2].find('div', class_='ball_red').text)
# \n跳行
# 下面印出威力彩
print('威力彩')
balls2 = results[0].find_all('div', class_='ball_tx ball_green')
print('開出順序:', end=' ')
for i in range(0, 6):
    print(balls2[i].text, end='')


# ptt八卦版，取得最新貼文

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
myweb = requests.get(url, cookies={'over18': '1'})  # 跟cookies說滿18歲
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')


posts = sp.find_all('div', class_='r-ent')

# print(posts)
for post in posts:
    print('標題', post.find('a').text)
    print('作者', post.find('div', class_='author').text)
    print('連結', post.find('a')['href'])
    print('推文', post.find('div', class_='nrec').text)
    print()


# 網頁資料讀取，用BeautifulSoup抓取(lxml)，存成jason檔

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
myweb = requests.get(url, cookies={'over18': '1'})  # 跟cookies說滿18歲
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
jdata = []

posts = sp.find_all('div', class_='r-ent')

with open('ptt.json', 'w', encoding='utf-8') as f:
    for post in posts:
        title = post.find('a').text
        author = post.find('div', class_='author').text
        link = post.find('a')['href']
        push = post.find('div', class_='nrec').text
        jdata.append({'標題': title, '作者': author, '連結': link, '推文': push})
    json.dump(jdata, f, ensure_ascii=False)
    # 預設True意思是全英文，有中文要設False

# 翻頁爬取練習，只有提示

page = 39222
url = 'https://www.ptt.cc/bbs/Gossiping/index' + str(page) '.html'

myweb = requests.get(url, cookies={'over18': '1'})  # 跟cookies說滿18歲
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
posts = sp.find_all('div', class_='r-ent')
jdata = []

# 電影

url = 'https://movies.yahoo.com.tw/movie_comingsoon.html'

myweb = requests.get(url)
myweb.encoding = 'utf-8'
sp = BeautifulSoup(myweb.text, 'lxml')
posts = sp.find_all('div', class_='release_info')
print(posts[0].find('div', class_='release_movie_name').a.text.strip())
print(posts[0].find('div', class_='en').a.text.strip())  # strip()刪除字串前後的空白
print(posts[0].find('div', class_='realse_movie_time').text.replace('上映日期:', '')
print(posts[0].find('div', class_='leveltext').span.text.strip())
print(posts[0].find('div', class_='release_text').span.text.strip())


# 正規化
# https://regex101.com/
import re
html=< div class="content" >
  Email:
  < a href="mailto:service1@test.com.tw" > mail1 < /a > <br >
  < a href="mailto:Andy@test.com.tw" > mail2 < /a > <br >
  < ul class="price" > 定價: 360元 < /ul >
  < img src="http://test.com.tw/p1.jpg" >
  < img src="http://test.com.tw/p2.jpg" >
  < img src="http://test.com.tw/p3.png" >
  電話: (07)696-7777, (07)696-7778
  手機: 0912-345678, 0935-001534
< /div >


emails=re.findall(r'[a-zA-Z0-9\._-]+@[a-zA-Z-9\._-]+', html)
print(emails)

prices=re.findall(r'[0-9]+元', html)
# print(prices[0])
# print(prices[0].split('元')[0])
prices=re.findall(r'[0-9]+元', html)[0].split('元')[0]
print(prices)

# 爬蟲Dcard
import requests
from bs4 import BeautifulSoup

url='https://www.dcard.tw/f'

myweb=requests.get(url)
myweb.encoding='utf-8'
sp=BeautifulSoup(myweb.text, 'lxml')
arts=sp.find_all('article')
# recursive會做執行遞迴的動作
for art in arts:
    div=art.find_all('div', recursive=False)
    print('標題:', art.find('h2').text)
    print('作者:', div[0].text)
    print('內文:', div[1].text)
    print('愛心數:', div[2].div.text)
    print('回應數:', div[2].span.text)
    print('===================')


# chrome_臺銀法拍屋
# 步驟ㄧ、先看能不能執行
from selenium import webdriver
from bs4 import BeautifulSoup
url='https://www2.bot.com.tw/house/default.aspx'

myweb=webdriver.Chrome()
myweb.get(url)
myweb.find_element_by_id('fromdate_TextBox').send_keys('1090101')
# 拍賣期間起日1090101、迄日10901231
myweb.find_element_by_id('todate_TextBox').send_keys('1091231')
# 地區選擇台中市
myweb.find_element_by_id('country_DDL').send_keys('台中市')
# 查詢的動作，查詢按鈕
myweb.find_element_by_id('Submit_Button').click()
# 先看能不能執行

# 步驟二、印出來看看
from selenium import webdriver
from bs4 import BeautifulSoup

url='https://www2.bot.com.tw/house/'
myweb=webdriver.Chrome()
myweb.get(url)
myweb.find_element_by_id('fromdate_TextBox').send_keys('1090101')
# 拍賣期間起日1090101、迄日10901231
myweb.find_element_by_id('todate_TextBox').send_keys('1091231')
# 地區選擇台中市
myweb.find_element_by_id('country_DDL').send_keys('台中市')
# 查詢的動作，查詢按鈕
myweb.find_element_by_id('Submit_Button').click()

sp=BeautifulSoup(myweb.page_source, 'lxml')
# 表格
results=sp.find('table', id='House_GridView')
for row in results.find_all('tr'):
    print([s for s in row.stripped_strings])  # 印出來檢查

# 寫入一個csv檔
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
url='https://www2.bot.com.tw/house/default.aspx'

myweb=webdriver.Chrome()
myweb.get(url)
myweb.encoding='utf-8'
myweb.find_element_by_id('fromdate_TextBox').send_keys('1090101')
# 拍賣期間起日1090101、迄日10901231
myweb.find_element_by_id('todate_TextBox').send_keys('1091231')
# 地區選擇台中市
myweb.find_element_by_id('country_DDL').send_keys('台中市')
# 查詢的動作，查詢按鈕
myweb.find_element_by_id('Submit_Button').click()
sp=BeautifulSoup(myweb.page_source, 'lxml')
# 表格
results=sp.find('table', id='House_GridView')
# 寫入
with open('bothouse.csv', 'w', encoding='utf-8-sig', newline='')as f:
    writer=csv.writer(f)
    for row in results.find_all('tr'):
        writer.writerow([s for s in row.stripped_strings])
myweb.quit()


# 台鐵時刻表
# 步驟ㄧ、先看能不能執行
from selenium import webdriver
from bs4 import BeautifulSoup
url='https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime'

myweb=webdriver.Chrome()
myweb.get(url)
# id和name一樣
myweb.find_element_by_id('startStation').send_keys('4220-臺南')
# id和name一樣
myweb.find_element_by_id('endStation').send_keys('4400-高雄')
# 日期，先清除原有預設的資料
myweb.find_element_by_id('rideDate').clear()
myweb.find_element_by_id('rideDate').send_keys('20210710')

myweb.find_element_by_id('startTime').send_keys('08:00')
myweb.find_element_by_id('endTime').send_keys('09:00')
# 出現錯誤不能使用id找，改用label找還是找不到"對號"按鈕，查看網頁原始碼搜尋"<label"，是在第16個
# 方法1:
myweb.find_elements_by_tag_name('label')[15].click()
# myweb.find_elements_by_xpath('//form/div/div[3]/div/div[2]/label[2]')
# ^方法2:用路徑來找//*[@id="queryForm"]/div[1]/div[3]/div[1]/div[2]/label[2]

myweb.find_element_by_name('query').click()
sp=BeautifulSoup(myweb.page_source, 'lxml')
results=sp.find('table', class_='itinerary-controls')
for row in results.find_all('tr'):
    print([s for s in row.stripped_strings])
