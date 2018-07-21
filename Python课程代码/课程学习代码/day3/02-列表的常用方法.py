# 列表的常用方法
# 1、求列表的长度len()
list1 = [1,2,3,4,'adc',5]
num = len(list1)
print("list1的长度=%d"%(num))


# =============列表脚本操作================

# 2、列表之间的合并 +
lsit2 = [1,2,3]
list3 = ['a','b','c']
list4 = lsit2 + list3
print("list4的值是",(list4))

# 3、重复
list5 = [1]*5
print(list5)

# 4、判断一个元素在不在列表里面用in 返回一个bool类型
# 如果判断一个元素不在列表里面用 not in
listNum = [1,2,4,'a','b',8]
numbool = 'b' in listNum
print(numbool)

numbool2 = 'c' not in listNum
print(numbool2)

# 5、
# is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同。
listNum3 = listNum2 = [1,2,3,4,5]
numbool3 = 1 is listNum
print(numbool3)

numbool4 = listNum3 is listNum2
print(numbool4)

listNum4 = [1,2,3,4,5]
numbool5 = listNum4 is listNum2
print(numbool5)

a = 1
b = 1
numbool6 = a is b
print(numbool6)

# 通过上面的结论可以看出只有数值型和字符串型的情况下，a is b才为True，当a和b是tuple，list，dict或set型时，a is b为False。


# 6、删除列表元素
lista = [1,2,3,4,5,'a','b']

# 删除列表的下标为2的元素
del lista[2]
print(lista)

# 列表的迭代

lista1 = [1,2,3,4,5,'a','b']









