
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

- Fact table, dimentional table
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