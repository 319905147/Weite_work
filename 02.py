x = 0
for i in range(3):  # i 循环 i 可以取  0 1 2
    x += 1         # i 每取一个值, x 就 加 1 , 同时 j这个循环,j依次取 0 1 2
    for j in range(3):
        if j:   # 假如j取0, x就加1,j 取1 ,就会终止这次循环,然后j取 2 ,在终止,以此类推
            continue
        x += 1    # 最终就是 i 每循环一次,x就加2
print(x)




