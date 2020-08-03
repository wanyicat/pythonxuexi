# #                       print的用法
# # print("hello world!")
# # print(2333)
# # print(False)
# # print("我们老北京"*2)
# # print(1+2+3*(3/2+5*3)) # 可以做计算器用奥
# # print(2>3) #可以做逻辑判断
# # a = "黄岭" #赋予a含义为 黄岭
# # print(a)
# #                       input的用法
# # b = input("请输入:")
# # print("输出的内容：",b)
# # a = float(input("请输入"))
# # b = float(input("请输入"))
# # c = float(input('请输入'))
# # print("输出",a+b+c)
# #len支持的格式有 字符串 数组 元组 字典
# # int是整数 float是小数 str是字符串 bool是布尔值 tuple是元组 list是数组 
# # dict是字典 type是格式 len是计算长度 print是打印 input是输出内容
# # a = input("字符1输入：")
# # b = input("字符2输入：")
# # print("字数：",len(a+b))
# # p = (2,4,5,7,"老北京鸡肉卷","东坡扣肉","AE86",True,False)
# # print(p[4])                         
# # print(p.index("东坡扣肉"))
# # print(p.count(True))
# # print(type('老北京鸡肉卷'))
# # index可以找出下标编号，多个相同元素下从左至右第一个
# # count可以统计元素的数量，适用场景为多个相同元素
#                 #    '''元组的使用'''
# #index和count只适用于一维元组
# # p = (2,4,5,7,"老北京鸡肉卷","东坡扣肉","AE86",True,False)
# # b = (p,"上校鸡块",6688)
# # print(b[0][4])
# #批量取值专业名词叫切片，可以批量取值。切片必须连续取值，不可以跳着取值
# #批量取值用冒号，左闭又开，并且只能从左往右数。
# #print(p[-2])  倒着取值可以用负数
# # print(p[4:6]) 
# # '''print("我是谁")''' #多行注释用三个单引号或者三个双引号
# #用引号注释前面不能加空格
# # print("我是谁")
#                 #   '''数组的使用'''
# #元组是使用（） 数组是使用[]
# #元组写好后不能修改，数组可以
# # u = [5,8,6,"辣子鸡块","番茄炒蛋",True,False]
# # u.append("我是一根柴") #append可以进行追加，在元素最后面。
# # print(u)
# # """dsadasdsa"""
# # '''dasdsacadas'''
# # print(u[2:5])
# # u.insert(3,"干炒牛河") #insert可以进行插入，任意位置。
# # print(u)
# # print("1+1")
# # u.pop(2) #pop是剪切
# # print(u)
# # x = u.pop(2)
# # y = u.pop(1)
# # print(x)
# # print(y)
# # a = ["京酱肉丝",'AE86',666,9527,True,False,"馄饨",'酸辣面片汤']
# # b = [a,"周杰伦","张学友","糖醋排骨",123321]
# '''b.append(666)           append是最后面追加元素
# b.insert(3,"test")      insert是插入元素
# c = a.pop(2)            pop是剪切
# d = b.pop(-1)
# print(b)
# x = a[2]
# y = b[5]               注意：元组不可更改，数组可以。
# print(c)                     元组是使用（）数组是使用[]
# print(d)
# print(x)
# print(y)
# print(x+y+c+d)
# print(len(a[0]))         len是计算长度
# print(a.index('馄饨'))   index是找到下标
# print(type(True))        type是找到格式
# print(a.count(False))    count是统计数量'''
# # a.clear()
# # print(a)
# # e = ["我们老北京儿阿","起来就是这么一出","真是盖了帽了，我的老北鼻"]
# # a.extend(e)         extend是在数组中添加数组
# # print(a)
# # print(e)
# # f = a+e
# # print(f)
# # print(a)
# # a.pop(0)
# # print(a)
# # print(a.pop(0))
# # print(a)
# # print(e)
# # print(e.pop(0))
# # a = ["京酱肉丝",'AE86',666,9527,True,False,"馄饨",'酸辣面片汤']
# # b = [a,"周杰伦","张学友","糖醋排骨",123321]
# # a.remove("馄饨") remove是删除，相比于pop而言remove没有赋值功能
# # print(a)
# # c = [0,False,1,True]
# # print(c.index(0))   
# # print(c.count(0))   
# '''在编程中false=0 true=1'''
# # b.insert(2,"郭富城")  2代表插入的位置 郭富城代表插入的字符
# # print(b)
# '''
# 所有的方法都是小括号结尾，比如print() input() len() pop()
# 元组，数组，字典，的取值都是用中括号，比如a[1] b[2]
# 元组，数组，字典，的定义分别为() [] {}
# '''
# '''                     字典的用法
# '''
# #字典的值没有前后顺序
# #字典的结构必须是键值对结构 key:value
# # t = {"name":"黄岭",'age':28,'学历':'大专'}
# # print(t['age']) #取值用中括号
# # t['high'] = '175cm' #增加键值对直接用中括号
# # print(t)
# # t['name'] = '王萧'  #修改键值对也是用中括号
# # print(t)
# # print(t.get('name')) #取值的第二种方法可以用get
# # print(t)
# # t.update(国籍='中国')
# # print(t)
# # t.update(fww=3)    #update是新增或者修改
# # print(t)           #update的key不能加引号，value可以加引号 
# # t.pop('fww')       #pop是剪切，字典同样适用
# # t.update(high=175)
# # t.update(国籍='中国')
# # t.update(sex='男')
# # print(t)
# # '''用key取值和用get取值的区别'''
# # print(t.get('name')) #name如果存在他们没有区别
# # print(t['name'])     #name如果不存在用get会提示None，用key取值会报错
# # del t['sex']
# # print(t)
# #数组字典的元素可以用del来删除

