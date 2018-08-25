
import random

# 随机产生一个1-100的整数
# 输入的数字如果和产生的随机数是一样的，就提示猜对了，并且游戏结束
# 如果输入的数大于或者小于随机数，就提示输入的数字偏大或者偏小，然后重新输入
# random 产生的是（num1，num2）的随机数，其随机值是 num1 —— num2-1
number  = random.randint(1,100+1)
count = 0
while 1:
    count += 1
    valueNumber = input("请输出你要猜测的数")
    value = int(valueNumber)
    if value == number:
        if count < 5:
            print("神算子")
            break
        else:
            print("还不错")
            break
    elif value < number:
        print("小了")
    else:
        print("大了")

# 这里的地址是一样的，这就代表了是引用，
he = 16
va = 16
print(type(he))
print(id(he),id(va))

