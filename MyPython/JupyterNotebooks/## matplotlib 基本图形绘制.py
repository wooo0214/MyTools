-## matplotlib 基本图形绘制

## 折线图

## 库的引入
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_excel('F:\\00study\\10周数据分析师\\周老师—技术线\\大周老师第二阶段\\大周老师4\\第三节\\折线图.xlsx')
data.head()

## excel 的日期：
## 仅适用于excel中，与之前的时间戳（1970/1/1开始）毫无关系
## 当把日期格式变成数值格式时，会自动计算，转换成从1900年1月1日起到指定日期的天数
## 1900年的2月有28天，但excel中计算成了29天 -- excel 的bug。在计算时，从1900-01-01开始算时要减去两天

data['日期'] = pd.to_datetime(data['日期']-2，unit='d', origin=pd.Timestamp('1900-01-01')) ## -2 
## pd.to_datetime(parameters, unit=str, origin=...) 从origin开始加上单位为unit、数量为parameters的日期
data.head()

## 4-02 
## 折线图
## 日期叠一起了：设置x轴坐标倾斜
plt.xticks(rotation=30) # 倾斜30度

plt.plot(data['日期'],data['总销售额'])
plt.show()

## 设置画布大小
plt.figure(figsize=(20,5)) # figsize 元组
## 日期叠一起了：设置x轴坐标倾斜
## 得先有画布，再设置x轴等其他设置
plt.xticks(rotation=30) # 倾斜30度

plt.plot(data['日期'],data['总销售额'], color='red') # color 改变线条颜色
plt.show()

## 一个图画多个线条
## linewidth
# marker: 每个坐标点上标记的样式
# linestyle
plt.figure(figsize=(20,5))
## 日期叠一起了：设置x轴坐标倾斜
plt.xticks(rotation=30) # 倾斜30度

plt.plot(data['日期'],data['总销售额'], color='red', linewidth=2, marker='*') # 设置线条宽度
plt.plot(data['日期'],data['自配送销售额'], color='green', marker='o', linestyle='--')
plt.plot(data['日期'],data['FBA销售额'], color='blue', linestyle=':')

########### 中文显示问题
font = {'family': 'SimHei',
        'size': 20}
plt.rc('font',**font)

## 设置x，y轴名称
plt.xlabel('时间')
plt.ylabel('销售额')

plt.show()

## 柱形图
#  

