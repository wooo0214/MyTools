# 连接查询

/*
笛卡尔乘积现象： 表1有m行，表2有n行，结果为m*n行

发生原因：没有有效的连接条件

分类：
	按年代分类：sql92标准（仅支持内连接），sql99标准（推荐；支持内连接+外连接（左外和右外）+交叉连接）
	按功能分类：
		内连接：等值连接，非等值连接，自连接
		外连接：左外连接，右外连接，全外连接
		交叉连接

*/

SELECT * FROM beauty;
SELECT * FROM boys;

# 一、sql92
# 1、等值连接
# 案例一：查询女名和对应男名
SELECT NAME,boyName 
FROM boys i, beauty u
WHERE u.boyfriend_id = i.id;

# 案例二：查询员工名和对应的部门名; 为表起别名（起别名后，select查询字段就不能用原来的表名）
SELECT last_name, department_name, e.department_id, e.commission_pct
FROM employees e, departments d  # 顺序无关
WHERE e.department_id=d.department_id
AND e.commission_pct IS NOT NULL; # 可以加筛选

# 2、非等值连接 
# 案例一：查询员工的工资和工资级别

/*CREATE TABLE job_grades
(grade_level VARCHAR(3),
 lowest_sal  int,
 highest_sal int);

INSERT INTO job_grades
VALUES ('A', 1000, 2999);

INSERT INTO job_grades
VALUES ('B', 3000, 5999);

INSERT INTO job_grades
VALUES('C', 6000, 9999);

INSERT INTO job_grades
VALUES('D', 10000, 14999);

INSERT INTO job_grades
VALUES('E', 15000, 24999);

INSERT INTO job_grades
VALUES('F', 25000, 40000);*/

SELECT salary, grade_level
FROM employees e, job_grades g
WHERE salary BETWEEN g.lowest_sal AND g.highest_sal;

# 3、自连接
# 案例：查询员工名和上级的名字
SELECT yg.last_name '员工名', sj.last_name '上级'
FROM employees yg, employees sj
WHERE yg.employee_id=sj.employee_id;

