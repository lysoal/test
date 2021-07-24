




# number = input("请输入数字")
# if int(number) > 10:
#     print("对")
# else:
#     print("错")


# num = input("请输入数字：")
# new_num = int(num)
# if new_num%2 == 1:
#     print("奇数")
# else:
#     print("偶数")




    #多条件
# score = input("请输入分数")
# data = int(score)

# if data > 90:
#     print("优")
# elif data > 80:
#     print("良")
# elif data > 70:
#     print("中")
# elif data > 60:
#     print("差")
# else:
#     print("不及格")





    #条件嵌套
# print("欢迎致电10086，我们提供了如下服务：1.花费相关；2.业务办理；3.人工服务")
# choice = input("请选择服务序号")
# if choice == "1":
#     print("话费相关")
#     cost = input("查询话费 请按1；缴纳话费请按2；")
#     if cost == "1":
#             print("傻🐖🐖余额为♥520♥")
#     elif cost == "2":
#             print("充值话费面额")
#     else:
#             print("没有这个选项")
# elif choice == "2":
#     print("业务办理")
# elif choice == "3":
#     print("人工服务")
# else:
#     print("没有这个选项")





score = input("请输入分数")
data = int(score)

if data >=90 and data <=100:
    print("A")
elif data >=80 and data <90:
    print("B")
elif data >=60 and data <80:
    print("C")
elif data >=40 and data <60:
    print("D")
elif data >=0 and data <40:
    print("E")
else:
    print("输入错误")