'''字典中可以加入字典'''
# a = {}
# b =input('请输入账号:')
# c =input('请输入密码：')
# d ={b:c}                     
# a.update(d)
# print(a)

# # a = input('name:')
# # b = input('age:')
# # c = input('sex:')
# # u = {'name':a,'age':b,'sex':c}
# # print(u)

# # u = {'name':input('name:'),'age':input('age:'),'sex':input('sex:')}
# # print(u)
# '''                  Python第三章课程                 '''
# '''                     判断                          '''
# # age = int(input('请输入你的年龄:'))
# # if age > 20 and age < 30 :
# #     print('1')
# # elif age > 30 and age < 60 :
# #     print('2')
# # elif age > 60 :
# #     print('3')
# # else :
# #     print(True) 

# # a = ('你好不好')
# # if a in '你好吗' :                in的用法
# #     print('yes')
# # else:
# #     print('no')    

# # a = (0.88)
# # if type(a) is int :
# #     print('这是一个数字')
# # elif type(a) is str :
# #     print('这是一个字符串')    
# # elif type(a) is bool :            #is的用法：确认格式。
# #     print("这是布尔值")   
# # else :
# #     print('请输入正确的格式')     

# # print('欢迎来到年龄阶段探测器')
# # age = int(input('请输入你的年龄:'))
# # if age == 18 :
# #     print('你虽然已经成年了，但是学无止境。')
# # elif  age < 18 :
# #     if   age == 0 :
# #         print('你还在妈妈的肚子里呢，别调皮。')
# #     elif age <= 4 :
# #         print('你还是个婴儿')
# #     elif age > 4 and age <= 10 :
# #         print('你就是个小屁孩')
# #     else :
# #         print('你还未成年')
# # elif  age > 18 and age <= 30 :
# #     print('要好好规划自己的未来')
# # elif  age > 30 and age <= 60 :
# #     print('家庭的重担压得你喘不过气吧')
# # else :
# #     print('你可以退休享受生活了')


# # a_int = (0,1,2) in (0,1,2,3,4,5,6)
# # print(a_int) #返回false
# # a_int = (0,1,2) and (1,2,3) in (0,1,2,3,4,5,6)
# # print(a_int) #返回false
# # a_int = (0,1,2) or (1,2,3) in ((0,1,2),1,2,3,4,5,6)
# # print(a_int) #返回(0,1,2)
# # a_int = (0,1,2) and (1,2,3) in ((0,1,2),1,2,3,4,5,6)
# # print(a_int) #返回false
# # a_int = (0,1,2) and (1,2,3) in ((0,1,2),(1,2,3),2,3,4,5,6)
# # print(a_int) #返回true
# # a_int = (0,1,2) or (1,2,3) in ((0,1,2),(1,2,3),2,3,4,5,6)
# # print(a_int) #返回(0,1,2)

