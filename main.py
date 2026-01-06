# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import keyword

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')
    # print(keyword.kwlist)
    num1 = 0.1
    num2 = 0.2
    print(num1 + num2)
    num3 = 17
    print(f'{num3} + {num2}')
    print(f"非运算:~{num3}")
    print(f"{num3:3}原码: {num3:08b}")
    print(f"{num3:3}取反：{(1<<8) - 1 ^num3:08b},得到结果的补码")
    print(f"{~num3:08b},计算结果的原码")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
