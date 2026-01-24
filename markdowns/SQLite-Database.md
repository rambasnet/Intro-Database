# Sqlite Database

## Topics
- What is Sqlite DB?
- Key Features of Sqlite DB

## What is SQLite DB?

- https://sqlite.org/index.html
- SQLite is a software library that provides a self-contained, serverless, zero-configuration, and transactional SQL database engine
- simpler terms: it's a lightweight, file-based relational database management system that allows you to create, manage, and interact with databases using the SQL language
- commonly used in scenarios where a full-fledged database server might be overkill or unnecessary, such as small to medium-sized applications, mobile apps, embedded systems, and prototyping
- particularly well-suited for projects that need a simple and self-contained database solution without the need for a dedicated database server

## Key Features of Sqlite DB

### Self-Contained

- SQLite operates as a library linked directly into the application
- database engine and the application using it are tightly integrated into a single program

### Serverless

- no separate server process, no need to set up and maintain a database server
- suitable for embedded systems, mobile applications, and desktop applications

### Zero-Configuration
- doesn't require complex configuration or administration
- simply include the SQLite library in your application and start using it

### Transactional
- supports ACID (Atomicity, Consistency, Isolation, Durability) properties, which ensure data integrity and reliability even in the face of system failures or crashes.

### File-Based
- database is stored in a single file on the disk
- makes it easy to manage, backup, and transfer databases

### Cross-Platform
- SQLite is designed to work on various operating systems, including Windows, macOS, Linux, iOS, and Android.

### Supports Standard SQL
- SQLite uses SQL (Structured Query Language) for querying and managing data, making it familiar to those who are already accustomed to relational databases

### Limited Concurrent Access
- supports concurrent read access by multiple processes or threads
- doesn't support concurrent write 
- not recommended for situations with heavy write loads and high-concurrency requirements




## References

- https://www.sqlite.org – SQLite homepage
- https://www.sqlite.org/features.html – SQLite features
- https://www.sqlite.org/copyright.html – SQLite license
- https://www.sqlite.org/docs.html – SQLite documentation


```python

```
