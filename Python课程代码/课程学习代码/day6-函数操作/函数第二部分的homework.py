# 1.写⼀个函数将⼀个指定的列表中的元素逆序(例如[1, 2, 3] -> [3, 2, 1])(注意：不要使⽤列表⾃带的逆序函数)
def reserverList(list):
    lenList = len(list)
    for i in range(0,lenList):
        value = list.pop(i)
        list.insert(0,value)
    return list
list1 = [1,2,3]
result = reserverList(list1)
print(result)
# 法二
list2 = [1,2,3,4]
list3 = list2[::-1]
print(list3)

# 2.写⼀个函数，提取出字符串中所有奇数位上的字符
def exract(str):
    str1 = ''
    for i in str[1:len(str):2]:
        str1 += i
    return str1

str1 = 'sdfjsjfjjgjjjfg2323'
result1 = exract(str1)
print(result1)

# 3.写⼀个匿名函数，判断指定的年是否是闰年
result2 = lambda year:(year % 400 == 0)or((year % 100 != 0) and (year % 4 == 0))
print(result2(2008))

# 法二
#法2
def leap_year(number):
    if number%100 == 0:
        if number%400 == 0:
            return '闰年'
        else:
            return '平年'
    else:
        if number%4 == 0:
            return '闰年'
        else:
            return '平年'
print(leap_year(189))

#4.使⽤递归打印：
# n = 3的时候
#   @
#   @@@
# @@@@@
# n = 4的时候:
#   @
#   @@@
#   @@@@@
# @@@@@@@
# 法1
def my_pritn(n,m=0):
    if n == 0:
        return None
    my_pritn(n-1,m+1)
    print(' '*m,end = '')
    print('@'*(2*n-1))
my_pritn(8)
# 法2
def print_star(n,m=0):
    if n == 1:
        print(' '*m,'@ ')
    else:
        print_star(n - 1,m+1)
        print(' '*m,'@ '*n)
print_star(5)

# 5.写函数，检查传⼊列表的⻓度，如果⼤于2，那么仅保留前两个⻓度的内容，并将新内容返回给调⽤者。
list1 = [1,2,3,4,5,6,7,8]
def length(list1):
    list2 = []
    if len(list1) > 2:
        list2 = list1[0:2]
        return list2
print(length(list1))

# 6.写函数，利⽤递归获取斐波那契数列中的第 10 个数，并将该值返回给调⽤者。
def sequence(n):
    if n == 1 or n == 2:
        return 1
    return sequence(n-1)+sequence(n-2)
print(sequence(6))






