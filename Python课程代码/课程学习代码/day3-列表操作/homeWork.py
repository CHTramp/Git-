'''
1. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是⼀个数字。例如2+22+222+2222+22222(此时共有5个数相加)，⼏个数相加有键盘控制。

分析：原来的等式可以等价为a*(1+11+111+1111+....) ,这里就可以用嵌套循环操作
'''
n = int(input("请输入你几个数相加"))
a = int(input("请输入你想要加的数"))
sum = 0

for i in range(1,n+1):
# 中间变量
    temp = 0
    for j in range(i):
        temp = temp + 10**j
# 最终结果
    sum = sum +  a*temp
print(sum)

'''
a=input('输入数字>>>')
count=int(input('几个数字相加>>>'))
ret=[]
for i in range(1,count+1):
    ret.append(int(a*i))
    
   # print(ret[i-1])
print(sum(ret))

'''


# 2. 打印图形1（正三角形）
n1 = int(input("请输入需要打印几行"))
for x in range(1,n1+1): # 行
    for y in range(0,x): # 列
        print("*",end='')
    print('')

# 3. 打印图形2（等腰三角形） (前面有空格，必须考虑空格的个数怎么打印)
n2 = int(input("请输入需要的打印多少行的等腰三角形"))
for x in range(1,n2+1):
    for y in range(n2-x):
        print(' ',end='')
    for z in range(0,x):
        print("* ",end='')
    print('')


# 4. 打印图形3(倒三角形）
n3 = int(input('请输入一个n值：'))
for x in range(n3):
    for y in range(n3-x):
        print('@', end = '')
    print('')

# 5. 输⼊两个正整数m和n，求其最⼤公约数和最⼩公倍数。
'''
m = int(input('请输入一个正整数m：'))
n = int(input('请输入一个正整数n：'))
if m > n:
    for x in range(n, 0, -1):
        if m % x == 0 and n % x == 0:
            print('%d和%d的最大公约数是：%d' % (m,n,x))
            print('%d和%d的最小公倍数是：%d' % (m,n,m*n/x))#两个数的最小公倍数=两个数的积最大公约数
            break
else:
    for y in range(m, 0, -1):
        if m % y == 0 and n % y ==0:
            print('%d和%d的最大公约数是：%d' % (m,n,y))
            print('%d和%d的最小公倍数是：%d' % (m,n,m*n/y))
            break
'''
# 6. ⼀个数如果恰好等于它的因⼦之和，这个数就称为 "完数 "。例如6=1＋2＋3.编程 找出1000以内的所有完数
num_list = []
for i in range(1,1000+1):
    for j in range(1,i):
        if i % j == 0:
            num_list.append(j)

    sum_num = 0
    for value in num_list:
        sum_num += value

    if sum_num == i:
        print("%d 是完数"%i)
    num_list.clear()


# 7. 输⼊⼀⾏字符，分别统计出其中英⽂字⺟、空格、数字和其它字符的个数。
str1 = input('请随便输入一串字符：')
Alphabet = 0
space = 0
digital =0
other =0
for item in str1:
    if item.isalpha():
        Alphabet += 1
    elif item.isspace():
        space += 1
    elif item.isdigit():
        digital += 1
    else:
        other += 1
print('英文字母:%d 空格:%d 数字:%d 其他字符:%d' %(Alphabet, space, digital, other))

# 8.有⼀个⻓度是10的列表，数组内有10个⼈名，要求去掉重复的
list_num = ['赵','刘','张','唐','黄','赵','刘','喻','是']
list_num2 =[]
for item in list_num:
    if item not in list_num2:
        list_num2.append(item)
print(list_num2)

# 也可以用集合，因为集合中元素是不能重复的
set_num = set(list_num2)
print(list(set_num))