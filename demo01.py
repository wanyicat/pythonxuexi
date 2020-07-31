#                       print的用法
# print("hello world!")
# print(2333)
# print(False)
# print("我们老北京"*2)
# print(1+2+3*(3/2+5*3)) # 可以做计算器用奥
# print(2>3) #可以做逻辑判断
# a = "黄岭" #赋予a含义为 黄岭
# print(a)
#                       input的用法
# b = input("请输入:")
# print("输出的内容：",b)
# a = float(input("请输入"))
# b = float(input("请输入"))
# c = float(input('请输入'))
# print("输出",a+b+c)
#len支持的格式有 字符串 数组 元组 字典
# int是整数 float是小数 str是字符串 bool是布尔值 tuple是元组 list是数组 
# dict是字典 type是格式 len是计算长度 print是打印 input是输出内容
# a = input("字符1输入：")
# b = input("字符2输入：")
# print("字数：",len(a+b))
# p = (2,4,5,7,"老北京鸡肉卷","东坡扣肉","AE86",True,False)
# print(p[4])                         
# print(p.index("东坡扣肉"))
# print(p.count(True))
# print(type('老北京鸡肉卷'))
# index可以找出下标编号，多个相同元素下从左至右第一个
# count可以统计元素的数量，适用场景为多个相同元素
                #    '''元组的使用'''
#index和count只适用于一维元组
# p = (2,4,5,7,"老北京鸡肉卷","东坡扣肉","AE86",True,False)
# b = (p,"上校鸡块",6688)
# print(b[0][4])
#批量取值专业名词叫切片，可以批量取值。切片必须连续取值，不可以跳着取值
#批量取值用冒号，左闭又开，并且只能从左往右数。
#print(p[-2])  倒着取值可以用负数
# print(p[4:6]) 
# '''print("我是谁")''' #多行注释用三个单引号或者三个双引号
#用引号注释前面不能加空格
# print("我是谁")
                #   '''数组的使用'''
#元组是使用（） 数组是使用[]
#元组写好后不能修改，数组可以
u = [5,8,6,"辣子鸡块","番茄炒蛋",True,False]
u.append("我是一根柴") #append可以进行追加，在元素最后面。
print(u)
"""dsadasdsa"""
'''dasdsacadas'''
print(u[2:5])
u.insert(3,"干炒牛河") #insert可以进行插入，任意位置。
print(u)
print("1+1")
u.pop(2) #pop是剪切
print(u)
x = u.pop(2)
y = u.pop(1)
print(x)
print(y)