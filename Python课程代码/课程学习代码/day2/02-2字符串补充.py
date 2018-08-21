
'''
在字符串中，如果加上ord()Python中字符串中的字符是Unicode编码
Unicode码是十六位的对一个字符，一般是八位对一个字符
Unicode码包含了ASSCII码，可以表示所有的语言
用ord()函数获取一个字符的Unicode码

'''


str = ord('刘') # 这是先把刘转换成Unicode码，然后在赋值给str
print(str)

str1 = ord(chr(200000))
print(str1)

# chr()函数，是传一个int类型数据，然后把它转换成并返回一个字符
print(chr(200000))

str2 = chr(10000)
print(str2)

print(chr(65))

'''
在字符串中，还存在一些转义字符，比如 \ \t \n \\ 等
那么如果不想字符串进行转义，可以在前面加上一个r或者R

'''
str11 = r"\\"
print(str11)

str22 = R'\n'
print(str22)
