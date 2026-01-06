# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。
import types


class Person:
    pass

p = Person()
p.hobby = "reading"
print(p.hobby)

# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：\(S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(self):
    return math.pi * self.radius ** 2

c = Circle(5)
c.cal = types.MethodType(calculate_area, c)
area = c.cal()
print("%.2f" % area)
