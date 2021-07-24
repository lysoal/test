# from typing import Counter


# v1 = 0 or 3 and 7 or 4 and 4 or 1
# print(v1)

# r = 3 and 0
# print(r)


#实现连续支持三次登录系统错误后直接退出，并显示剩余次数
# count = 0
# while count < 3:
#     count += 1
#     user = input("请输入用户名：")
#     pwd = input("请输入密码：")
#     if user == "123456" and pwd == "123":
#         print("登录成功")
#         break
#     else:
#         message = "用户名或密码错误，剩余次数为{}次" .format(3-count)
#         print(message)




#猜年龄游戏
count = 4
while count > 0:
    count -= 1
    age = input("请输入年龄：")
    age = int(age)
    if age == 33:
        print("恭喜你猜对了")
        break
    else:
        print("猜错了")
    if count == 1:
        choice = input("是否继续游戏(Y/N)")
        if choice == "Y":
            count = 4
        elif choice == "N":
            break
        else:
            print("输入错误")
            break
print("结束")