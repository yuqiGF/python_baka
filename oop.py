#类
class Car:
    wheel = 4  #类属性

    #self可以拿到当前实例对象
    def __init__(self,name,age):  #初始化方法，第一个参数默认是self，相当于构造器
        self.name = name  #self相当于this
        self.age = age
    def run(self):
        self.wheel = 2  #实例属性  优先访问实例属性
        print(self.name + " is running")

    #魔法方法   在合适的时候自动调用
    def __str__(self): #输出的时候自动调用  （相当于java 的重写toString）
        print(self.name + " is running")
    def __eq__(self,other): #相当于重写equals（）
        return self.name == other.name
    def __lt__(self,other): return self.name < other.name  #同理
#对象
c = Car("yuqiqi" , 12)
#动态的添加属性
c.color = "red"
c.brand = "blue"
c.name = "ciallo"
print(c.__dict__)  #⭐对象中的属性作为字典返回

if __name__ == "__main__":
    c.run()
    print(c.wheel)