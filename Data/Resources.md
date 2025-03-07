
## Women in big data

https://www.womeninbigdata.org/training/

## Datacamp - Data Engineer

https://www.datacamp.com/learn/onboarding/tracks/associate-data-engineer-in-sql/video

[Enrolled]  -  with SQL (SQL basic see SQL\SQL.md)

[SQL cheat sheet](https://www.databasestar.com/sql-cheat-sheets/)

### Terms

Data lake
    - stores all raw data, all data structures
    - petabytes (1 million GBs)
    - used by data scientist
    - big data, real-time analytics
Data warehouse
    - specific data for specific use
    - relatively small
    - stores mainly structured data
    - also used by analysts

### Relational Databases

- Split tables: entities and affiliations should be split into their own table, one entity/affiliation one table
- Constrains: primary key, foriegn key, not null, unique
- create, alter, drop
- superkeys > keys > primary key
- N:M relations: create a new table without primary key

### Database design

> best practices to design normalized tables in a relational database
> information_schema

- Fact table: has measurements and metrics that would reference to dimentional tables; dimentional table: has attributes
- Star vs snowflake schema
- normalized and denormalized databases
- Normal Forms
    - 1 NF: all rows unique, each cell only has one value
    - 2 NF: 1 NF + non-primary attributes cannot be dependent on subset of candidate keys
    - 3 NF: 2 NF + no transitive dependency for non-prime attributes
- Views
    - create, drop, security, materialized
- Database roles - access control: create, revoke
- Table partitions: vertical, horizontal
    - [syntax examples](https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE-EXAMPLE): partition by list/range
- Integrity

### Data warehousing

- four layers: source, staging, storage, presentation
- ETL/ELT
    - Extract
    - Transform: sorting
    - Load: playlists, reports
- Example to show the design processes:
    - Architecture: bottom up or up bottom
    - Design: Kimball four steps:
        - fact and dim tables design
    - Implementation: on-premise or cloud
    - Data cleaning: ELT or ETL

### Snowflake

A cloud data warehouse

Snowflake sql syntax

> https://docs.snowflake.com/en/reference

- data types
- functions: aggregate, concat, extract, group by all
- joining: natural join (no need to write ON ), lateral (join subquery, to save computation in complex queirys with many joins )
- CTE: common table expressions
- Query optimization
- JSON, semi-structured data: VARIANT data type, functions, querying
    - PARSE_JSON
    - OBJECT_CONSTRUCT

### Visulization

left, right skewed