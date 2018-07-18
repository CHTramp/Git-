'''
什么是字符串?
字符串是通过双引号或者单引号括起来的文本信息
‘abc’
“sunk”

'''
# 创建字符串
str1 = 'abcde'
str2 = "sunck is a good main"


'''
字符串的运算

'''
# 字符串连接
str4 = "sunck is a"
str5 = "good main"
str6 = str4 + str5
print("str6 = ",str6)

# 输出重复字符串
str7 = "main"
str8 = str7 * 3
print("str8 = ",str8)

# 访问字符串中的某一个字符
# 通过索引下标查找字符，索引从0开始
# 字符串名【下标】
str9 = "sunck is a good main"
print(str9[1])

# 截取字符串的一部分
str10 = "sunck is a good main"
# 从给定下标出开始截取到给定下标之前
str11 = str10[4:15]
# 从头截取到给定下标之前
str12 = str10[:5]

# 从给定的下标截取到末尾
str13 = str10[8:]

print("str13 = ",str13)


a = "where there is a will there is a way"

# 判断一个字符串在不在里面
b = "there"
c = (b in a)
print("c = ",c)

# 判断一个字符串不在里面

b1 = "was"
c1 = (b1 not in a)
print("c1 = ",c1)

'''
格式化输出：
常用的格式化输出有：%d   %s    %f   \n   \t占位符

'''
number = 100
print("num的值 = ",number)
print("num的值%d"%(number))

strs = "hello world"
print("strs的值是%s"%(strs))
print("strs的值是",strs)

f = 10.2324
# %.2f是保留两位有效数字
print("f的值是%.2f"%(f))

'''
转义字符   \
将一些字符转换成有特殊含义的字符
'''
# \n  换行输出
num1 = 122
str19 = "hello world"
print("num = %d\nstr19 = %s\nf = %.3f" % (num1, str19, f))
'''
\\
'''
print("sunck \\ is")

# \'   \"
print('tom is a \'good\' man')
print("tom is a \"good\" man")
#      tom is a 'good' man


'''
\t   制表符
'''
print("sunck\tgood")

print("sunck is a good\thelloworld shhdhe miss")


# 如果字符中有好多字符串都需要转义，就需要加入好多\，为了简化，Python允许用r表示内部的字符串默认不转义
















