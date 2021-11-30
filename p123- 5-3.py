# 一只球从80m高度自由下落,每次落地后返回原高度的一半,再下落
# 求:第10次落地是共经过多少米?第10 次反弹多高?   编写函数实现

def func1(x):
    n = (1 / 2) ** x * 80
    print(n)


def func2(x):
    m = 0
    n = 80
    a = 80 / 2 + n
    for i in range(x):
        m += a * (1 / 2) ** i  # m 第十次弹起时的总路程
    j = (1 / 2) ** x * 80  # j 为第十次弹起的高度
    print(m - j)


print('第10次落地时共经过的距离: ')
func2(10)
print('第10次反弹的高度为: ')
func1(10)
