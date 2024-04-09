## 旅游网站数据预处理
## 删掉代码后，根据注释复原

#*
# 我的笔记
# *#

import numpy as np
import pandas as pd

# 把第0列设置为索引列
df = pd.read_csv("F:\\00study\\10周数据分析师\\周老师—技术线\\大周老师第二阶段\\大周老师3\\第二节\\data2.csv", index_col = 0)
df.head()

## 查看数据形状
df.shape
## 查看数据详情，从其中分析出哪些列有空值
df.info()
## 查看数据的描述，并说明为什么不是所有的列都有数据描述
df.describe()

df.columns
## 查看列的值，并发现列的值有什么问题
df.columns.values

## 去除列名称两端的空格
col[0].strip()

## 批量去除空格
#*
# 列表推导式#
df.columns = [x.strip() for x in col]
df.columns.values

## 重复值的处理：去除掉数据中所有的重复值，
## 标准：所有行都重复的话即为重复值

## 查看重复值
df[df.duplicated()]
## 查看一共有多少重复值
df.duplicated().sum()
## count vs sum
- count 计数，计算所有的数量
- sum 统计所有值为true的数量

## 删除掉所有的重复数据，并替换原来的数据
df.drop_duplicates(inplace=True)

## 再次查看重复值
df.duplicated().sum()
## 再次查看形状
df.shape
## 重置索引
df.index = range(df.shape[0])
## 再次查看索引，检查是否重置成功
df.index

## 3-12
## 异常值的处理
## 处理的字段： 价格，节省

df.describe()
# 转置查看
df.describe().T

## 计算价格的标准差
df['价格'].std()

## 计算价格减去价格平均值的差值
df['价格'] - df.['价格'].mean()

## 标准差标准化处理，也叫做标准分数
sta=(df['价格']-df['价格'].mean())/df['价格'].std()
## 标准分数大于3的认为是异常值
## 筛选异常值
df[sta.abs()>3] ## abs 绝对值

## 节省的钱大于价格的钱的数据筛选出来
df[df['节省']>df['价格']]

###### 数据拼接，把异常值拿出来
pd.concat([df[df['节省']>df['价格']],df[sta.abs()>3]])

## 从原始数据中删除掉所有的异常值
### 找到异常值的索引
del_index = pd.concat([df[df['节省']>df['价格']],df[sta.abs()>3]]).index
### 执行删除
df.drop(del_index, inplace=True)
### 查看形状
df.shape

## 缺失值的处理
## 查看每一列的缺失值
df.isnull().sum()

## 筛选出出发地为空的数据
df[df['出发地'].isnull()]

## 筛选出价格为空的数据
df[df['价格'].isnull()]

## 访问出发地为空的数据的出发地这一列
df.loc[df['出发地'].isnull(),'出发地']

## 访问出发地为空的数据的路线名这一列
df.loc[df['出发地'].isnull(),'路线名']

## 替换缺失值1 提取
df.loc[df['出发地'].isnull(),'出发地'] = [str(x)[:2] for x in df.loc[df['出发地'].isnull(),'路线名']]
## 替换缺失值2 字符串切割
[str(x).split("-") for x in df.loc[df['出发地'].isnull(),'路线名']][0][0]

## 验证数据是否被填充
df['出发地'].isnull().sum()

## 价格的处理，用平均值填充
## 求价格平均值
df['价格'].mean()

## 四舍五入
round(df['价格'].mean())

## 用平均值填充价格为空的数据
df['价格'].fillna(round(df['价格'].mean()), inplace=True)

df.isnull().sum()

### 作业：请把目的地和节省两个字段的空值按照上述逻辑自行处理
df.loc[df['目的地'].isnull(),'目的地'] = [str(x)[3:5] for x in df.loc[df['路线名']

## 【了解即可】拓展：
df.head()

## 提取酒店评分：正则表达式
df['酒店评分'] = df['酒店'].str.extract('(\d\.\d分/5分)')
df.head()

## 提取酒店等级
df['酒店等级'] = df['酒店'].str.extract(' (.+) ') ## .代表任意字符，.+代表出现多次的任意字符
df.head() 