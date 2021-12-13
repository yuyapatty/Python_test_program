# 字典宣告
dic1 = {"A": "內向穩重", "B": "外向樂觀"}

# 字典宣告並檢查是否對應
# dict1={"A":"內向穩重","B":"外向樂觀","o"}
# dict1=dict([["A","內向穩重"],["B","外向樂觀"],["O","自信堅強"],["AB","聰明自然"]])
dict1 = dict(春季="暖和", 夏季="炎熱", 秋季="涼爽", 冬季="寒冷")
name = input("輸入季節名稱:")
season = dict1.get(name)
if season == None:
    print("沒有" + "name" + "季節!")
else:
    print(name + "的天氣為:" + dict1[name])
dict1.clear()
print(dict1)

# 字典宣告並檢查是否對應
dict1 = {"林小明": 85, "曾山水": 93, "鄭美麗": 67}
name = input("輸入學生姓名:")
if name in dict1:
    print(name + "的成績為:" + str(dict1[name]))
else:
    score = int(input("輸入學生分數:"))
    dict1[name] = score
    print("字典內容:" + str(dict1))

# 字典宣告並檢查是否對應
dict1 = {"電視": 15000, "冰箱": 23000, "冷氣": 28000}
name = input("輸入電器名稱:")
if name in dict1:
    print(name + "的價格為:" + str(dict1[name]))
else:
    price = int(input("輸入%s電器價格:" % (name)))
    dict1[name] = price
    print("字典內容:" + str(dict1))

# 字典應用分別取出索引與值
dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的%s 數目為 %d 面" % (listkey[i], listvalue[i]))

# 字典應用分別取出索引與值
dict1 = {"水瓶座": "活潑善良", "雙魚座": "迷人保守", "白羊座": "天生勇者", "金牛座": "熱情敏感"}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print(" %s 的性格特徵為 %s " % (listkey[i], listvalue[i]))

# 字典應用
dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
item1 = dict1.items()
for i, j in item1:
    print("得到的%s 數目為 %d 面" % (i, j))

# 字典應用
dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
listitem = list(dict1.items())
for i in range(len(listitem)):
    print(listitem[i])

# 集合
全班學生 = set(["John", "Mary", "Tina", "Fiona",
           "Claire", "Eva", "Ben", "Bill", "Bert"])
英文及格 = set(["John", "Mary", "Fiona", "Claire", "Ben", "Bill"])
數學及格 = set(["Mary", "Fiona", "Claire", "Eva", "Ben"])
print("英文與數學都及格:", 英文及格 & 數學及格)
print("數學不及格:", 全班學生-數學及格)
print("英文及格且數學不及格:", 英文及格 & (全班學生-數學及格))

# 字典查詢
dict1 = {"台北市": 6, "新北市": 2, "桃園市": 5, "台中市": 8, "台南市": 3, "高雄市": 9}
city = input("輸入要查詢的六都名稱:")
if city in dict1:
    print(city + "今天的PM2.5為: " + str(dict1[city]))
else:
    print("六都中沒有「" + city + "」城市!")

# 字典應用
dict1 = {"鼠": "親切和藹", "牛": "保守努力", "虎": "熱情大膽", "兔": "溫柔仁慈"}
# item1=dict1.items()
item1 = list(dict1.items())
for i, j in item1:
    print("生肖屬%s 的性格特徵為 %s " % (i, j))
