
# while  循环
'''
while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...


在Python中没有++，--的运算，++等价于+=
'''

i = 0
sum1 = 0
while i < 5:
    sum1 = sum1+ i
    i+=1
print(sum1)

# 求1-100的偶数的和


j = 0
sum2 = 0
while j <= 100:
    if j % 2 == 0:
        sum2 += j
    j += 1
print(sum2)

'''

while 条件1:

        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        ...(省略)...

        while 条件2:
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
            ...(省略)...
'''
i = 1
n = int(input("请输入一个数"))
while i <= n:
    j=1
    while j <= i:
        print("*",end='')
        j+=1
    print("\n")
    i+=1




'''
#debug = False
rows = cols = 9
sep = ' '
w1 = []

# 默认全部用.填充
for i in range(0, rows):
    row = sep * cols
    w1.append(row)

for i in range(0, rows):
    # 第一行和最后一行
    if i in (0, rows - 1):
        row = list(range(0, cols, 2))
        for j, item in enumerate(row):
            row[j] = '*'
        w1[i] = sep.join(row)
    else:
        # 需要替换的索引
        ri = cols - i - 1
        # 替换
        w1[i] = w1[i][:ri] + '*' + w1[i][ri + 1:]

for r in w1:
    print(r)

'''



#debug = True
rows = cols = 9
sep = ' '
w1 = []

# 默认全部用.填充
for i in range(0, rows):
    row = sep * cols
    w1.append(row)

for i in range(0, rows):
    # 第一行和最后一行
    # \
    w1[i] = w1[i][:i] + '*' + w1[i][i + 1:]
    ri = -i
    # /
    row = w1[i][:ri - 1] + '*'
    if i > 0:
        row += w1[i][ri:]
    w1[i] = row

for r in w1:
    print(r)