# # '''and优先级找flase or优先级找true'''
# # a = 0 and 1
# # b = [] and {} and '' and () and 'ddd'
# # c = True and 0 and  1 and False and {}
# # d = 0 or 1
# # print(a,b,c,d) #分别返回 0 [] 0 1


# grade = {}
# grade.update(张三=66,李四=80,王麻子=75,浪晋=95,黄岭=100,王萧=88,张飞=28,刘备=55,关羽=77,曹操=92)
# print(grade)
# grade_a = {}
# grade_b = {}
# if grade. < 60 :
#     print('分数不及格')
#     grade = grade_a
# else:
#     print('恭喜你及格啦')
#     grade = grade_b
'''        while的用法        '''
# studentlist = ['张三','李四','王五','赵六','黄岭','大锤','王萧','张飞','刘备','关羽']
# grade_a ={}
# grade_b ={}
# a = 0
# while a < len(studentlist) :
#     b = int(input("请输入"+studentlist[a]+"成绩:"))
    
#     if b < 60 :
#         grade_a[studentlist[a]] = b 
#     if b  >= 60 :
#         grade_b[studentlist[a]] = b 
#     a = a + 1
# print(grade_a,grade_b)

'''        for的用法    '''
# studentlist = ['张三','李四','王五','赵六','黄岭','大锤','王萧']
# for a in studentlist :
#     print(a)  #一次循环输出 张三 李四 王五 赵六 黄岭 大锤 王萧

# t = tuple(range(0,100))
# print(t)
# for x in t :
#     print(x)


# t = tuple(range(0,100,5)) #5代表了步数
# print(t) #输出 (0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95)


# studentlist = ['张三','李四','王五','赵六','黄岭','大锤','王萧','张飞','刘备','关羽']
# grade_a ={}
# grade_b ={}
# for i in range(0,10) : 
#     a = int(input('请输入'+studentlist[i]+'的成绩:'))
#     if a < 60 :
#         grade_a[studentlist[i]] = a
#     if a >= 60 :
#         grade_b[studentlist[i]] = a
# print(grade_a) 
# print(grade_b)


'''        九九乘法表    '''
# for x in range(1,10) :
#     for y in range(1,x+1) :
#         print(y,'×',x,'=',x*y,end=" ")
#     print( )

# a = '红灯'
# b = '绿灯'
# c = '黄灯'
# x = range(1,69)
# for i in x :
#     if i < 31 :
#         print(a)
#     if i < 66 and i >= 31 :
#         print(b)
#     if i >= 66  :
#         print(c)
'''       红绿灯循环      '''
# a = '红灯'
# b = '绿灯'
# c = '黄灯'
# n = 1
# while n < 10 :
#     x = range(1,69)
#     for i in x :
#         if i < 31 :
#             print(a,'还有',31-i,'秒结束')
#         if i < 66 and i >= 31 :
#             print(b,'还有',66-i,'秒结束')
#         if i >= 66  :
#             print(c,'还有',69-i,'秒结束') 

# a = 0
# while a == 0 :
#     for i in range(30,0,-1) :
#         print('红灯还有'+str(i)+'秒结束')
#     for i in range(35,0,-1) :
#         print('绿灯还有'+str(i)+'秒结束')
#     for i in range(3,0,-1) :
#         print('黄灯还有'+str(i)+'秒结束')
'''  range只能是整数，默认从小往大数，如上使用负数可以倒数
     range(20,10,-1)  rang(-10,-5,1)   range(-6,-8,-1)                                                  
'''
# i = 1
# while i < 10 :
#     a = 30
#     while a > 0 and a <= 30 :
#         print('红灯还有',a,'秒')
#         a = a - 1
#     b = 35
#     while b > 0 and b <= 35 :
#         print('绿灯还有',b,'秒')   
#         b = b - 1
#     c = 3
#     while c > 0 and  c <= 3 :
#         print('黄灯还有',c,'秒')
#         c = c - 1
#     i = i + 1
'''fomat和{}{}没有搞懂，要查找资料'''
# light = {'红灯':30,
#          '绿灯':35,
#          '黄灯':3 }
# t = 0
# while t ==0 :
#     for i in light :   '''此处i是字典里面的KEY，不是指一组键值对'''
#         for j in range(light[i]) :
#             print("{}还有{}秒".format(i,light[i]-j))
#         print("======================================================")

