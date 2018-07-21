# 列表的常见函数
# 1、append()
list1 = [1,2,3,4,5]
list1.append('abc')
print(list1)

# 2、清空列表
list2 = ['a','b']
list2.clear()
print(list2)

# 3、浅拷贝
list3 = list1.copy()
print(list3)
# 4、得到列表中包含该元素的个数
num = list3.count(1)
print(num)

# 5、迭代extend（）,想当于在原来的列表后面一次增加了一些元素,参数需要传递一个迭代类型，可以是list、tuple
a = [1,2,3,4]
b = [2,3,4,5,6]
c = (1,1,2,2)
a.extend(c)
print(a)

# 6、 把一个列表里的元素倒序，reverse（），没有返回值
b.reverse()
d = b
print(d)

# 7、移除列表中某个值的第一个匹配项，从左找到第一个指定元素remove()
a1 = [1,2,3,2,3,4,2,'a']
a1.remove(2)
print(a1)

# 8、移除列表中的一个元素（默认最后一个），并返回该元素的值 pop()
a2 = [1,2,3,'a','b',2,5]
num1 = a2.pop(5)
print(num1)

# 9、列表的排序：注意排序优先级：数字>大写字母>小写字母>符号>中文
'''
1、sort   永久性的排序，就是原来的列表都改变了
2、sorted  临时性排序  ,需要同类型
3、reverse() 列表反序

'''
aa = [1,2,3]
bb = [44,5,5]

a23 = ['aa','adfa','sdf']
k = bb.sort()
print(bb)
b2 = sorted(a23)
print(b2)

# 10.求列表中最大元素的值max（list） 同类型元素
print(max(bb))

# 11. 求列表中的最小元素的值min(list)  同类型元素
a4 = [4,12,3,5,7]
print(min(a4))

# 12、遍历列表
a5 = [1,3,5,6,7]
for valuse in a5:
    print(valuse)

count = len(a5)
i = 0
while i < count:
    print(a5[i])
    i += 1

# 13、使用range()函数生成一系列数值
# 产生1——9的数值
for valuse1 in range(1,10):
    print(valuse1)


# 产生0——5 的数值，并转化成列表的形式
valuse2 = list(range(0,6))
print(valuse2)
print(type(valuse2))

'''
切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。我们使用一对方括号、起始偏移量start、终止偏移量end 
以及可选的步长step 来定义一个分片。

格式： [start:end:step]

• [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
• [start:] 从start 提取到结尾
• [:end] 从开头提取到end - 1
• [start:end] 从start 提取到end - 1
• [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
• 左侧第一个字符的位置/偏移量为0，右侧最后一个字符的位置/偏移量为-1

'''

list7 = [1,2,3]
# 调用函数，
list8 = list7.__add__([5,6])
print(list8)
print(list7)
