
# 编写函数

def reverse_num(num):
    if num < 0:
        numStr = str(-num)
        numStr = numStr[::-1]
        num = -int(numStr)
    else:
        numStr = str(num)
        numStr = numStr[::-1]
        num = int(numStr)
    return num

print(reverse_num(123))
print(reverse_num(-123))