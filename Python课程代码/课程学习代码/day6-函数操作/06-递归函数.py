"""
1、什么是递归
递归函数：在函数的函数体中调用函数本身


理论上循环能做的事情，递归都可以做


对递归的要求：能不用就不用
函数调用的过程是一个压栈的过程（每调用一次函数，系统都要为其分配内存空间，
用来存储函数中声明变量和参数，这个内存在函数调用结束的时候会自动释放）
"""


def func1():
    print('===')
    func1()


"""
2、怎么去写一个递归函数
a.找临界值（跳出循环---->return）
b.找关系：假设当前函数对应的功能已经实现，找到f(n)和f（n-1)的关系
c.使用f（n-1)和前面找到的关系去实现f(n)的功能
"""


# 写一个递归函数实现：1+2+3+4+.....+n
def my_sum(n):
    sum1 = 0
    for x in range(1, n + 1):
        sum1 += x
    return sum1


print(my_sum(5))


# 递归函数
def my_sum2(n):
    # 1.找到临界值
    if n == 1:
        return 1
    # 2.找my_sum2(n)和my_sum2(n-1)的关系
    # 3.使用my_sum2(n-1)去实现my_sum2(n)的功能
    return my_sum2(n - 1) + n


print(my_sum2(5))


# 用递归2*4*6*.....n（n是偶数）
def my_mul(n):
    if not n % 2:
        if n == 2:
            return 2
        return my_mul(n - 2) * n
    else:
        print('请输入偶数')
        return None


print(my_mul(6))

"""
n=3
***
**
*
n=4
****
***
**
*

"""


def print_star(n):
    # 1.找临界值
    if n == 1:
        print('*')
        return None
    # 2.找关系
    """
    关系：先打印n个'*'，然后打印f(n-1)

    """
    print('*' * n)
    print_star(n - 1)


print_star(8)

"""
n = 4
*
**
***
****
n=3
*
**
***
"""


def print_star(n):
    if n == 1:
        print('*')
        return None
    print_star(n - 1)
    print('*' * n)


print_star(5)
