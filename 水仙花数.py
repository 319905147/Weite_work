
for i in range(100, 1000):
    x = i // 100       # / 返回商  得到百位数字
    y = i // 10 % 10     # / 返回商 % 返回余数 得到 十位数字
    z = i % 10     # 返回商 得到个位数字
    if i == x**3 + y**3 + z**3:
        print(i)


# 以下为学习探索的过程   理解使用 运算符
"""
# print(121 % 10)
i = 153
x = i // 100  # / 返回商  得到百位数字
y = i // 10 % 10  # / 返回商 % 返回余数 得到 十位数字
z = i % 10  # 返回商 得到个位数字
if x*100 + y*10 + z == x ** 3 + y ** 3 + z ** 3:
    print('水花仙数是153')
    print("%-5d" % i)


print(153 // 100)
print(153 // 10 % 10)
print(153 % 10)

"""

# if 153 == 1 ** 3 + 5 ** 3 + 3 ** 3:
#     print('153符合所求的数')






