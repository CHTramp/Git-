
import random
print(5/2)

a = 20
b = 0

num = b or a
print(num)

# 产生一个int类型的随机数
num1 = random.randint(0,10)
print(num1)

# 产生一个小数的随机数
number = random.uniform(0,99)
print(number)


# 练习：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问n个月的有多少对为多少？

def mousNum(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a + b
    return a
# 第二种写法
# a = 0
# b = 1
# for i in range(6): # 6代表的是月数
#     a,b = b, a + b
# print(a)

numb = mousNum(6)
print(numb)



