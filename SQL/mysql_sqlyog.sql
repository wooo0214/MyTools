/*
数据库常见概念：DB, DBMS, SQL
数据库存储数据特点：
	1.数据存放到表中，表(table)再放到库(database)中
	2.一个库中可有多张表，每张表有唯一的表名用来标识自己
	3.表中有一个或多个列(columns)，列又称为“字段”
	4.表中的每一行数据，相当于java中“对象”

常见数据库管理系统：mysql, db2, oracle, sql server

mysql
背景：MySql AB > sun > Oracle
优点：开源免费；成本低 ；性能高，移植性好；体积小，便于安装
*/

--DQL, data query language
--basic query

/*
select 查询列表 from 表名

特点：
1. 表中的字段、常量值、表达式、函数
2. 查询结果是虚拟的表格

*/

USE myemployees;

SELECT `name` FROM stuinfo;

-- 查询常量值
SELECT 100;
SELECT 'john';

--表达式
SELECT 100%98;

--函数
SELECT VERSION();

--起别名
SELECT 100%98 AS 结果;
SELECT last_name AS 姓 FROM employees; 
SELECT first_name 名 FROM employees;

SELECT salary AS OUT pot FROM employees;
SELECT salary AS "out put" FROM employees; 

--去重 distinct
SELECT DISTINCT department_id FROM employees;

-- +号的作用: 只作为运算符
/*
如 
select 100+90；两个操作数均为数值型，则做加法运算
select '123'+90; 其中一方为字符型，试图将其转化为数值型：如果转化成功，则继续做加法运算；如失败，则将字符型值转化为0 
select null+10; 只要有null，结果就是null

*/
-- wrong:
SELECT 
	last_name+first_name AS 姓名
FROM
	employees;
-- correct: use CONCAT()	
SELECT CONCAT(last_name,first_name) AS 姓名 FROM employees;

-- 显示表的结构
DESC departments;

-- test
-- 显示出表employees的全部列，各列之间用逗号连接，列头显示为OUT_PUT
-- ifnull()
SELECT 
	IFNULL(commission_pct,0) AS 奖金率,
	commission_pct
FROM
	employees;
	

SELECT 
	CONCAT(`employee_id`,',',`first_name`,',',`last_name`,',',`email`,',',`phone_number`,',',`job_id`,',',`salary`,',',IFNULL(`commission_pct`,0),',',`manager_id`,',',`department_id`,',',`hiredate`) AS OUT_PUT
FROM
	employees;

--条件查询 where
/*
分类：
	1. 按条件表达式筛选
	条件运算符： > < = != <> >= <=
	2. 按逻辑表达式
	逻辑运算符：
	作用：连接条件表达式
		&& || !
		and or not
	3.模糊查询
		like
		between and
		in
		is null
		is not null
	
*/
-- 查询员工名中包含字符a的员工信息:like
/*
特点：
	1. 一般和通配符搭配使用：
	% 任意多个字符，包含0字符
	_ 任意单个字符
*/
SELECT
	*
FROM 
	employees
WHERE
	last_name LIKE '%a%';
-- 员工名第三个字符为n，第五个字符为l的
SELECT
	*
FROM 
	employees
WHERE
	last_name LIKE '__n_l%';
	
-- 员工名第二个字符为_的员工
SELECT
	*
FROM 
	employees
WHERE
	last_name LIKE '_\_%'; --\ 转义字符
	--last_name like '_$_%' escape '$'; $可以为任意字符
	
-- between and
/*
1. 提高语句简洁度
2. 包含临界值
3. 两个临界值不能调换顺序
*/
SELECT
	*
FROM 
	employees
WHERE
	employee_id BETWEEN 100 AND 120;
	
-- in
/*
1. 提高语句简洁度
2. in列表的值类型必须一致或兼容；兼容：如‘123’和123
*/
SELECT
	*
FROM 
	employees
WHERE
	job_id IN ('it_prog','ad_vp','ad_pres');

-- is null
/*
=, <>不能用于判断null值
is null, is not null可以用于判断null值
*/
SELECT
	*
FROM 
	employees
WHERE
	commission_pct IS NULL;
	
--安全等于 <=>

--案例一：查询没有奖金的员工名和奖金率
SELECT
	last_name,
	commission_pct
FROM
	employees
WHERE
	commission_pct <=> NULL;

--案例二：查询工资为12000的
SELECT
	last_name,
	commission_pct
FROM
	employees
WHERE
	salary <=> 12000;

-- is null vs <=>
/*
is null: 仅仅可以判断null值，可读性较高，建议使用
<=>: 既可以判断null值，也可以判断普通的数值，可读性较低

*/

--测试题1，p37
SELECT * FROM employees WHERE commission_pct IS NULL AND salary < 18000;
SELECT * FROM employees WHERE job_id != 'IT' OR salary = 12000;
DESC departments;
SELECT DISTINCT location_id FROM departments;
--5. 不一样； 
/*
如果判断的字段有null值的话：
select * from employees 选取的是employees表中的所有内容，包含commission_pct为null或者last_name为null的行；
select * from employees 选取的是同时满足① commission_pct不为null 和② last_name不为null 两个条件的行; 相当于对上一条的结果做了去空
*/

