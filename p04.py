# 串列(成績)
scores = [85, 79, 93]
print("國文成績:%d" % scores[0])
print("數學成績:%d" % scores[1])
print("英文成績:%d" % scores[2])

# 串列(姓名)
scores = ["林小虎", "王中森", "紹木易"]
print(scores[-1])
print(scores[-2])

# 串列(不同型態)
items = [12, "apple", True]
for i in items:
    print(i, end=",")

# 串列(輸出編號姓名)
list = ["林小虎", "王中森", "紹木易"]
n = 1
for s in list:
    print("編號:%d 姓名:%s" % (n, s))
    n += 1

# 輸出雙串列應用
subjects = ["國文", "數學", "英文"]
scores = [85, 79, 93]
for i in range(len(scores)):
    print("%s成績:%d" % (subjects[i], scores[i]))

# 串列倒著輸出
names = ["林小虎", "王中森", "紹木易"]
n = len(names)  # n會的得到3
for i in range(n-1, -1, -1):
    print(names[i])  # print("姓名:%s % "names[i])

# 串列的塞值與計算長度
scores = []
total = 0
while True:
    inscore = int(input("請輸入學生的成績:"))
    if (inscore == -1):
        break
    scores.append(inscore)
print("共有%d學生" % (len(scores)))
for i in scores:
    total += i
avg = total/len(scores)
print("本班總成績:%d ， 平均成績:%5.2f" % (total, avg))

# 串列的塞值與計算長度
scores = []
total = 0
n = 1
while True:

    inscore = int(input("請輸入第%d天的存款:" % n))
    scores.append(inscore)
    n += 1
    if (n == 8):
        break
for i in scores:
    total += i
print("存款總額:%d " % (total))

# 串列刪除
fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]
while True:
    print("串列元素有:", fruits)
    influit = input("請輸入要刪除的水果(Enter表示結束):")
    if (influit == ""):
        break
    n = fruits.count(influit)
    if (n > 0):
        fruits.remove(influit)
    else:
        print(influit, "不再串列中!")

# 串列排序
scores = []
while True:
    inscore = input("請輸入學生的成績:")
    if (inscore == ""):
        break
    scores.append(int(inscore))
# 再新增一個字串來存放排序過的[]
scores1 = sorted(scores, reverse=True)
print(scores)
print(scores1)

# 串列取出偶數
numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]
odd_numbers = []
for i in numbers:
    if (i % 2 != 0):  # 不等於0
        odd_numbers.append(i)
print(odd_numbers)

# 串列搜尋
fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]
while True:
    infruit = input("請輸入喜歡的水果(Enter表示結束):")
    if (infruit == ""):
        break
    n = fruits.count(infruit)
    if (n > 0):
        # 先找尋他在哪一個位置
        i = fruits.index(infruit)
        print("%s在串列中的第%d項" % (infruit, i+1))
    else:
        print(infruit, "不在串列中!")

# 串列塞值計算成績
scores = []
total = 0
for i in range(1, 6):
    inscore = int(input("請輸入第%d位同學的成績:" % (i)))
    scores.append(inscore)
    total += inscore
avg = total/(len(scores))
print("本班總成績:%d分，平均成績:%5.2f分" % (total, avg))

# 先去2串列看有沒有一樣的(結果丟回n)，如果沒有就加到2裡
numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]
numbers2 = []
for i in numbers:
    n = numbers2.count(i)
    if (n == 0):
        numbers2.append(i)
print(numbers2)


# 取得最高分的索引值，就是排序過後的第一筆:最低就是最後一筆
scores = []
names = []
for i in range(1, 4):
    inname = input("請輸入第%d位同學的名字:" % (i))
    inscore = int(input("請輸入第%d位同學的成績:" % (i)))
    names.append(inname)
    scores.append(inscore)
scores2 = sorted(scores, reverse=True)
n1 = scores.index(scores2[0])
print("姓名:%s , 成績:%d" % (names[n1], scores[n1]))
