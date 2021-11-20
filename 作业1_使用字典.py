# 从键盘任意输入一字符串,输入其中不同的字符串以及他们各自的个数;
# 例如:输入" abcdefgabc ",则输出:{'a':2,'b':2,'c':2,'d':1,'e':1,'f':1,'g':1}
# (提示使用字典)


my_dict2 = {}
char = input("请输入任意的字符串: ")
for i in char:
    num = char.count(i, 0, len(char))
    my_dict1 = {i: num}
    my_dict2.update(my_dict1)
print(my_dict2)
