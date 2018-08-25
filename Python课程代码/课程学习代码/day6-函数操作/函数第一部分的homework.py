
import random

# 1.编写一个函数，求1+2+3+....+N
def sumNumber(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return  sum

result = sumNumber(100)
print(result)


# 2.编写一个函数，求多个数中的最大值

def maxNumber(*args):
    return max(*args)
result1 = maxNumber(1,33,5,2,55,8,434)
print(result1)

# 3.编写一个函数，实现摇色子的功能，打印n个色子的点数和
def sumNumber2(n):
    sum = 0
    count = 0
    while True:
        count += 1
        value = random.randint(1,6)
        print(value)
        sum += value
        if count == n:
            break
    return sum
result2 = sumNumber2(5)
print(result2)
# 法二，利用列表存储
def sumN(n):
    sum = 0
    count = 0
    listNum = []
    while True:
        count += 1
        value = random.randint(1,6)# random产生随机数的时候，死要包括结束位
        print(value)
        listNum.append(value)
        if count == n:
            for i in listNum:
                sum += i
            break
    return sum
result3 = sumN(5)
print(result3)
# 法三：通过外界输入
def my_sum():
    number = int(input('请输入N值：'))
    sum1 = 0
    for item in range(1,number+1):
        import random
        n = random.randint(1,6)
        print(n)
        sum1 += n
    print('和:',sum1)

my_sum()

# 4.编写一个函数，交换指定字典的key和value。

def exchangeKeyAndValue (dictNum):
    # 定义一个列表，用来存储子弹的每一个键值对
    list1 = []
    # 定义一个列表，把这些键值对存储
    list2 = []
    for key,value in dictNum.items():
        list1 = [value,key]
        list2.append(list1)

    return dict(list2)
dict1 = {'a':1,"b":4,'c':5}
result4 = exchangeKeyAndValue(dict1)
print(result4)

# 5、编写一个函数，求3个数的最大值
def maxNumber(a,b,c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max
result5 = maxNumber(5,99,10)
print(result5)


# 6.编写一个函数,提取指定字符串中的所有的字母，然后拼接在一起后打印出来
def delDigst(str1):
    str2 = ''
    for i in  str1:
        if 'z'>=i>='a' or 'A'<= i <='Z':
            str2 += i
    return str2

str1 = "sfsfhsf133sdfsf8877s"
result6 = delDigst(str1)
print(result6)


# 7.写一个函数，可以对多个数进行不同的运算
# 例如: operation('+', 1，2，3) --->求1+2+3的结果
# operation( '-'，10，9) --->求10-9的结果
# operation( ''，2，4，8，10) --->求24* 8* 10的结构
def caluNum(option,*argc):
    if option == '+':
        sum = 0
        for value in argc:
            sum += value
        return sum
    elif option == '-':
        sum = argc[1]
        for value1 in  argc[1:]:
            sum -= value1
        return sum
    elif option == '*':
        sum = 1
        for value2 in  argc:
            sum *= value2
        return sum
    elif option == '/':
        sum = argc[1]
        for value3 in argc[1:]:
            sum /= value3
        return sum
result7 = caluNum('+',2,2,5)
print(result7)
result8 = caluNum('-',2,2,5)
print(result8)
result9 = caluNum('*',2,2,5)
print(result9)
result10 = caluNum('/',2,2,5)
print(result10)
