# 编写一个程序,打印出 10行的杨辉三角

def function(n):
    my_list1 = [1]
    if n == 1:
        print(my_list1)
    else:
        for i in range(n):
            my_list2 = [1]
            print(my_list1)
            if i == 0:
                my_list2.append(1)
            else:
                if i < n - 1:
                    for j in range(i):
                        my_list2.insert(j + 1, my_list1[j] + my_list1[j + 1])
                my_list2.append(1)
            my_list1 = my_list2


function(10)
