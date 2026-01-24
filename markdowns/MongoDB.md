# MongoDB

- https://www.mongodb.com/

- popular open-source NoSQL (non-relational) database management system designed for handling large volumes of unstructured or semi-structured data
- often used in modern web and mobile applications, as well as in various other data-intensive use cases
    - including content management systems, e-commerce platforms, real-time analytics, and IoT (Internet of Things) applications. Its flexibility, scalability, and ease of use make it a popular choice for developers working with diverse and evolving data requirements

## Here are some key characteristics and features of MongoDB:

### Document-Oriented

- MongoDB stores data in a format called BSON (Binary JSON), which is a binary-encoded serialization of JSON-like documents
- these documents can have flexible and varying structures, making it suitable for handling data with changing schemas

### Schema-less

- MongoDB is schema-less, which means that you can insert data without defining a rigid schema beforehand
- this flexibility makes it well-suited for projects where data structures evolve over time

## Scalability

- MongoDB is designed for horizontal scalability, making it capable of handling large amounts of data and high levels of traffic
- It can be used in clusters to distribute data across multiple servers for load balancing and fault tolerance

### Rich Query Language
- MongoDB provides a powerful query language for querying and retrieving data
- You can perform complex queries, including filtering, sorting, and aggregation, using the MongoDB Query Language (MQL)

### Indexing
- MongoDB supports the creation of indexes on fields in your documents, which can significantly improve query performance

### Geospatial Capabilities
- MongoDB includes geospatial features, allowing you to perform geospatial queries and store and analyze location-based data

### Replication and High Availability
- MongoDB supports replica sets, which are groups of MongoDB servers that maintain identical copies of data 
- this provides data redundancy and high availability in case of server failures

### Sharding
- MongoDB allows data to be distributed across multiple servers or shards, which can improve performance and scalability even further


## MongoDB Document

- records in MongoDB are called documents
- has structure similar to JSON called BSON (Binary JSON)
- e.g.,

```json
{
	title: "Post Title 1",
	body: "Body of post.",
	category: "News",
	likes: 1,
	tags: ["news", "events"],
	date: Date()
}
```
- keys are strings without quotes, and the field values may include numbers, strings, booleans, arrays, or even nested documents

## MongoDB Server

- can download and install free community edition or use cloub-based Atlas
- we'll utilize cloud-based free edition of MongoDB server
- use Python PyMongo database driver - [https://www.mongodb.com/docs/drivers/pymongo/](https://www.mongodb.com/docs/drivers/pymongo/)
- install pymongo using pip

```bash
$ pip install pymongo
$ python -m pip install pymongo
```

## Create your free account or signup using GitHub or Google
- [https://account.mongodb.com/account/login](https://account.mongodb.com/account/login)

### Create Organization

- let's call it intro-db

### Create New Project

- let's call it demo-db

### Create Deployment

- Pick FREE deployment

### Create a db user

- give a name such as db-user
- use Certificate for authentication
- set certificate expiration - 6 months
- save the certificate in your system
- add your current IP address in list
- load sample data

### MongoDB ServerAPI docs

- [https://pymongo.readthedocs.io/en/stable/api/pymongo/server_api.html](https://pymongo.readthedocs.io/en/stable/api/pymongo/server_api.html)


```python
from pymongo import MongoClient
from pymongo.server_api import ServerApi
```


```python
path_to_certificate = 'python/x509-cert-MongoDB-Atlas.pem'
```


```python
uri = "mongodb+srv://cluster0.xeszaub.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
```


```python
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
```


```python
db = client['testDB']
collection = db['testCol']
doc_count = collection.count_documents({})
print(doc_count) # Should print 0 as the testDB doesn't exist 
```

    0



```python
# let's connect to sample_airbnb database
# this database is generated when you load sample data
db = client['sample_airbnb']
```


```python
collection = db['listingsAndReviews']
```


```python
doc_count = collection.count_documents({})
```


```python
doc_count
```




    5555



## SQL to MongoDB Mapping Chart

- [See docs](https://www.mongodb.com/docs/manual/reference/sql-comparison/)


```python

```
