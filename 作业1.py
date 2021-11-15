# 一个列表若有20个整数组成,要求:将偶数放在前面,奇数放在后面,并输出该列表,(初始20个数据由用户任意输入)


my_list2 = []
my_list1 = []
my_list = input("请输入20个整数，两数之间用空格隔开：").split(" ")
try:
    if len(my_list) == 20:
        for i in range(len(my_list)):
            t = int(my_list[i])
            my_list[i] = t
        for j in my_list:
            if j % 2 == 0:
                my_list1.append(j)
            else:
                my_list2.append(j)
        my_list1.extend(my_list2)
        print(my_list1)
    else:
        print('你输入的数字不满足20 个整数')
except ValueError as f:
    print('你的输入里有字符,不是纯数字,请重新输入 ')
    print(f)  # 打印字符异常信息
