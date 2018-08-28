#/usr/bin/env python3
from math import exp,log,sqrt
from datetime import  datetime,date,time,timedelta
#注：第2行为引入三个数学函数：exp,log,sqrt


print("Output #1:I'm excited to learn Python.")

#例子1：方法format()
x=2
y=6
z=x+y
a=y-x
print("Three plus six equals {0:d}." .format(z))
print("Six reduce three equals {1:d}.".format(x,y,a))       #花括号中“1”对应后面.format()方法的第2个值，d代表把该值转为整数


#例子2:列表
o=[1,2,3,4]
p=['one','two','three','four']
q=o+p
print(q)
print('output:{1},{2}'.format(p,o,q))     #同上



#例子3：整数
x=8
y=2.14
z=4.13
print("x的值为：{0}".format(x))
print("x的平方为：{0}".format(x**2))
print("输出为：{0}".format(int(z)/int(y)))      #此处int()函数将数值字符串类型转为了整数类型



#例子4：浮点数
x=3.14
y=27.5
print("y除以x输出为：{0:.3f}".format(y/x))        #此处".3f"为保留后续运算结果小数点后3位



#例子5：第2行代码引入的3个数学函数
x=3.14
print('e的乘方为：{0}'.format(exp(x)))
print('log自然对数：{0}'.format(log(x)))
print('16的平方根为：{0}'.format(sqrt(16)))


#例子6：字符串和多行字符
print('I\'m a Chinese!')                #此处斜杆为转义
print('''以下是多行文本：                   
I am a Chinese,     
I like listening to music.
Anytimes I want to travel the whole world!              
''')                         #针对多行长文本，可以使用'''...'''   在长文本内所有字符都不需要去转义



#例子7：字符串应用
x='My girl friend is'
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
total_sales=int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)

print('This week\'s total sales: '+str(total_sales))






#例子8：split函数，分解字符串，返回一个list。
gf='My girl friend is very beautiful.'
print(gf.split(' ',3));


#例子9：replace函数：替换字符串
string="Ling is a 'chi huo'."
print(string.replace('chi huo','dou b'))


#例子10：date日期模块
print('以下是日期信息：')
print('The date is {0}'.format(date.today()))
print('Year:{0}'.format(date.today().year))
print('Month:{0!s}'.format(date.today().month))
print('Day:{0!s}'.format(date.today().day))

yestoday=datetime.today()+timedelta(days=-1)
print(yestoday)


#复制一个字典
user = {'name':'zkx','age':24}
new_dict = user.copy()


#列表生成式：
my_data = [[1,2,3],[4,5,6],[7,8,9]]
#第一种方法:
for i in my_data:
    for x in i:
        if x > 5:
            print(x)

#第二种方法，列表生成式：
new_list = [x for i in my_data for x in i if x > 5 ]
print(new_list)



#集合生成式：
my_data = [(1,2,3),(4,5,6),(7,8,9)]
set_of_tuples1 = {x for x in my_data}
print('set_of_tuples1 is {}'.format(set_of_tuples1))

set_of_tuples2 = set(my_data)
print('set_of_tuples2 is {}'.format(set_of_tuples2))


#字典生成式：
data = {2017:200,2016:500,2015:700}
result = {key : value for key,value in data.items() if value>300}
print('result is {}'.format(result))
print('key is {0},value is {1}'.format(result.keys(),result.values()))



#异常处理：
#定义一下计算平均值的函数
def getMean(num_list):
    return sum(num_list)/len(num_list)

my_list = []

try :
    result = getMean(my_list)
except ZeroDivisionError as detail :
    print('Output(Error):'+str(float('nan')))
    print('Output (Error):',detail)
else:
    print("(This mean is ):",result)
finally:
    print('finally:The finally block is executed every time')












