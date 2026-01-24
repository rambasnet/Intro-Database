# Relational Database Concepts

- widely used type of database management system (DBMS) that organize data into tables with rows and columns
- relational databases use the following concepts
- deep understanding of these concepts help you mastering relational databases

## Database Schema

- a schema refers to the logical and structural organization of a database
- defines the layout, design, and relationships of the database objects, such as tables, views, indexes, and constraints
- it provides a blueprint for how data is stored, how it is organized, and how different parts of the database are interconnected

### Databae Schema: E-Commerce System

- let's consider a simple example of a database schema for an e-commerce platform that tracks products, customers, and orders
- this schema will define the structure and relationships between tables

#### Table: Customers

| Column       | Data Type   | Constraints         |
|:-------------|:------------|:--------------------|
| CustomerID   | INT         | Primary Key         |
| FirstName    | VARCHAR(50) | Not Null            |
| LastName     | VARCHAR(50) | Not Null            |
| Email        | VARCHAR(100)| Not Null, Unique    |
| Phone        | VARCHAR(20) |                     |

#### Table: Products

| Column       | Data Type   | Constraints         |
|:-------------|:------------|:--------------------|
| ProductID    | INT         | Primary Key         |
| ProductName  | VARCHAR(100)| Not Null            |
| Price        | DECIMAL(10,2)| Not Null           |
| Category     | VARCHAR(50) |                     |

#### Table: Orders

| Column       | Data Type   | Constraints         |
|:-------------|:------------|:--------------------|
| OrderID      | INT         | Primary Key         |
| CustomerID   | INT         | Foreign Key (Customers) |
| OrderDate    | DATE        | Not Null            |
| TotalAmount  | DECIMAL(10,2)| Not Null            |

#### Table: OrderDetails

| Column       | Data Type   | Constraints         |
|--------------|-------------|---------------------|
| OrderID      | INT         | Foreign Key (Orders)|
| ProductID    | INT         | Foreign Key (Products)|
| Quantity     | INT         | Not Null            |


## Tables and Records

- explanation of tables as the primary data storage units
- understanding rows (also called records or tuples) as individual data entries in a table
- columns (also called attributes or fields) as data characteristics stored in each record

### Example: Customer Table with Records

| CustomerID | FirstName | LastName | Email               |
|------------|-----------|----------|---------------------|
| 101        | John      | Doe      | john@example.com   |
| 102        | Jane      | Smith    | jane@example.com   |
| 103        | Michael   | Johnson  | michael@example.com|


## Primary keys

- definition of primary keys as unique identifiers for records within a table
- importance of primary keys in maintaining data integrity and ensuring record uniqueness
- illustration of primary key constraints

## Foreign Keys and Relationships

- introduction to foreign keys as references to primary keys in other tables.
- explanation of how foreign keys establish relationships between tables.
- different types of relationships: one-to-one, one-to-many, and many-to-many.

## Constraints and Data Integrity

- discussion of various constraints, including unique constraints and not-null constraints
- Explanation of how constraints ensure data validity and integrity
- Role of constraints in preventing incorrect or incomplete data

## Database Normalization

- introduction to normalization as a process for organizing data to minimize redundancy and data anomalies
- explanation of normalization forms (1NF, 2NF, 3NF, etc.)
- illustration of normalization through examples and practical scenarios

## Denormalization

- understanding denormalization as the deliberate introduction of redundancy for performance optimization
- when and why denormalization might be used in certain scenarios

## Relational Algebra

- basic introduction to relational algebra, a set of mathematical operations used to manipulate relational data
- operations like SELECT, PROJECT, JOIN, and UNION, and their practical implications

## Entity-Relationship (ER) Modeling

- overview of ER modeling as a visual representation of data relationships
- use of symbols like entities, attributes, and relationships in creating ER diagrams


## Practical Examples and Queries
- Applying concepts to real-world scenarios
- Writing SQL queries to perform CRUD (Create, Read, Update, Delete) operations


```python

```
