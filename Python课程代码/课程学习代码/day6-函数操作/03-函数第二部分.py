

'''
作用域

作用域：一个变量可以使用的范围，就是这个变量的作用域。（函数和类可以影响变量的作用域）
全局变量：从声明开始到文件结束都可以使用的变量
局部变量：在函数（类）中声明的变量就是局部变量。作用域是从声明开始到文件结束。
如果要让一个局部变量变成全局变量，可以用global语句
格式：
global 变量
变量 = 新值
在声明函数的时候，如果函数里面在声明新的函数，可能用到nonlocal，不过这样使用的频率很低。

'''

count = 0
def function():
    global count
    # count = 0
    count += 1
function()
print(count)
function()
print(count)
function()
print(count)
function()
print(count)


'''
匿名函数

匿名函数：本质还是函数，以另外一种简单的方式来声明的
匿名函数的声明：
函数名 = lambda 参数列表：返回值

'''

num = lambda x,y:max(x,y)
print(num(6,2))

# 练习：写一个函数，求1+2+3+.....，和不能大于10000
def my_sum():
    sum1 = 0
    number = 1
    while True:
        if sum1 + number >= 10000:
            return sum1,number-1#一个return可以返回多个值，多个值之间用逗号隔开多个值以元组返回
        sum1 += number
        number += 1
print(my_sum())


"""
声明一个函数就是在声明一个变量(其实使用函数就是在使用变量，是一个道理）
可以赋值，可以查看类型，可以作为函数的参数，可以作为函数的返回值
"""




