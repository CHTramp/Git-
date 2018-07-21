
# 列表和C语言中的数组差不多，Python中的列表是可以存储任何类型的数据，与C语言不同的就是C语言是只能存储相同类型的数据
# 注意：在Python中报unexpected indent这种错误是属于在写代码的时候缩进有问题
list1 = [1,2,3,'aa',6]

# 打印列表
print(list1)

# 取列表中的某一个元素，可以根据下标来取
num = list1[0]
print(num)

num1 = list1[4]
print(num1)

# 列表也有切片，和字符串的切片是一样的,
num2 = list1[0:]
print(num2)
print(type(num2))
# 对于切片来讲，一共有三个参数，第一个是起始位置，第二一个是结束位置(不包含)，第三个参数是歩长，可以是正数也可以是负数，默认是1
# 倒序输出列表
num3 = list1[::-1]
print(num3)
# 取出列表的第2到3位，取的是下标为2、3的元素的值，不包括结束为，因为是左闭右开
num4 = list1[2:4]
print(num4)





