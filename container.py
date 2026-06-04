#python容器  list  str  tuple元组  set集合  dict字典
s = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
print(s[-1]) #反向索引  从-1开始
print(s[0 : 5 : 2])  #开始，结束。步长
print(s[:5])
s.append(11)
s.remove(3) #删除内容为3的元素
s.pop(0) #删除索引
s.reverse() #反转
s.sort() #排序
#列表推导式
a = [i ** 2 for i in range(1, 11)]
print(a)

str1 = "yuqiqi"
str1.find("y")
str1.count("i")
str1.strip("i")  #去除空白或者指定字符

#⭐元组  不可变的列表  小括号
t1 = (1,2,3,4,5,6,7,8,9,10)
t1.count(1)
t1.index(1) #匹配第一次出现的位置
#组包
t2 = 1 ,2 ,3 , 4
#解包
a , b , c , d = t2
#（*）扩展捷报
x , *y , z = t2   #y是中间两个  放在前后都可以

#集合
s1 = {1 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}
s2 = set()  #⭐空集合
s1.add(1)
s2.add(2)
s1.pop() #随机删除
s1.difference_update(s2) #差集
s1.union(s2) #并集
s1.intersection(s2) #交集



#字典  就相当于map
d1 = {}  #⭐空字典
d2 = {a:1 , b:2 , c:3}