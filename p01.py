#輸出學生成績資料
print("姓名  座號  國文  數學  英文")
print("%3s  %2d  %3d  %3d  %3d" % ("林大明",1,100,87,79))
print("%3s  %2d  %3d  %3d  %3d" % ("陳阿中",2,74,88,100))
print("%3s  %2d  %3d  %3d  %3d" % ("張小英",11,82,65,80))

print("年分  2012  2013  2014  2015")
print("%4d  %2.1f  %3.1f  %3.1f  %3.1f"%(2012,2.2,74.23,1.2,12.1))

#計算總分 
chi=int(input("請輸入國文成績:"))
eng=int(input("請輸入英文成績:"))
math=int(input("請輸入數學成績:"))
total=chi+eng+math
#print("你的成績總分為:" + str(total))
print("你的成績總分為:%d"%(total))

#輸出2位同學的成績與總分
name1=str(input("請輸入第一位同學的姓名:"))
score1=int(input("請輸入第一位同雄的成績:"))
name2=str(input("請輸入第二位同學的姓名:"))
score2=int(input("請輸入第二位同學的成績:"))

print("姓名  成績")
print("%3s  %3d " % (name1,score1))
print("%3s  %3d " % (name2,score2))
total=score1+score2
print("成績總分為:%d"%(total))

#計算長方形面積
length=float(input("請輸入長方形長度:"))
width=float(input("請輸入長方形寬度:"))
area=length*width
print("長方形的面積為:" + str(area))

#計算6年後存款
deposit=int(input("請輸入本金存款金額:"))
times=1.02**6
#deposit=deposit*times
deposit*=times
print("6年後存款為:%d元" % (deposit))

#檢查手機餘額
money=50000
cell=int(input("請輸入手機金額:"))
money-=cell
print("剩餘為:%d元" % (money))




