# 巢狀迴圈(輸出)
for i in range(1, 4):
    print("外部第", i, "次迴圈,內部執行", i, "次迴圈: ", end="")
    for j in range(1, i+1):
        print("#", end="")
    print()

# 巢狀迴圈(相乘)
for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%d" % (i, j, i*j), end="")
    print()

# 巢狀迴圈(指定範圍輸出)
n = int(input("請輸入正整數:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 巢狀迴圈(最小公倍數)
a = int(input("請輸入a的值: "))
b = int(input("請輸入b的值: "))
for i in range(1, a*b+1):
    if (i % a == 0 and i % b == 0):
        break
print("%d 和  %d 的最小公倍數 = %d" % (a, b, i))

# 巢狀迴圈(印出大樓樓層)
n = int(input("請輸入大樓的樓層數: "))
print("本大樓具有的樓層數:")
# 若大於4層樓，則不顯示4
if(n >= 4):
    n += 1
for i in range(1, n+1):
    if(i == 4):
        continue
    print(i, end="")

# while迴圈
totle = 1
i = 1
n = int(input("請輸入正整數 n 的值: "))
while(i <= n):
    totle *= i
    i += 1
print("%d!=%d" % (n, totle))

# while迴圈(等差級數)
i = 2  # 起始值
n = int(input("請輸入正整數 n 的值: "))
while(i <= n):
    print(i, end=" ")
    i += 2

# while無限迴圈碰上break
while True:
    n = int(input("請輸入正整數n的值(-1代表結束):"))
    if(n == -1):
        break
    for i in range(2, n+1, 2):
        print(i, end=" ")

# range
list1 = range(10)
list2 = range(1, 10)
list3 = range(1, 10, 2)
list4 = range(10, 1, 2)

print(list(list1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(list2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(list3))  # [1, 3, 5, 7, 9]
print(list(list4))  # []

# range(指定範圍)
n = int(input("請輸入正整數:"))
for i in range(1, n+1):
    print(i, end=" ")

# range(指定範圍並計算總合)
n = int(input("請輸入正整數:"))
sum = 0
for i in range(1, n+1):
    sum += i  # 迴圈在這裡結束
print("從1到%d的整數和為%d" % (n, sum))

# range(指定範圍並間隔2)
n = int(input("請輸入正整數:"))
for i in range(1, n+1, 2):
    print(i, end=" ")

# range(指定範圍並計算間隔2的總合)
n = int(input("請輸入正整數:"))
sum = 0
for i in range(1, n+1, 2):
    print(i, end=" ")
    sum += i  # 迴圈在這裡結束
print("\n從1到%d的整數和為%d" % (n, sum))
