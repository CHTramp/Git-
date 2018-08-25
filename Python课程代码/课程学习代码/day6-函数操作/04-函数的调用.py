
"""
函数的调用其实本质上是可以把它当做一个变量在用
可以赋值，可以查看类型，可以作为函数的参数，可以作为函数的返回值
"""

def func():
    print("I Love You")

print(func(),type(func))

# 函数名func1可以当成变量使用
def func1(a):
    print(a)
    return 10
print(func1,type(func1))

"""
python中的三目运算符
值1 if 表达式 else 值2----->判断表达式是否为True,为True整个表达式的结果为'值1',否则表达式的结果为'值2'

"""
a = 10 if 10 > 20 else 20

print(a)
b = 20 if 20>30 else 30
print(b)

"""
 3.将函数作为函数的返回值

"""
# 写一个函数有个参数，要求传入一个运算符号（+，-，*，>,<），返回符号对应的功能
# + ------>求和功能
# - ------>求差功能
# ........
def get_method(char):
    if char == '+':
       return lambda x,y:x+y
    elif char == '-':
        def func(m,n):
            return m - n
        return func
    elif char == '*':
        return lambda x,y:x*y
    elif char == '>':
        def func(x,y):
            return x > y
        return func
    elif char == '<':
        return lambda x,y:x < y
    else:
        def func(x,y):
            return None
        return func
print(get_method('+')(10,20))
print(get_method('-')(10,20))
print(get_method('%')(10,20))
result55 = get_method('+')(10,30)
print(result55)