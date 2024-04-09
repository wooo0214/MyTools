-- MySQL - group by
---- 分组函数

/*
功能：统计，又称聚合函数，统计函数或组函数

分类：
sum
avg
max
min
count
*/

-- 简单使用

SELECT SUM(salary) FROM employees;
SELECT COUNT(salary) FROM employees; -- salary这一栏非空的值的数量

SELECT SUM(salary) 和, AVG(salary) 平均 FROM employees;

SELECT ROUND(AVG(salary),2) FROM employees;

-- 参数支持哪些类型

/*
特点：
1. sum，avg一般用于处理数值型；max，min，count可以处理任何类型
2. 都忽略null值
3. 都可以和distinct搭配，实现去重
4. count的单独介绍
5. 和分组函数一同查询的字段有限制：要求是group by后的字段
*/
SELECT SUM(last_name), AVG(last_name) FROM employees; -- no
SELECT MIN(last_name), MAX(last_name) FROM employees; -- yes, last_name是可排序的
SELECT MIN(hiredate) FROM employees; -- yes 日期可排序 
SELECT COUNT(last_name),COUNT(commission_pct) FROM employees; -- yes，count用于计算非空值

SELECT SUM(commission_pct), AVG(commission_pct), SUM(commission_pct)/35, SUM(commission_pct)/107 FROM employees; -- sum, avg不计算null值
SELECT MAX(commission_pct)， MIN(commission_pct) FROM employees;
SELECT COUNT(commission_pct) FROM employees;

SELECT SUM(DISTINCT salary), SUM(salary) FROM employees;
SELECT COUNT(DISTINCT salary), COUNT(salary) FROM employees;

-- count的单独介绍

SELECT COUNT(*) FROM employees; -- 统计employees表的总行数
SELECT COUNT(1), COUNT(2), COUNT('一个') FROM employees; -- 相当于给表单独加了一栏全为1，2或‘一个’,并统计其个数

-- 效率

MYISAM 存储引擎下，count(*)效率最高
INNODB 存储引擎下，count(*)和count(1)效率差不多，但比count('')要高

-- 测试

-- 1. 查询公司员工工资的最大值、最小值、平均值和总和

SELECT MAX(salary) 最大值, MIN(salary) 最小值, ROUND(AVG(salary),2) 平均值, SUM(salary) 总和 FROM employees;

-- 2. 查询员工表中的最大入职时间和最小入职时间的相差天数（difference）

SELECT DATEDIFF(MAX(hiredate),MIN(hiredate)) Difference FROM employees; 

-- 3. 查询部门编号为90的员工个数

SELECT COUNT(*) FROM employees WHERE department_id = 90;

-- 分组查询

-- 查询每个部门的平均工资

/*
分组数据：
select 分组函数, 列（要求出现在group by的后面）
from ...
where condition
group by group_by_expression;

特点：
1. 分组查询中的筛选条件分为
			数据源			位置		关键字
	分组前筛选	原始表			group by子句前	where
	
	分组后筛选	分组后的结果集		group by子句后	having
	
	①分组函数做条件肯定是放在having子句中
	②能用分组前筛选的，就优先考虑分组前筛选
	
2. group by子句支持单个字段分组，多个字段分组（用逗号隔开，无顺序要求），表达式或函数（用的较少）
3. 可添加排序
*/
SELECT AVG(salary),department_id FROM employees
GROUP BY department_id;

SELECT MAX(salary), job_id FROM employees
GROUP BY job_id;

-- 查询每个位置上的部门个数

SELECT COUNT(*), location_id
FROM departments
GROUP BY location_id;

-- 添加条件

-- 案例一：查询邮箱中包含a字符的，每个部门的平均工资

SELECT AVG(salary), department_id
FROM employees
WHERE email LIKE '%a%'
GROUP BY department_id;

-- 案例二：查询有奖金的每个领导手下员工的最高工资

SELECT MAX(salary), manager_id
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY manager_id;

-- 添加分组后的筛选

-- 案例三： 查询哪个部门的员工个数>2

/*
根据原始表是无法直接得出的，要基于新表 SELECT COUNT(1) AS num, department_id FROM employees
GROUP BY department_id 
1. 查询所有部门员工数量
2. 根据1的结果进行筛选
*/

SELECT * FROM
(SELECT COUNT(1) AS num, department_id FROM employees
GROUP BY department_id) t1
WHERE num > 2;

-- ****having 添加分组后的筛选

SELECT COUNT(*) AS num, department_id FROM employees
GROUP BY department_id
HAVING COUNT(*)>2;

-- 案例四：查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资

SELECT MAX(salary) 最高工资, job_id 工种编号 FROM employees
WHERE commission_pct IS NOT NULL  -- 对原始表的筛选，分组前的筛选
GROUP BY job_id
HAVING 最高工资 > 12000; -- 分组后的筛选

-- 案例五：查询领导编号>102的每个领导手下的最低工资>5000的领导编号，以及其最低工资

SELECT MIN(salary) 最低工资, manager_id 领导编号 FROM employees
WHERE manager_id > 102
GROUP BY manager_id
HAVING 最低工资 > 5000;

-- 按表达式或函数分组

-- 案例六：按员工姓名长度分组，查询每一组的员工个数，筛选员工个数>5的有哪些

SELECT COUNT(*) c, LENGTH(last_name) len FROM employees
GROUP BY len
HAVING c > 5; -- mysql 中， group by和having后支持使用别名，但oracle等中不支持

-- 按多个字段分组

-- 案例七：查询每个部门每个工种的员工的平均工资

SELECT AVG(salary), department_id, job_id FROM employees
GROUP BY department_id, job_id;

-- 添加排序,筛选条件

SELECT AVG(salary) avg_sal, department_id, job_id FROM employees
WHERE department_id IS NOT NULL
GROUP BY  job_id,department_id
HAVING avg_sal > 10000
ORDER BY avg_sal DESC;

-- 分组查询案例讲解

	--1. 查询各job_id员工工资的最大值，最小值，平均值，总和，并按job_id升序
SELECT job_id, MAX(salary), MIN(salary), AVG(salary), SUM(salary) FROM employees
GROUP BY job_id
ORDER BY job_id;
	--2. 查询员工最高工资和最低工资的差距
SELECT (MAX(salary) - MIN(salary)) Difference FROM employees;
	--3. 查询各个管理者手下员工的最低工资，其中最低工资不低于6000，没有管理者的员工不计算在内
-- select min(salary), manager_id from employees
-- where salary > 7000 and manager_id is not null
-- group by manager_id;

SELECT MIN(salary), manager_id FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary) >= 6000; 

	--4. 查询所有部门的编号，员工数量和工资平均值， 并按平均工资降序
SELECT department_id, COUNT(1), COUNT(*), AVG(salary) FROM employees
GROUP BY department_id
ORDER BY AVG(salary) DESC;
	--5. 选择具有各个job_id的员工人数
SELECT COUNT(1), job_id FROM employees
GROUP BY job_id;

