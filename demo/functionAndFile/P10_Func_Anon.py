"""
    该案例演示了函数的注释
"""
# 普通的自定义函数：
# def dog(name, color, species):
#    return (name, color, species)


# 添加了注释的自定义函数：
def dog(name:str, age:(1, 99), species:'狗狗的品种') -> tuple:
    return (name, age, species)

print(dog.__annotations__)
