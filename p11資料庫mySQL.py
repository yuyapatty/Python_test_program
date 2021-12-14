# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:51:29 2021

@author: YY
"""
# 讀取mySQL
# 原型
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='yuya', password='yuya',
                       charset='utf8', db='empdb')

cursor = conn.cursor()
sql = "  "

cursor.execute(sql)

conn.commit()  # 更新
conn.close()  # 關閉連線

# 增加

conn = pymysql.connect(host='localhost', port=3306, user='yuya', password='yuya',
                       charset='utf8', db='empdb')

cursor = conn.cursor()
sql = "SELECT * FROM 員工"

cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    print(item)
conn.commit()
conn.close()

# 修改欄位資料(部門代號)

conn = pymysql.connect(host='localhost', port=3306, user='yuya', password='yuya',
                       charset='utf8', db='empdb')

cursor = conn.cursor()
sql = "ALTER TABLE 員工 DROP 部門代號"

cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    print(item)
conn.commit()
conn.close()

# 開啟empdb資料庫，查詢員工資料表，執行以下指令，並列印出查詢結果:
# 1.查詢副理級職的員工，分別計算男女員工總數。
# 2.查詢工程師的平均薪資，男女員工分開計算，並將平均薪資由大到小排序

conn = pymysql.connect(host='localhost', port=3306, user='yuya', password='yuya',
                       charset='utf8', db='empdb')
cursor = conn.cursor()
sql =
SELECT 性別, AVG(薪資)
FROM 員工
WHERE 現任職稱 like '%工程師'
GROUP BY 性別
ORDER BY AVG(薪資) DESC


sql =
SELECT 性別, COUNT(*)
FROM 員工
WHERE 現任職稱 like '%副理'
GROUP BY 性別


cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    print(item[0], item[1])
conn.commit()
conn.close()
