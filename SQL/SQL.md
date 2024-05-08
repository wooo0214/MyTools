## MySQL vs MSSQL

https://www.plesk.com/blog/various/mysql-vs-mssql/

MySQL is an open-source relational database management system, known for its scalability, reliability, and ease of use. It offers a range of features including data integrity, transactions, indexes, and stored procedures, commonly used in web applications, content management systems, and other software solutions that require efficient and organized data storage and retrieval.

MSSQL is an RDBMS developed by MS, using SQL to interact with the db and offers advanced capabilities, such as indexing, stored procedures, and triggers. It supports a wide range of features, including transaction processing, data warehousing, and business intelligence. It interacts well with MS products, making it a popular choice for organizations that rely on the Microsoft ecosystem for their database needs.

### Differences

1. OS: MySQL offers smooth performance on several well-known operating systems such as Windows, Mac OS X, and Linux. MSSQL 


##  https://www.tutorialspoint.com/sql/sql_interview_questions.htm

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

Sql function

    Trunc()
    Nvl(exp1, exp2)
    Nvl2(exp1, exp2,exp3)
    Nullif()
    Coalesce()

    Conditional processing:
        Case
        Decode
        
    Group functions
        Avg
        Count
        Max
        Min
        Sum
        Variance
        stddev

查询：
    子查询
        Select in select
        All [operator]
        Any [operator]
        
    模糊查询
    视图
    Case
    临时建表查询

##  Coursera：Foundations for Big Data Analysis with SQL <https://www.coursera.org/learn/foundations-big-data-analysis-sql/lecture/Qc8OG/what-does-a-dbms-do> 
    ü SQL command 4 categories:

        DDL definition
        DML manipulation
        DQL query
        DCL control
    

    Ø DB design strategy: DB normalization and denormalization
    Ø 3NF: third normalization form - Conditions:
        1. Primary key - every table should have a primary key - good practice: avoid using intelligent key
        2. Atomic columns - atomic means data which cannot be divided further
        3. No repeating groups
        4. Non-key columns describe only the whole key
        5. No derived columns
        
    Ø Denormalization examples:
        1. Allowing dup rows
        2. Pre-joined tables
        3. Derived columns
        4. Summary tables

    Semi-structured data: JSON, XML, CSV with headers

    Transaction - ACID: atomicity, consistency, isolation and durability

    RDBMS Strength
        1. Enforcing business rules
        2. Transactions, OLTP
        3. Structure
        4. Many good choices in relational db softwares
        5. Strong with small or medium data
        6. Simple security controls
        7. Fast (at reasonable scale)
        8. Lots of tools and solutions -- ecosystem

    Limitations for traditional RDBMSs
        1. Schema on write - 
        2. High cost of storage
        3. Weak support for unstructured data
        4. Difficulty of distributed transactions 

## Leetcode

https://leetcode.com/problems/game-play-analysis-iv/

    - Two columns as primary key (col a, col b)
        ○ How to select the row that meets conditions
        ○ You cannot use Alias in where clause, unless you make the selection as a new table
        ○ Datediff(day, d1, d2), returns result of d2 minus d1
    - Divide how to get the float result?
        ○ Int, select 2/4 returns 0
        ○ How to round the result to specified decimal places.