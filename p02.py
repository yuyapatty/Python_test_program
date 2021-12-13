# 輸入密碼(判斷密碼)
pw = input("請輸入密碼:")
if pw == "1234":
    print("歡迎光臨!")

pw = input("請輸入密碼:")
if pw == "1234":
    print("歡迎光臨!")
else:
    print("密碼錯誤!")

# 輸入成績(判斷及格)
score = int(input("請輸入成績:"))
if score >= 60:
    # 老師(score>=60):
    print("讚!成績及格")
else:
    print("成績不及格，加油喔!")

# 輸入成績(判斷等級)
score = int(input("請輸入成績:"))
if score >= 90:
    print("優等")
elif score >= 80:  # 每次都從第一列開始檢查
    print("甲等")
elif score >= 70:
    print("乙等")
elif score >= 60:
    print("丙等")
else:
    print("丁等")

# 輸入年齡(判斷收看等級)
age = int(input("請輸入年齡:"))
if age <= 5:
    print("可看普遍級")
elif age <= 11:
    print("可看普遍級及保護級")
elif age <= 17:
    print("可看限制級以外的電影")
else:
    print("您已成年，可看各級影片!")

# 輸入金額(判斷後打折)
money = int(input("請輸入購物金額:"))
if (money >= 10000):
    if(money >= 100000):
        print(money*0.8, end=" 元\n")
    elif(money >= 50000):
        print(money*0.85, end=" 元\n")
    elif(money >= 30000):
        print(money*0.9, end=" 元\n")
    else:
        print(money*0.95, end=" 元\n")
else:
    print(money, end=" 元\n")

# 輸入數值(比較大小)
a = int(input("請輸入a的值:"))
b = int(input("請輸入b的值:"))
c = int(input("請輸入c的值:"))
if a > b:
    if a > c:
        print("最大值為 %d" % (a))
    else:
        print("最大值為 %d" % (c))
else:
    if b > c:
        print("最大值為 %d" % (b))
    else:
        print("最大值為 %d" % (c))
