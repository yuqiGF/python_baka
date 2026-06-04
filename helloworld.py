from selectors import SelectSelector

print("helloworld")
print(type(True))
print(isinstance(True,bool))
# 字符串定义
s1 = "hello world"
#字符串拼接
print(s1 + "ciallo")

# 字符串格式化⭐ %s
name = "宇崎崎"
job = "程序员"
print("大家好，我是%s , 工作是 %s" % (name,job))
# 字符串格式化⭐⭐ f
print(f"你好 ， 我是{name}")

# 获取键盘输入 获取到的默认是字符串类型  调用如int()这样的函数可以转化
# s = input("你多高")
# t = input("你多重")
# print(f"你的bmi是{float(t) ** 2 / float(s)}")

# 运算符
a = 1 ** 3  #幂指数
b = 5 / 2  #返回真结果为浮点数的除
c = 5 // 2 #返回结果为整数的除法

# 逻辑运算符  and or not
aa = 1 < 3 and 1 < 2
ab = 1 < 3 or 1 < 2
ac = not 1 < 3

# 流程控制  if   match case（相当于java的switch）
score = 199
if score > 100:
    print("及格")
else:
    print("不及格")
print("------------------")

# match case
d = input("请输入今天星期几")
match d :
    case "1":
        print("今天星期一")
    case "2" | "3":  #或
        print("你好")
    case _:   #下划线是默认
        print(d)

# 循环
i = 1
while i < 2:
    print("你好")
    i += 1
else:   #不满足的时候执行一次
    print("你不好")

msg = "helloworld"
for i in msg:
    print(i)
else:
    print("遍历完毕")

for i in range(10): # range()从0开始到9结束  包前不包后
    print("ciallo")

# 九九乘法表
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{i} x {j} = {i * j}" , end="\t") #每行结尾都是制表符号（不屑的话默认是换行）
    print()  #字带换行
    