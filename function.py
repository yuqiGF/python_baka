#函数
def add(a,b):
    """
    函数的说明文档
    :param a:参数1
    :param b: 参数2
    :return: 和
    """
    return a+b


print(add(1, 2))

num = 1
def test():
    global num #⭐声明全局变量  使函数内可以修改全局变量
    num = num + 1
test()
print(num)

def test2(*args , **kwargs):
    """
    不定长参数
    :param args:位置参数
    :param kwargs: 关键字参数
    :return:
    """
    print(args)

#⭐匿名函数 lambda 参数：函数体 只能单行 （通常作为高阶函数的参数使用）
var = lambda: print("hello")

#⭐类型注解
aa : int = 1
def test3(a : list[int]) -> list[int]:  #箭头后面是返回值类型
    return a

#导入模块功能  from *** import *** as ***
import random as r
r.randint(1 , 100)

# 异常捕获
try:
    print(r.randint(1 , 100))
except NameError as e:
    print(e)
finally:
    print("结束")