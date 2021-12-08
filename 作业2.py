# 123_4 编写函数,求出  1+(1+2)+(1+2+3)+...+(1+2+3+4+..+n)的和,函数以n为参数,n由用户从键盘输入

def func(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(0, i + 1):
            s += j
    print(s)


func(int(input('请输入一个整数: ')))
