

# 定义学生 列表
import aifc

stu_list = []


def stu_menu():
    print('1 添加学生信息')
    print('2 删除学生信息')
    print('3 修改学生信息')
    print('4 查看个人的信息')
    print('5 查看全部学生的信息')
    print('6 退出系统')


# 添加学生信息
def insert_student():
    name = input('请输入要添加的学生姓名')
    for stu in stu_list:
        if stu['name'] == name:
            print('这个学生信息已经存在')
        return

    age = input('请输入要添加学生的年龄')
    num = int(input('请输入要添加学生的学号'))
    # 定义一个字典进行存储单个学生的信息
    stu_dict = {'name': name, 'age': age, '学号': num}
    # 将学生字典 添加到学生列表中
    stu_list.append(stu_dict)


# 删除学生信息
def remove_student():
    name = input('请输入要删除的学生名字')
    for stu in stu_list:
        if stu['name'] == name:
            stu_list.remove(stu)
            print('该学生的信息已经删除')
            break
        else:
            print('该学生的信息不存在,请在次输入学生名字')

# 修改学生的信息


def modify_student():
    # 1 都使用 name 对学生进行判断
    # 2 使用 input 获取要 修改 的学生姓名
    name = input('请输入需要操作的学生的姓名:')
    # 3 判断学生的信息是否存在
    for student in stu_list:
        if student['name'] == name:
            # 4 学生存在对学生进行 修改
            student['age'] = int(input('请重新输入年龄'))
            student['gender'] = input('请重新输入性别')
            # return
            break
    # 5 学生信息不存在,直接结束
    else:
        print('-*-----该学生的信息不存在,无法修改-----*-')

'''

def search_student():
    # 1 都使用 name 对学生进行判断
    # 2 使用 input 获取要 查询 的学生姓名
    name = input('请输入需要操作的学生的姓名:')
    # 3 判断学生的信息是否存在
    for student in stu_list:
        if student['name'] == name:
            # 4 学生存在对学生进行 查询
            print(f'姓名:{student["name"]},年龄:{student["age"]},学号:{student["num"]}')
            # return
            break
    # 5 学生信息不存在,直接结束
    else:
        print('-*-----该学生的信息不存在无法查询-----*-')


def show_all_student():
    if len(stu_list) > 0:
        for student in stu_list:
            print(f'姓名:{student["name"]},年龄:{student["age"]},学号:{student["num"]}')
            # print(student)
    else:
        print('目前还没有学生信息')

'''


# 查询单个学生的信息

def search_student():

    name = input('请输入要查询的学生信息')
    for stu in stu_list:
        if stu['name'] == name:
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 学号:{stu["学号"]}')
            break
    else:
        print('该学生的信息不存在,请重新输入姓名')


# 查询全部学生的信息
def show_all_student():
    if len(stu_list) > 0:
        for stu in stu_list:
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, {stu["学号"]}')
    else:
        print('目前还没有学生信息,请添加学生信息')


# 退出系统 保存学生的信息   文件  w

def save():
    f = open('学生信息.txt', 'w')
    buf = f.write(str(stu_list))
    # f.write()
    f.close()



while True:
    stu_menu()
    opt = input('请输入编号进行操作: ')
    if opt == '1':
        # print('1 添加学生信息')
        insert_student()
        print('学生信息添加成功')
    elif opt == '2':
        # print('2 删除学生信息')
        remove_student()
    elif opt == '3':
        # print('3 修改学生信息')
        modify_student()
    elif opt == '4':
        # print('4 查看个人的信息')
        search_student()
    elif opt == '5':
        # print('5 查看全部学生的信息')
        show_all_student()
    elif opt == '6':
        save()
        print('6 退出系统')
        break

    else:
        print('请输入正确的编号进行操作')
        continue

    input('回车键继续')



