-- 排序查询 order by *** asc|desc
/*
1. 如果不写，默认升序
2. order by 子句中可支持单个字段、多个字段、表达式、函数、别名
3. order by 子句一般放在最后，limit子句除外【from > where > select > order】
*/
--
SELECT * FROM employees
WHERE department_id >= 90
ORDER BY hiredate ASC;

-- 按年薪【按年薪表达式排序】高低显示
SELECT *, salary*12*(1+IFNULL(commission_pct,0)) 年薪
FROM employees
ORDER BY salary*12*(1+IFNULL(commission_pct,0)) DESC;

-- 按年薪【按别名排序】高低显示
SELECT *, salary*12*(1+IFNULL(commission_pct,0)) 年薪
FROM employees
ORDER BY 年薪 DESC;

-- 按姓名长度显示员工姓名和工资 【按函数排序】
SELECT LENGTH(last_name) 字节长度, last_name, salary FROM employees
ORDER BY LENGTH(last_name) DESC;

-- 先按工资升序，再按员工编号降序排序【按多个字段排序】
SELECT * FROM employees
ORDER BY salary ASC, employee_id DESC;

-- 案例
--1. 查询员工姓名和部门号和年薪，按年薪降序，按姓名升序
SELECT last_name, department_id, salary*12*(1+IFNULL(commission_pct,0)) 年薪
FROM employees
ORDER BY 年薪 DESC, last_name ASC;

--2. 选择工资不在8000到17000的员工的姓名和工资，按工资降序
SELECT last_name, salary
FROM employees
WHERE salary < 8000 OR salary > 17000 -- where salary not between 8000 and 17000
ORDER BY salary DESC;

--3. 查询邮箱中包含e的员工信息，并先按邮箱的字节数降序，再按部门号升序
SELECT * FROM employees
WHERE email LIKE '%e%'
ORDER BY LENGTH(email) DESC, department_id ASC;

-- 常见函数
/*
好处：隐藏了实现细节；提高代码的重用性
调用：select 函数名（实参列表）【from 表】
特点：
	1.叫什么（函数名）
	2.干涉么（函数功能）
	
分类：
	1.单行函数：concat, length, ifnull等
	2.分组函数，又称统计函数，聚合函数，组函数
	
sum，常见函数：
	字符函数：
		length
		
	数学函数：
	
	日期函数：
	now
	curdate
	curtime
	year
	month
	monthname
	day
	hour
	minute
	second
	str_to_date
	date_format
	
	其他函数：
		version
	控制函数：

*/
-- 字符函数 length
SELECT LENGTH('john'); -- return 4
SELECT LENGTH('一二三hahaha')；-- return 15
 
SHOW VARIABLES LIKE '%char%';

-- concat 拼接字符串
-- upper, lower
SELECT UPPER('john')

SELECT CONCAT(UPPER(last_name),' ',LOWER(first_name)) FROM employees;

-- substr, substring; 索引从1开始
--截取从指定字符处后面所有字符
SELECT SUBSTR('李莫愁陆展元',4) out_put;
--截取从指定索引处指定字符长度的字符
SELECT SUBSTR('李莫愁陆展元',1,3) out_put;

SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),LOWER(SUBSTR(last_name,2)),'_',UPPER(SUBSTR(first_name,1,1)),LOWER(SUBSTR(first_name,2))) 姓名 FROM employees;

-- instr: 返回字串第一次出现的索引，如果找不到返回0

SELECT INSTR('杨不悔殷六侠','殷六侠') AS out_put;

-- trim: 去掉前后空格
SELECT LENGTH(TRIM('   一二三    ')) AS out_put;
SELECT TRIM('a' FROM 'aaaaayiensaaaaa') AS out_put;

-- lpad(a,b,c): 用指定字符c实现左填充指定长度b
SELECT LPAD('yi',10,'*') AS out_put;
SELECT LPAD('yier',2,'*') AS out_put;

-- rpad(a,b,c): 用指定字符c实现右填充指定长度b
SELECT RPAD('yi',10,'*') AS out_put;
SELECT RPAD('yier',2,'*') AS out_put;

-- replace
SELECT REPLACE('周芷若周芷若周芷若张无忌与周芷若','周芷若','赵敏') AS out_put;

-- 数学函数

--round 四舍五入
SELECT ROUND(1.65);
SELECT ROUND(-1.45);
SELECT ROUND(1.567,2);

--ceil 向上取整, 返回>=该参数的最小整数
SELECT CEIL(1.02);
SELECT CEIL(-1.01);

--floor 向下取整，返回<=该参数的最大整数
SELECT FLOOR(-9.99);

-- truncate 截断,小数点后保留指定位数
SELECT TRUNCATE(1.69999,2);

