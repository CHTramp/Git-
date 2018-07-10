import  random
num = int(input("请输入你的号码"))


res = random.choice(range(100)) + 1

# 判断是否中奖

if num == res:
    print("恭喜你中奖500万")
else:
    print("就差一点点了，加油")

