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












