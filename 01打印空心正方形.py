a = int(input('请输入正方形的边长a: '))
if 0 < a < 21:
    print('*' * a)
    for i in range(a - 2):
        print('*','' * (a - 2),'*')
    print('*' * a)


