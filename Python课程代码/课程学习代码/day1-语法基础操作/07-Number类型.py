'''
分类：整数、浮点数、复数
'''
'''
整数：Python可以处理任意大小的整数，当然包括负整数，在程序中表示和数学的写法一样
'''
number1 = 10
number2 = number1

# 连续定义多个变量
number3 = number4 = number5 = 1
print(number3,number4,number5)

# 交互是赋值定义变量
num1, num2 = 6, 7
print(num1, num2)
'''
浮点数:浮点数由整数部分与小数部分组成，浮点数运算可能会四舍五入的误差
'''
f1 = 1.1
f2 = 2.2
print(f1+f2)


'''
复数：实数部分和虚数部分组成： A =  a + bi
'''

'''
数字类型转换

'''
# 转化为整数
print(int(1.1))
print(int(1.9))

print(float(1))
print(float(3))

# 字符串转化成整数
print(int("123"))
print(float('112.23'))

# 字符串第一个作为正负号才有意义
print(int("sdj121"))
print(int('+123'))
print(int("-123"))

