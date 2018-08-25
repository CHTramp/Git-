# 对于元组来说，元组和列表是差不多的
# 元组是不能不修改的， 比如不能增加元素，不能修改元素，不能删除元素，

# 元组遍历

tu = (1,2,34,5)
for index,value in enumerate(tu):
    print(index,value)

# 返回这个元素在对象中出现的次数
num = tu.count(2)
print(num)

# index 返回的是查找在列表中的下标
num2 = tu.index(34)
print(num2)

# ============类型相互转换======

# 1、字典转换成元组
dict1 = {'name':1,"age":23}
# 如果直接tuple(dict1) 那么返回的只是字典的keys
tu1 = tuple(dict1.values())
print(tu1)

# 字典转换成列表,list(dict1) 那么返回的只是字典的keys
li = list(dict1)
print(li)

li2 =list(dict1.values())
print(li2)

# 2、字典转换成字符串
str1 = str(dict1)
print(str1)

# =====元组转换成字符串、列表====注意元组不可以转为字典

tupleExchang = (1,2,3,4,5,"a")
str2 = tupleExchang.__str__()
print(type(str2))
print(str2)

list2 = list(tupleExchang)
print(list2)

# =======列表转换成字符串、元组======注意：不能转换成字典
list3 = [1,2,34,55,6]
str3 = str(list3)
print(str3)

tup = tuple(list3)
print(tup)


tup_num = (1,2,3,4,5)
*m,n = tup_num # *m代表的是把前面的都赋值给m，以列表的形式，而n则去的是最后一个
print(m,n)

m,*n = tup_num # 第一个元素赋值给m，剩下的都赋值给n
print(m,n)


