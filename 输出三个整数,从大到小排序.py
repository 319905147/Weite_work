while True:
    # while Ture  无限循环
    x = eval(input('请输入第一个数:'))
    y = eval(input('请输入第二个数:'))
    z = eval(input('请输入第三个数:'))
#  eval()可以输入小数和整数   int()只能输入整数   float()只能输入小数
    if x > y:
        if x > z:
            max1 = x
            if y > z:
                max2 = y
                max3 = z
            else:    # z>y
                max2 = z
                max3 = y
        else:     # z>x
            max1 = z
            max2 = x
            max3 = y
    else:    # y > x
        if y > z:
            max1 = y
            if x > z:
                max2 = x
                max3 = z
            else:    # z>x
                max2 = z
                max3 = x
        else:      # z>y
            max1 = z
            max2 = y
            max3 = x

    print(max1, max2, max3)










