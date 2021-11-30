# 1 眼看要过年了,深夜食堂经营的不错,你打算给员工发奖金犒劳一下,请你定义函数,当输入员工姓名和工作时长两个参数时,即可大印出该员工获得的奖金
# 发奖金的要求要求如下:
# 工作时长小于6 月，发国定奖金500元
# 时长在 6月到一年 （包含一年）每月奖金 120元
# 超过一年 每月奖金 180元
name = input('请输入员工的姓名 : ')
month = eval(input('请输入工作的时长 : '))


def func(name, month):
    if 0 < month < 6:
        print(name)
        print('奖金为 500')
    elif 6 <= month <= 12:
        print(name)
        print('奖金为 %d 元' % (month * 120))
    elif 12 <= month:
        print(name)
        print('奖金为 %d 元' % (month * 180))
    else:
        pass


func(name, month)
