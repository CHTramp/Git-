"""
1.什么是模块：一个.py文件就是一个模块

2.import :可以通过import关键字导入其他的模块
import 模块名（.py文件名）

直接导入模块的时候，相当于把被导入的模块里面的内容粘贴到import的位置

3.怎么使用模块中的内容？什么内容是可以使用的？
import 模块名------->导入模块中的整个内容
模块名.的方式去使用模块中的内容

在模块中声明全局变量都可以使用（普通变量、函数、类）

"""
'''
import other_test

other_test.test1()

'''


from other_test import test2
import pygame

result = test2(1,20)
print(result)