'''       登录模块       '''
# userlist ={}
# username = input('请输入账号：')
# a = len(username)
# b = ('abcdefghijklmnopqrstuvwxyz')
# if a >=5 and a <=8 :
#     if username[0] in b :
#         print('账号可以使用')
#         # password = input('请输入密码：')
#         # if len(password) >= 6 and len(password) <= 12 :
#         #     print('账号注册成功，3s后跳转页面')
#         #     # userlist.update(username = password)
#         #     userlist[username] = password
#         # else :
#         #     print('密码不规范，请重新输入')
#         #     exit()
#     else :
#         print('账号不合法，账号开头必须为小写字母')
#         exit()
# else :
#     print('账号不规范，请重新输入')
#     exit()
# # password = input('请输入密码：')
# # if len(password) >= 6 and len(password) <= 12 :
# #     print('账号注册成功，3s后跳转页面')
# # else :
# #     print('密码不规范，请重新输入')
# #     exit()
# # userlist[username] = password
# # print('用户账号密码',userlist)
'''     循环终止和跳过循环    '''
# for i in range(10) :
#     if i ==4 :
#         break
#     print(i)
'''                 break是跳出循环，continue是跳过某一个循环。'''
# for i in range(10) :
#     if i ==4 :
#         continue
#     print(i)




'''                        方法的定义(函数)                       '''
# def jiafa(a,b,c) :
#     '''三个数相加之和
#     '''
#     if type(a) is int and type(b) is int and type(c) is int :
#         print(a+b+c)
#     else:
#         print('输入的数据类型不正确')
# jiafa(10,11,0)  #打印出21
# print(jiafa(10,18,6)) #打印出 34 None，原因是没有返回值。
# '''   返回值   '''
# def jiafa(a,b,c) :
#     '''三个数相加之和
#     '''
#     if type(a) is int and type(b) is int and type(c) is int :
#         return a+b+c
#     else:
#         return '输入的数据类型不正确'
# jiafa(10,11,0)  #没有打印
# print(jiafa(10,18,6))  #打印34 有了返回值


'''    方法用法的实例  设计方法的时候可以用return来添加返回值   '''
# def checkname(username) :
#     if len(username) >= 5 and len(username) <= 8 :
#         if username[0] in 'qwertyuioplkjhgfdsazxcvbnm' :
#             return True
#         else :
#             return '账号必须为小写字母开头'
#     else :
#         return '账号长度必须为5到8位'

# username = input('请输入账号：')
# password = input('请输入密码：')
# userlist = {}
# if checkname(username) == True :
#     if len(password) >=6 and len(password) <= 12 :
#         print('账号注册成功')
#         print({username:password})
#         userlist.update({username:password})
#         print(userlist)
#     else :
#         print('密码必须为6到12位')
# else :
#     print(checkname(username))


'''异常捕获'''
# try :
#     print(a+1)
# except :
#     print('代码错误')

'''异常类'''
# try :
#     print(a+1)
# except Exception as c:
#     print('代码错误',c)


# def chekenp(a,b) :
#     '''
#     验证账号密码是否可用
#     '''
#     try :
#         if len(a) >= 5 and len(a) <= 8 :
#             if a[0] in 'qwertyuioplkjhgfdsazxcvbnm' :
#                 if len(b) >=6 and len(b) <=12 :
#                     return True
#                 else :
#                     return '密码必须为6到12位'
#             else :
#                 return '账号必须为小写字母开头'
#         else :
#             return '账号长度必须为5到8位'
#     except :
#         return '账号或密码不合法'

# x = input('请输入账号：')
# y = input('请输入密码：')
# if chekenp(x,y) == True :
#     print('恭喜你，账号创建成功')
# else :
#     print(chekenp(x,y))

''' 代码的单位从小到大分别为：变量 方法 类 模块 包     '''
'''  安装包 pip install + 包的名字                               
     卸载包 pip uninstall + 包的名字
     查看包 pip list  
     使用包 import +包的名字
'''
# import time 
# for i in range(10) :
#     time.sleep(1)         '''停顿一秒'''
    # print(i)

# import random
# i = random.randint(100,50000) '''随机数'''
# print(i)






        















         







    


        


    




    
    

    










       
    

    


