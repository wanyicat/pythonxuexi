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
# u = [5,8,6,"辣子鸡块","番茄炒蛋",True,False]
# u.append("我是一根柴") #append可以进行追加，在元素最后面。
# print(u)
# """dsadasdsa"""
# '''dasdsacadas'''
# print(u[2:5])
# u.insert(3,"干炒牛河") #insert可以进行插入，任意位置。
# print(u)
# print("1+1")
# u.pop(2) #pop是剪切
# print(u)
# x = u.pop(2)
# y = u.pop(1)
# print(x)
# print(y)
# a = ["京酱肉丝",'AE86',666,9527,True,False,"馄饨",'酸辣面片汤']
# b = [a,"周杰伦","张学友","糖醋排骨",123321]
'''b.append(666)           append是最后面追加元素
b.insert(3,"test")      insert是插入元素
c = a.pop(2)            pop是剪切
d = b.pop(-1)
print(b)
x = a[2]
y = b[5]               注意：元组不可更改，数组可以。
print(c)                     元组是使用（）数组是使用[]
print(d)
print(x)
print(y)
print(x+y+c+d)
print(len(a[0]))         len是计算长度
print(a.index('馄饨'))   index是找到下标
print(type(True))        type是找到格式
print(a.count(False))    count是统计数量'''
# a.clear()
# print(a)
# e = ["我们老北京儿阿","起来就是这么一出","真是盖了帽了，我的老北鼻"]
# a.extend(e)         extend是在数组中添加数组
# print(a)
# print(e)
# f = a+e
# print(f)
# print(a)
# a.pop(0)
# print(a)
# print(a.pop(0))
# print(a)
# print(e)
# print(e.pop(0))
# a = ["京酱肉丝",'AE86',666,9527,True,False,"馄饨",'酸辣面片汤']
# b = [a,"周杰伦","张学友","糖醋排骨",123321]
# a.remove("馄饨") remove是删除，相比于pop而言remove没有赋值功能
# print(a)
# c = [0,False,1,True]
# print(c.index(0))   
# print(c.count(0))   
'''在编程中false=0 true=1'''
# b.insert(2,"郭富城")  2代表插入的位置 郭富城代表插入的字符
# print(b)
'''
所有的方法都是小括号结尾，比如print() input() len() pop()
元组，数组，字典，的取值都是用中括号，比如a[1] b[2]
元组，数组，字典，的定义分别为() [] {}
'''
'''                     字典的用法
'''
#字典的值没有前后顺序
#字典的结构必须是键值对结构 key:value
# t = {"name":"黄岭",'age':28,'学历':'大专'}
# print(t['age']) #取值用中括号
# t['high'] = '175cm' #增加键值对直接用中括号
# print(t)
# t['name'] = '王萧'  #修改键值对也是用中括号
# print(t)
# print(t.get('name')) #取值的第二种方法可以用get
# print(t)
# t.update(国籍='中国')
# print(t)
# t.update(fww=3)    #update是新增或者修改
# print(t)           #update的key不能加引号，value可以加引号 
# t.pop('fww')       #pop是剪切，字典同样适用
# t.update(high=175)
# t.update(国籍='中国')
# t.update(sex='男')
# print(t)
# '''用key取值和用get取值的区别'''
# print(t.get('name')) #name如果存在他们没有区别
# print(t['name'])     #name如果不存在用get会提示None，用key取值会报错
# del t['sex']
# print(t)
#数组字典的元素可以用del来删除

# a = input('name:')
# b = input('age:')
# c = input('sex:')
# u = {'name':a,'age':b,'sex':c}
# print(u)

# u = {'name':input('name:'),'age':input('age:'),'sex':input('sex:')}
# print(u)
'''                  Python第三章课程                 '''
'''                     判断                          '''
# age = int(input('请输入你的年龄:'))
# if age > 20 and age < 30 :
#     print('1')
# elif age > 30 and age < 60 :
#     print('2')
# elif age > 60 :
#     print('3')
# else :
#     print(True) 

# a = ('你好不好')
# if a in '你好吗' :                in的用法
#     print('yes')
# else:
#     print('no')    

# a = (0.88)
# if type(a) is int :
#     print('这是一个数字')
# elif type(a) is str :
#     print('这是一个字符串')    
# elif type(a) is bool :            #is的用法：确认格式。
#     print("这是布尔值")   
# else :
#     print('请输入正确的格式')     

print('欢迎来到年龄阶段探测器')
age = int(input('请输入你的年龄:'))
if age == 18 :
    print('你虽然已经成年了，但是学无止境。')
elif  age < 18 :
    if   age == 0 :
        print('你还在妈妈的肚子里呢，别调皮。')
    elif age <= 4 :
        print('你还是个婴儿')
    elif age > 4 and age <= 10 :
        print('你就是个小屁孩')
    else :
        print('你还未成年')
elif  age > 18 and age <= 30 :
    print('要好好规划自己的未来')
elif  age > 30 and age <= 60 :
    print('家庭的重担压得你喘不过气吧')
else :
    print('你可以退休享受生活了')
     

       
    

    


