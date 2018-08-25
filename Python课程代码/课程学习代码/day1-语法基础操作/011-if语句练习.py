
'''

# 判断任意输入一个数字是不是偶数
num = int(input("请输入一个数字"))
if num % 2 == 0:
    print("您输入的这个是是偶数")
else:
    print("您输入的不是偶数")
'''



# 作业：从控制台输入一个三位数，如果是水仙花数这输出 153 = 1^3 + 5^3 + 3^3
# 作业：从控制台输入一个五位数，如果是回文数，这输出，11111  12321   12221  对称这种
# 作业：从控制台输入两个数，比较大小，输出较大的值
# 作业：从控制台输入三个数，输出较大的值
'''
num = int(input("请输入一个数"))
num1 = num // 100
num2 = num // 10 % 10
num3 = num % 10

if num == num1 ** 3 + num2 ** 3 + num3 ** 3:
    print("这是水仙花数")
else:
    print("这不是水仙花数")


a = int(input("请输入一个五位数"))
a1 = a // 10000
a2 = a //1000 % 10
a3 = a // 10 % 10
a4 = a % 10

if a1 == a4:
    if a2 == a3:
        print("这是一个回文数")
    else:
        print("这不是一个回文数")
else:
    print("这不是一个回文数")
    
'''



'''
    第二种写法
    
    a = int(input("请输入一个三位数"))
    a1 = a //10000
    a2 = a %10
    if a1 != a2:
        print(no)
    else:
    ----和上面差不多
'''

'''
m = int(input("请输入比较大小的第一个数"))
n = int(input("请输入比较大小的第二个数"))
if m > n:
    print(m)
elif m == n:
    print("两个数相同,其值等于",m)
else:
    print(n)
'''
'''
if m > n:
    if m > i:
        print(m)
    else:
        print(i)
elif n > m:
    if n > i:
        print(n)
    else:
        print(i)
elif m > i:
    if m > n:
        print(m)
    else:
        print(n)
        

'''
m = int(input("请输入第一个数"))
n = int(input("请输入第一个数"))
i = int(input("请输入第一个数"))

max = m
if n > max:
    max = n
if i > n:
    max = i
print("max = ",max)












