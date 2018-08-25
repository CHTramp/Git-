'''
对于一个函数，他的参数是可以有很多样式的，
下面我们就来一一的看
在函数传参是，一般按照形参的顺序一一传递

'''

# 第一种：可以给形参指定值，位置可以改变
def fun(a,b,c):
    print(a,b,c)
    return (a,b,c)
result = fun(c = 10,b = 20, a = 30)
print(type(result))


# 第二种：函数的形参中，有默认值

def fun1(a,b = 20):
    print(a,b)
    return a + b
result1 = fun1(10)
print(result1)

# 第三种、参数个数不定
# 参数的个数不确定的时候，就在声明函数的时候，形参的前面加一个*,将形参变成元组
# 调用函数的时候，这个参数会将对应的实参作为元组的元素保存起来




def fun2(*argc):
    for value in argc:
        print(value)
# 调用函数
fun2(1,2,3,4,5,6,7)
# 注意：在函数参数的个数不定时，必须写在函数形参的最后

def fun3(a,*argc):
    print(a,argc)

fun3(1,2,3,4,5,6)

# 不能这样写
# def fun4(*argc,a):
#     print(argc,a)
# fun4(1,2,3,45,6)
# 但是可以指定形参参数的值，
def fun5(*argc,a):
    print(argc,a)
fun5(1,2,3,4,5,a = 6)