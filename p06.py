#函式宣告與應用
def ctof(c):
    f=c*1.8+32
    return f

inputc=float(input("請輸入攝氏溫度:"))
print("華氏溫度為:%5.1f度" % ctof(inputc))

#函式宣告與應用
def getarea(width):
    return width*width

print(getarea(6))

#函式宣告與應用
def getarea(width,height=12):
    return width*height

print(getarea(6, 9))#答案會依輸入的為準

#區域與全域變數
def scope():
    var1=1
    print(var1, var2)

var1=10
var2=20
scope()
print(var1, var2)

#區域與全域變數(變更全域)
def scope():
    global var1
    var1=1
    var2=2
    print(var1, var2)

var1=10
var2=20
scope()
print(var1, var2)

#divmod函式應用
preson=int(input("請輸入學生人數:"))
apple=int(input("請輸入蘋果總數:"))
ret=divmod(apple, preson)
print("每個學生可分得蘋果" + str(ret[0]) + "個")
print("蘋果剩餘" + str(ret[1]) + "個")

#多個函式應用
list1=[]
while True:
    innum=int(input("請輸入電費(-1:結束):"))
    #先判別有沒有=-1
    if (innum==-1):
        break
    list1.append(innum)#新增到串列
#先計算串列個數
print("共輸入 %d 個數" % (len(list1)))
print("最多電費為 : %d 元" % (max(list1)))
print("最少電費為 : %d 元" % (min(list1)))
print("電費由大牌到小為 : {}".format(sorted(list1, reverse=True)))
   
#startswith函式應用
web=input("請輸入網址:")
if (web.startswith("http://") or web.startswith("https://")):
    print("輸入的網址格是正確!")
else:
    print("輸入的網址格式不正確!")
    
#endswith函式應用
picture=input("請輸入圖片檔案名稱:")
if (picture.endswith(".jpg")):
    print("圖片格式是jpg!")
else:
    print("圖片格式不是jpg!")
    
#ljust與rjust應用
listname=["林大明","陳阿中","張小英"]
listchi=[100,74,82]
listmath=[87,88,65]
listeng=[79,100,8]
print("姓名    座號   國文   數學   英文")
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchi[i]).rjust(5), str(listmath[i]).rjust(5), str(listeng[i]).rjust(5))

#ljust與rjust應用
listname=["鐘明達","鄭廣月","何美麗"]
list1=[34210,]
list2=[23600,23900,127800,125000]
list3=[145000,83400,10000,90000]

print("姓名       第一季   第二季   第三季   第四季")
for i in range(0,3):
    print(listname[i].ljust(5), str(listchi[i]).rjust(7), str(listmath[i]).rjust(7), str(listeng[i]).rjust(7))

#find與replaced函式應用
str1="I love Python"
print(str1.find("o"))
print(str1.find("p"))
print(str1.replace("o", "&"))
print(str1.replace("o", "&", 1))
print(str1.replace("o", ""))
print(str1.replace("Python", "c"))

#replace函式應用
date1="2017-8-23"
date1="西元 " + date1
date1=date1.replace("-"," 年",1)
date1=date1.replace("-"," 月",1)
date1+=" 日"
print(date1)

#replace函式應用
time1="10:23:41"
time1=time1.replace(":","點 ",1)
time1=time1.replace(":","分 ",1)
time1+=" 秒"
print(time1)

#randint模組應用
import random as r
while True:
    inkey=input("按任意鍵再按Enter鍵表示擲骰子，直接按Enter鍵表示 結束:")
    if len(inkey)>0:
        num=r.randint(1, 6)
        print("你擲的骰子點數為: " + str(num) + "點")
    else:
        print("遊戲結束")
        break

#randint函式猜數字
import random as r
while True:
    num=r.randint(1, 6)
    inkey=int(input("請輸入你猜的骰子點數(-1表示結束:):"))
    if (inkey==-1):
        break
    print("系統的骰子點數為: " + str(num) + "點")
    print("你擲的骰子點數為: " + str(inkey) + "點")
    if (inkey>num):
        print("\n恭喜!你贏了")
    elif(inkey==num):
        print("平手!")
    else:
        print("你輸了!")
        
#多個函式應用
import random as r
list1=r.sample(range(1,50), 7)
special=list1.pop()#pop()取出最後一個元素並由串列中移除元素
list1.sort()#sort排序
print("本期大樂透中獎號碼為: ", end="")#此end示要跳一行
for i in range(6):
    if i==5:#為了讓最後一號後面不要有","
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=", ")
print("本期大樂透特別號為:" + str(special))

#time模組
import time as t
print(t.time())
print(t.localtime())
print(t.ctime())

