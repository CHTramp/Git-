
import keyword
print(keyword.kwlist)

# 1、find操作
'''
格式： 字符串名.find（参数一，参数二，参数三）
其中参数一是必须的，参数二和参数三可以省略
参数一：传入需要查找的字符串
参数二：从字符串哪个起始位置开始
参数三：截止位置，
返回值：如果有，则返回的是检测字符的起始下标
        如果没有，则就返回一个-1
'''
mystr = "hello world my name is changfeng，yes name is changfeng"
# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
num = mystr.find("world")
print("num的值=%d"%(num))
print("num的值=",num)

num2 = mystr.find("he",2,10)
print("num2的值是=%d"%(num2))

# 2、index()操作

''''
格式：字符串名.index（参数一，参数2，参数3）
其中参数一是必须的，参数二和参数三可以省略
参数一：传入需要查找的字符串
参数二：从字符串哪个起始位置开始
参数三：截止位置，
只不过如果str不在 mystr中会报一个异常

返回值：如果有，则返回起始下标，如果没有，则会报异常，

'''

num3 = mystr.index("name",0,20)
print("num3的值是%d"%(num3))


# 3、 count
'''
count
返回 检测str在start和end之间 在 mystr里面出现的次数

mystr.count(str, start=0, end=len(mystr))
'''

num4 = mystr.count("name",0)
print("num4的值是%d"%(num4))


# 4、replace
'''

把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

mystr.replace(str1, str2,  mystr.count(str1))

其中参数3，如果省略，则全部替换，如果传入则只替换相应的多少个，
'''

str = mystr.replace("changfeng","laoliu",1)
str2 = mystr.replace("changfeng","laoliu",2)
str3 = mystr.replace("changfeng","laoliu")

print(str)
print(str2)
print(str3)

# 5、split
'''
以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

mystr.split(str=" ", 2)  

其中参数2，是maxsplit ，表达的是指定分割多少个字符，意思就是str将被分割后替换成多少个“ ，”

分割后的类型是列表的形式


'''

print(type(mystr.split(" ")))

num5 = mystr.split(" ")
print("====\n",num5)

num6 = mystr.split("name",2)
print(num6)

num7 = mystr.split("name",1)
print("-------\n",num7)


print("===========\n")

# 6 和7 是一样的，把首字符变为大写,即把字符串的第一个字符大写

str4 = mystr.capitalize()
print(str4)

# 7
str5 = mystr.casefold()
print(str5)

# 8 center  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# mystr.center(width)

str6 = mystr.center(100)
print(str6)

# 9 判断一个字符串是不是以什么字符或者字符结尾，
'''
可以区域判断，有参数二和参数3

'''
str7 = mystr.endswith("feng",0,20)
print(str7)


# 10 判断字符串是不是只由字母构成,返回一个布尔类型的值,该函数没有参数传递.isalnum和isalpha等价的

mystr1 = "heool wolrd name world"
str8 = mystr1.isalnum()
print(str8)

mystr2 = "hello"
str9 = mystr2.isalpha()
print(str9)

# 11 判断字符串是不是只由数字构成
mystr3 = "12aa34"
str01 = mystr3.isdigit()
print(str01)

# 12  <20>partition
# 把mystr以str分割成三部分,str前，str和str后,从左边开始，与之对应的是rpartition  从右边开始
# mystr.partition(str)

mystr4 = "nanme is changfeng  hello changfeng  are you ok"
str02 = mystr4.partition("chang")
print(str02)

# 13、 按照行进行分割
'''
splitlines
按照行分隔，返回一个包含各行作为元素的列表

mystr.splitlines() 
'''

# 14、
'''
strip
删除mystr字符串两端的空白字符,也可以是\n \t
'''

mystr04 = "   hello   world     "
str12 = mystr04.strip()
print(str12)

mystr05 = "\n\thelloworld\t\n"
str11 = mystr05.strip()
print(str11)

# 15
'''
title
把字符串的每个单词首字母大写



lower
转换 mystr 中所有大写字符为小写

mystr.lower()        



upper
转换 mystr 中的小写字母为大写

mystr.upper()   



lstrip
删除 mystr 左边的空白字符

mystr.lstrip()



rstrip
删除 mystr 字符串末尾的空白字符

mystr.rstrip() 



strip
删除mystr字符串两端的空白字符
'''








