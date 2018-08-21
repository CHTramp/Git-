set_1 = {1,2,3,4,5,6}
set_2 = {1,3,5}

# 判断A集合是否包含在集合B中

'''
集合1 >= 集合2 -----判断集合1是否包含集合2(判断集合2中的元素是否都在集合1里面）
集合1 <= 集合2 -----判断集合2是否包含集合1（判断集合1中的所有元素是否都在集合2中）

'''
num = set_2 >= set_1
print(num)
num1 = set_1 >= set_2
print(num1)

'''

可以和数学的集合一样求并集（|），补集（^）,交集（&）,差集（-）
并集（|）：A中的元素+在B中的不在A中的元素
交集（&）：在A中也在B中的元素
差集（-）：A-B 在A中不在B中的元素
补集（^）：A中的元素+B中的元素-A和B中同时出现的元素。

'''
list_num = [1,2,3,4,5,6]
set_num = set(list_num)
print(type(set_num))

list_num1 = ['a','b',2,3,4,5]
set_num1 = set(list_num1)
print(type(set_num1))

set_result = set_num | set_num1
print(set_result)

set_result1 = set_num ^ set_num1

set_result2 = set_num & set_num1

set_result3 = set_num - set_num1

print(set_result,set_result1,set_result2,set_result3)

# 求集合的长度
count_num = len(set_num)
print(count_num)

for i,value in enumerate(set_num):
    print(i,value)