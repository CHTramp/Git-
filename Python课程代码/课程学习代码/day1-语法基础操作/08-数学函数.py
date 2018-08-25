
# 导入库
# 库：封装一些功能
# math:数学相关的库
import  math
import  random


# abs()函数 ：返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(abs(a1))

# 比较两个数的大小,如果输出的值是1那么a3>a4,如果等于-1则相反，等于0，说明两个值相同
a3 = 100
a4 = 9
print((a3>a4) - (a3<a4))

# 返回给定参数的最小值

print(max(1,2,3,4,5,6))


# 返回给定参数的最大值
print(min(1,2,3,4,5,6))

# 求x的y次方 2^5
print(pow(2,5))

# round(x[,n] 四舍五入,返回浮点数x的四舍五入的值，如果给出n值，则代表舍如到小数点后n位
print(round(3.456))
print(round(3.556))
print(round(3.456,2))
print(round(3.546,1))


# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

# 向下取整
print(math.floor(22.3))
print(math.floor(22.9))

# 返回整数部分与小数部分
print(math.modf(22.3))

# 开方
print(math.sqrt(16))

# 随机数
# 1.从序列的元素中随机挑选一个元素，元素不局限于数字，字符串也是可以的
print(random.choice([1,3,5,7,9]))

print(random.choice(range(5))) # range(5) == [0,1,2,3,4]

print(random.choice("sunck"))

# 产生一个1~100的随机数
r1 = random.choice(range(100)) + 1

# random.randrange([start,] stop[,step]) => 开始， 停止  ，步长
# start===指定范围的开始值，包含在范围内
# stop==指定范围的结束值，不包含在范围内
# step==指定的递增基数,如果不写，默认是1，
print(random.randrange(1,100,2))

# 从0~99选取一个随机数,
print(random.randrange(100))

# 随机生成[0，1)之间的数（浮点数） 一边用于概率
print(random.random())

list = [1,2,3,4,5]

# 将序列的所有元素随机排序
random.shuffle(list)
print(list)

# 随机生成一个实数（有可能是小数，有可能是整数），范围是[3,9]
print(random.uniform(3,9))






