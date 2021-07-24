#%
# name = "武功"
# age = 18
# message = "我叫%s,今年%d岁" %(name,age)
# print(message)

# text = "%(name)s你什么时候过来呀？ %(user)s今天不在家。" % {"name":"死鬼","user":"李杰"}
# print(text)

# text = " %s,这个片我已经下载了90%%了，居然特么的断网了" %"兄弟"
# print(text)




# #format(推荐)
# text = "我叫{0},今年18岁 " .format("哈哈")
# print(text)

# text = "我叫{0}，今年{1}岁，姓名是{0}。" .format("武功",18)
# print(text)


# text = "我叫{n1},今年{age}岁，姓名是{n1}。" .format(n1="武功",age=18)
# print(text)


# text = "我叫{0}，今年{1}岁"   #模板/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
# data = text.format("武功",18)
# print(data)

#f
# action = "跑步"
# text = f"嫂子喜欢{action},跑完之后满身大汗"
# print(text)


name = "喵喵"
age = 18
text = f"嫂子的名字叫{name}，今年{age}岁"
print(text)

text = f"嫂子的名字叫喵喵，今年{19+2}岁"
print(text)