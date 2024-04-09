# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:07:48 2022

@author: dell
"""

#a = float(input('a = '))
#b = float(input('b = '))
# 定义变量并赋值
a=8
b=3

# 计算x1
x1 = ((a+b)*(a-b)/(a*a+b*b))**0.5
print('x1 = %.2f' % x1)

# 计算x2
if x1 < -1:
    x2 = 5*x1 + 3
elif x1 >=-1 and x1 <= 1:
    x2 = x1 + 2
else:
    x2 = 3*x1 - 5
print ('x2 = %.2f' % x2)

# 计算成绩等级y
c = x1 * 100

if c >= 90:
    print ("y =", 'A')
    y = 'A'
elif c < 90 and c >= 80:
    print("y =", 'B')
    y = 'B'
elif c < 80 and c >= 70:
    print("y =", 'C')
    y = 'C'
elif c < 70 and c >= 60:
    print("y =", 'D')
    y = 'D'
else:
    print("y =", 'E')
    y = 'E'
    
# 保存结果为csv文件
import pandas as pd
dic = {'id':['q1','q2','q3']
       ,'answer':[x1,x2,y]}
answer_1 = pd.DataFrame(dic)

### 注意x1的小数位数

x1_cut = format(x1,'.2f')
float(x1_cut)
type(x1_cut)

answer_1.to_csv('answer_1.csv', index=False, encoding='utf-8-sig')
