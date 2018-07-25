'''
列表的练习

写代码，要求实现下面每一个功能

　　li=['alex','eric','rain']

　　1，计算列表长度并输出

　　2，列表中追加元素“servn"，并输出添加后的列表

　　3，请在列表的第一个位置插入元素‘tony’，并输出添加后的列表

　　4，请修改列表位置元素‘kelly’，并输出修改后的列表

　　5，请在列表删除元素‘eric’，并输出删除后的列表

　　6，请删除列表中的第2个元素，并输出删除后的元素的值和删除元素后的列表

　　7，请删除列表中的第三个元素，并输出删除后的列表

　　8，请删除列表的第2到4个元素，并输出删除元素后的列表

　　9，请用for len range输出列表的索引

　　10，请使用enumrate输出列表元素和序号

　　11，请使用for循环输出列表中的所有元素
 '''

li=['alex','eric','rain']
lenNum = len(li)
print(lenNum)

li.append("servn")
print(li)

li.insert(0,"tony")
print(li)

li[0] = "suny"
print(li)

li.pop(1)
print(li)

li.remove("eric")
print(li)
'''

tu = ('alex','eric,'rain')

　　1，计算元组的长度并输出

　　2，获取元祖的第二个元素，并输出

　　3，获取元祖的第1-2个元素，并输出

　　4，请用for输出元祖的元素

　　5，请使用for,len,range输出元组的索引

　　6，请使用enumerate输出元组元素和序号，（从10开始）
'''

tu = ('alex','eric','rain')
# 　　1，计算元组的长度并输出
print(len(tu))
# 　　2，获取元祖的第二个元素，并输出
print(tu[1])
# 　　3，获取元祖的第1-2个元素，并输出
print(tu[0:2])
# 　　4，请用for输出元祖的元素
for i in tu:
    print(i)
# 　　5，请使用for,len,range输出元组的索引
for i in range(len(tu)):
    print(i)
# 　　6，请使用enumerate输出元组元素和序号，（从10开始）
for index,i in enumerate(tu,10):
    print(index,i)



