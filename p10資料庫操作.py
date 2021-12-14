# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 13:57:46 2021

@author: YY
"""
# 建立空資料表CREATE TABLE
import sqlite3

conn = sqlite3.connect('db.sqlite')
sql = "CREATE TABLE student ('學號' TEXT PRIMARY KEY NOT NULL, '姓名' TEXT, '電話' TEXT)"
conn.execute(sql)
conn.commit()
conn.close()

# 修改資料表ALTER TABLE

conn = sqlite3.connect('db.sqlite')
# 增加欄位
#sql="ALTER TABLE student ADD 地址 TEXT "
#sql="ALTER TABLE student DROP 地址 "
sql = "INSERT INTO student  VALUES('1','王大明','0912345678')"

conn.execute(sql)
conn.commit()
conn.close()

# 執行資料查詢

conn = sqlite3.connect('db.sqlite')
# 讀取、查詢資料
sql = "SELECT * FROM employee"  # 沒有條件就是印出全部
cursor = conn.execute(sql)
rows = cursor.fetchall()
print(rows)  # 串列的型式
conn.commit()
conn.close()

# 執行資料查詢(加上條件)

conn = sqlite3.connect('db.sqlite')
# 讀取、查詢資料，SELECT接查詢哪個欄位
# where
#sql="SELECT Name, address FROM employee WHERE Name like '陳%' and address like '台北%'"
#sql="SELECT Name, Salary, Blood_Type, Gender FROM employee WHERE gender='男' and salary > 50000 and Blood_Type='A' "
sql = "SELECT Name, Blood_Type, Gender FROM employee WHERE (gender='男' and Blood_type='A') or (gender='女' and Blood_type='B')"
cursor = conn.execute(sql)
rows = cursor.fetchall()
for row in rows:
    # print(row[0], row[1], row[2], row[3])#顯示的欄位，第2題要4個
    print(row[0], row[1])
conn.commit()
conn.close()

# 更新資料

conn = sqlite3.connect('db.sqlite')

sql =
UPDATE employee
SET Salary = Salary+2000
WHERE Salary < 20000

conn.execute(sql)
conn.commit()
conn.close()