-- mod 取余
/*
mod(a,b) a-a/b*b
*/
SELECT MOD(-10,-3);
SELECT -10%-3;

-- 日期函数

-- now 返回当前系统日期+时间
SELECT NOW();
SELECT CURDATE(); --返回当前系统日期，不包含时间
SELECT CURTIME(); --返回当前时间

-- 获取指定的部分：年，月，日，小时，分钟，秒
SELECT YEAR(NOW()) 年;
SELECT YEAR('1997-1-1') 年;
SELECT MONTH(NOW());
SELECT MONTHNAME(NOW()); -- 英文月份名称
SELECT HOUR(NOW());
SELECT MIN(NOW());
SELECT SECOND(NOW());

-- str_to_date('9-13-1998','格式') 将字符通过指定的格式转化成日期
/*
格式符：
%Y 四位的年份
%y 两位
%m 月份，补零
%c 月份
%d 日
%H 24
%h 12
%i 分钟
%s 秒
*/
SELECT STR_TO_DATE('1998-3-2','%Y-%c-%d') out_put;

-- 例：查询入职日期为1992-4-3的员工信息
SELECT * FROM employees WHERE hiredate='1992-4-3';
SELECT * FROM employees WHERE hiredate=STR_TO_DATE('4-3 1992','%m-%d %Y');

-- date_format 将日期转换成字符
SELECT DATE_FORMAT(NOW(),'%y年%m月%d日') AS out_put;

-- 例：查询有奖金的员工名和入职日期（xx月/xx日 xx年）
SELECT last_name, DATE_FORMAT(hiredate,'%m月/%d日 %y年') 入职日期
FROM employees
WHERE commission_pct IS NOT NULL;

-- 其他函数
SELECT VERSION();
SELECT DATABASE();
SELECT USER();

-- 流程控制函数
-- if(expr1,expr2,expr3)

SELECT IF(10>5,'大','小');

SELECT last_name, commission_pct, IF(commission_pct IS NULL,'wu','you') 备注
FROM employees;

-- case 
CASE?

/*
-- case使用一. 适用于等值判断
case 要判断的变量或字段或表达式
when 常量1 then 要显示的值1 或语句1;  （值后面不用加; 语句要加;）
when 常量2 then 要显示的值2 或语句2;
...
else 值n或语句n;
end

表达式 - 值
字段 - ？

*/

/*
案例： 查询员工工资，要求
部门号=30，显示工资为1.1倍
部门号=40，显示工资为1.2倍
部门号=50，显示工资为1.3倍
*/

SELECT salary 原始工资, department_id,
CASE department_id
WHEN 30 THEN salary*1.1
WHEN 40 THEN salary*1.2
WHEN 50 THEN salary*1.3
ELSE salary
END AS 新工资 FROM employees;

-- case使用二: 类似多重if。区间
/*
case
when 条件1 then 要显示的值1 或语句1;
when 条件2 then 要显示的值2 或语句2;
...
else 要显示的值n 或语句n;
end
*/

/*
案例： 查询员工的工资情况
如果工资>20000， 显示A级别
工资>15000,B
工资>10000，C
否则，D
*/

SELECT salary,
CASE
WHEN salary > 20000 THEN 'A'
WHEN salary > 15000 THEN 'B'
WHEN salary > 10000 THEN 'C'
ELSE 'D'
END AS 工资级别
FROM employees;

-- 单行函数 案例讲解
-- 1. 显示系统时间（日期+时间）
SELECT NOW();
-- 2. 查询员工号，姓名，工资，以及工资提高百分之20%后的结果（new salary）
SELECT employee_id, CONCAT(first_name,last_name) AS 'Employees Names', salary, salary*1.2 AS 'New salary'
FROM employees;
-- 3. 将员工的姓名按首字母排序，并写出姓名的长度
SELECT last_name, LENGTH(last_name) 长度
FROM employees
ORDER BY SUBSTR(last_name,1,1) ASC;
-- 4. 做一个查询，产生下面的结果：
/*
<last_name> earns <salary> monthly but wants <salary*3>
Dream Salary
King earns 24000 monthly but wants 72000
*/ 
SELECT CONCAT(REPLACE(last_name,'_',''),' earns ',salary,' monthly but wants ',salary*3) AS 'Dream Salary' 
FROM employees
WHERE salary=24000;
-- 5. 使用case-when，按照下面的条件：
/*
job		grade
AD_PRES		A
ST_MAN		B
IT_PROG		C
SA_REP		D
ST_CLERK	E
产生下面的结果：
last_name	job_id	grade
king		ADPRES	A

*/
SELECT last_name, job_id AS job,
CASE job_id
WHEN 'AD_PRES' THEN 'A'
WHEN 'ST_MAN' THEN 'B'
WHEN 'IT_PROG' THEN 'C'
WHEN 'SA_REP' THEN 'D'
WHEN 'ST_CLERK' THEN 'E'
-- else null . 未说明其他情况可以省略else
END AS grade
FROM employees
WHERE job_id = 'AD_PRES'
ORDER BY grade;