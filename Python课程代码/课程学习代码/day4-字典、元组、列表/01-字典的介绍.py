# 字典：通过键值对的形式进行存储表达 即key - value  dict  具有极快的查找速度 并且是无序的

'''
key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key
'''
# 定义字典
dict1 = {'value':1,'value2':2}
print(dict1)

# 字典访问元素，通过key值访问
num = dict1['value']
print(num)

# 字典的添加，如果在添加的key在原来的基础之上没有，那么，就添加
dict2 = {'老刘':170,"老郑":168,"laowang":178,"laoliu":"laoqing"}
# 添加,添加到最后
dict2["laoxiang"] = 175
print(dict2)

# 添加，如果原来有key，那么就是修改原来的值(这也是修改)
dict2["老郑"] = 190
print(dict2)

# 删除，利用pop() 删除指定的key以及所对应的值
dict2.pop("laowang")
print(dict2)

# 查询里面的键值对
for value in  dict2:
    print(value,dict2[value])

# 拿到所以的key值
for key in dict2.keys():
    print(key)

# 拿到所以的value的值
for value1 in dict2.values():
    print(value1)

# 拿到所有的键值对，就是Number类型
for a,b in dict2.items():
    print(a,b)

# 拿到所有的键值对，不过是元组类型
for aa in dict2.items():
    print(aa,type(aa))

# 和list比较
# 1、查找和插入的速度极快，不会随着key-value的增加而变慢
# 2、需要占用大量的内存，内存浪费多
# list
# 1、查找和插入的速度随着数据量的增多而减慢
# 2、占用空间小，浪费内存少

# popitem会随机返回删除的键值对
dict3 = {"a":1,"b":2,"c":3,"d":5,"bc":7}
num2 = dict3.popitem()
print(num2)
print(dict3)

# get()函数，返回指定键的值，如果值不在字典中返回default值

number = dict3.get("c")
print(number)
# setdefault()和get函数是差不多的，都是返回一个指定的key的值，如果没有找到就返回为none
number2 = dict3.setdefault("ss")
print(number2)


