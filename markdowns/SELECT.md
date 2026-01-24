# READ

- the "READ" operation refers to the action of fetching or accessing existing data from a database or data storage system 
- the "R" in CRUD involves querying the database to retrieve/read specific records or information
- the READ operation is primarily implemented using SQL SELECT statements in relational databases, but it can also involve using various methods and functions provided by other types of data storage systems
- https://sqlite.org/lang_select.html
- syntax:

```sql
SELECT DISTINCT column_list
FROM table_list
  JOIN table ON join_condition
WHERE row_filter
ORDER BY column_list
LIMIT count OFFSET offset
GROUP BY column_name
HAVING group_filter;
```

- use GROUP BY to get the group rows into groups and apply aggregate function for each group
- use ORDER BY clause to sort the result set
- use DISTINCT clause to query unique rows in a table
- use WHERE clause to filter rows in the result set
- use LIMIT OFFSET clauses to constrain the number of rows returned
- use INNER JOIN or LEFT JOIN to query data from multiple tables using join
- use GROUP BY to get the group rows into groups and apply aggregate function for each group
- use HAVING clause to filter groups

### Select from a single table

- run the following command against chinook.db using DBeaver

```sql
SELECT
	trackid,
	name,
	composer,
	unitprice
FROM
	tracks;
```

### * shorthand wildcards

```sql
SELECT *
FROM tracks;
```
- best practice is to use column names explictly so you know what columns and data you're getting
- retrieving unnecessary data can have many negative effect to your application


## ORDER BY
- SQLite stores data in the tables in an unspecified order
- sorting/ordering data can be very useful in many applications
- sql result set can be sorted based on one or more columns in ascending or descending order

```sql
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,
    column_2 DESC;
```

- run the following SQL commands against chinook.db usinb DBeaver

```sql
SELECT
	name,
	milliseconds, 
    albumid
FROM
	tracks
ORDER BY
    albumid ASC;
```

- SQLite uses `ASC` by default so you can't omit it in the ORDER BY

```sql
SELECT
	name,
	milliseconds, 
	albumid
FROM
	tracks
ORDER BY
	albumid ASC,
    milliseconds DESC;
```

```sql
SELECT 
    TrackId, 
    Name, 
    Composer 
FROM 
   tracks
ORDER BY 
   Composer;
```
- NULL values are considered missing or not applicable and appear in the beginning of the set
- NULLS LAST and NULLS FIRST options can be used with ORDER BY clause

```sql
SELECT 
    TrackId, 
    Name, 
    Composer 
FROM 
    tracks
ORDER BY 
    Composer NULLS LAST;
```

## DISTINCT
- optional clause 
- allows you to remove the duplicate rows in the result set

```sql
SELECT DISTINCT	select_list
FROM table;
```

- run the following command against chinook.db using DBeaver

```sql
SELECT DISTINCT city
FROM customers 
ORDER BY city;
```

```sql
SELECT DISTINCT company
FROM customers
ORDER BY company;
```

## WHERE
- optional clause; used to provide filter/search condition for rows to be returned by the query
- syntax:

```sql
SELECT
	column_list
FROM
	table
WHERE
	search_condition;
```

- WHERE has the folloing form:

```sql
left_expression COMPARISON_OPERATOR right_expression
```
- e.g.:
```
WHERE column = 100;
WHERE column IN (1,2,3);
WHERE column LIKE 'An%';
WHERE column BETWEEN 10 AND 20;
```

### SQLite comparision operators

| Operator | Meaning |
|:-------| -------- |
| = | Equal to |
| <> or != | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

### SQLite logical operators

- allows you to test the truth of some expressions
- returns 1, 0, or a NULL value
- 1 means TRUE and 0 means FALSE

| Operator | Meaning |
| :--- | :--- |
| ALL | returns 1 if all expressions are 1|
| AND |  returns 1 if both expressions are 1, and 0 if one of the expressions is 0 |
| ANY | returns 1 if any of a set of comparisons is 1|
| BETWEEN | return 1 if a value is within a range |
| EXISTS | returns 1 if a subquery contains any rows |
| IN | returns 1 if a value is in a list of values |
| LIKE | returns 1 if a value matches a pattern |
| NOT | reverses the value of other operators |
| OR | returns 1 if either expression is 1 |


- let's use chinook.db with DBeaver

```sql
SELECT
   name,
   milliseconds,
   bytes,
   albumid
FROM
   tracks
WHERE
   albumid = 1;
```

```sql
SELECT
	name,
	milliseconds,
	bytes,
	albumid
FROM
	tracks
WHERE
	albumid = 1
AND milliseconds > 250000;
```

- LIKE operator can be used to match one or more any character in string comparison

```sql
SELECT
	name,
	albumid,
	composer
FROM
	tracks
WHERE
	composer LIKE '%Smith%'
ORDER BY
	albumid;
```

- IN operator can be used to test if a value is in a set

```sql
SELECT
	name,
	albumid,
	mediatypeid
FROM
	tracks
WHERE
	mediatypeid IN (1, 3);
```

### LIMIT

- limit clause constrains the number of rows returned by the query

```sql
SELECT
	trackid,
	name,
	milliseconds
FROM
	tracks
ORDER BY
	milliseconds ASC
LIMIT 5;
```

### OFFSET 

- limiting the nth highest or the lowest value

```sql
SELECT
	trackid,
	name,
	milliseconds
FROM
	tracks
ORDER BY
	milliseconds DESC
LIMIT 1 OFFSET 1;
```

### IS NULL
- checking if column or expression is NULL
- can't use `=` operator to compare to NULL

```sql
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NULL
ORDER BY 
    Name;   
```

### IS NOT NULL

```sql
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY 
    Name;
```


## SELECT with Python

- SELECT returns 0 or many records based on the query
- use cursor's fetchone() or fetchall() methods to return one or all the records
- fetchone returns the first row as a tuple from the result set
- fetchall returns all the rows as list of tuples


```python
from python import db
```


```python
help(db)
```

    Help on module python.db in python:
    
    NAME
        python.db - Sqlite Database wrapper.
    
    DESCRIPTION
        This module provides a wrapper for sqlite3 database operations.
        
        Example:
            import db
        
            # create a database connection
            conn = db.create_connection("sqlite.db")
            db.close_connection(conn)
    
    FUNCTIONS
        close_connection(conn: sqlite3.Connection) -> None
            Close a database connection to a SQLite database.
            Args:
              conn (Connection): Connection object
        
        create_connection(db_file: str) -> sqlite3.Connection
            Create sqlite3 connection and return it.
            
            Args:
                db_file (str): sqlite filename to open or create.
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Returns:
                sqlite3.Connection: sqlite3 connection object.
        
        create_table(db_file: str, create_table_sql: str) -> None
            Create a table from the create_table_sql statement
            Args:
                db_file (str): database file path
                create_table_sql (str): a CREATE TABLE statement
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                None
        
        delete(db_file: str, delete_sql: str, where: tuple[typing.Any]) -> int
            Delete a table from the delete_sql statement
            Args:
              db_file (str): database file path
              delete_sql (str): a DELETE statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows_affected (int): number of rows affected
        
        insert_many_rows(db_file: str, insert_rows_sql: str, rows: list[tuple[str]]) -> int
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              rows (list[tuple]): list of tuples as rows to be inserted for parameterized query
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                row_id (int): row id of the last inserted row
        
        insert_one_row(db_file: str, insert_row_sql: str, row: tuple[typing.Any]) -> int
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              row (tuple): row as tuple to be inserted
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                row_id (int): row id of the last inserted row
        
        select_many_rows(db_file: str, select_rows_sql: str, where: tuple[typing.Any]) -> Any
            Select all rows from a table from the select_data_sql statement
            Args:
              db_file (str): database file path
              select_data_sql (str): an SELECT statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows (Any): list of tuples as rows or None
        
        select_one_row(db_file: str, select_row_sql: str, where: tuple[str]) -> Any
            API to select one row from a table from the select_data_sql statement.
            
            Args:
                db_file (str): database file path
                select_row_sql (str): a SELECT statement
                where (tuple[str]): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Returns:
                tuple[str]: row as tuple or None
        
        update(db_file: str, update_sql: str, where: tuple[typing.Any]) -> int
            Update a table from the update_sql statement
            Args:
              db_file (str): database file path
              update_sql (str): an UPDATE statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows_affected (int): number of rows affected
    
    DATA
        Any = typing.Any
            Special type indicating an unconstrained type.
            
            - Any is compatible with every type.
            - Any assumed to have all methods.
            - All values assumed to be instances of Any.
            
            Note that all the above statements are true from the point of view of
            static type checkers. At runtime, Any should not be used with instance
            or class checks.
    
    FILE
        /Users/rbasnet/projects/Intro-Database/python/db.py
    
    



```python
db_file = 'data/chinook.sqlite'
```


```python
select = 'SELECT * from artists'
```


```python
row = db.select_one_row(db_file, select, ())
```


```python
row
```




    (1, 'AC/DC')




```python
rows = db.select_many_rows(db_file, select, ())
```


```python
rows
```




    [(1, 'AC/DC'),
     (2, 'Accept'),
     (3, 'Aerosmith'),
     (4, 'Alanis Morissette'),
     (5, 'Alice In Chains'),
     (6, 'Antônio Carlos Jobim'),
     (7, 'Apocalyptica'),
     (8, 'Audioslave'),
     (9, 'BackBeat'),
     (10, 'Billy Cobham'),
     (11, 'Black Label Society'),
     (12, 'Black Sabbath'),
     (13, 'Body Count'),
     (14, 'Bruce Dickinson'),
     (15, 'Buddy Guy'),
     (16, 'Caetano Veloso'),
     (17, 'Chico Buarque'),
     (18, 'Chico Science & Nação Zumbi'),
     (19, 'Cidade Negra'),
     (20, 'Cláudio Zoli'),
     (21, 'Various Artists'),
     (22, 'Led Zeppelin'),
     (23, 'Frank Zappa & Captain Beefheart'),
     (24, 'Marcos Valle'),
     (25, 'Milton Nascimento & Bebeto'),
     (26, 'Azymuth'),
     (27, 'Gilberto Gil'),
     (28, 'João Gilberto'),
     (29, 'Bebel Gilberto'),
     (30, 'Jorge Vercilo'),
     (31, 'Baby Consuelo'),
     (32, 'Ney Matogrosso'),
     (33, 'Luiz Melodia'),
     (34, 'Nando Reis'),
     (35, 'Pedro Luís & A Parede'),
     (36, 'O Rappa'),
     (37, 'Ed Motta'),
     (38, 'Banda Black Rio'),
     (39, 'Fernanda Porto'),
     (40, 'Os Cariocas'),
     (41, 'Elis Regina'),
     (42, 'Milton Nascimento'),
     (43, 'A Cor Do Som'),
     (44, 'Kid Abelha'),
     (45, 'Sandra De Sá'),
     (46, 'Jorge Ben'),
     (47, 'Hermeto Pascoal'),
     (48, 'Barão Vermelho'),
     (49, 'Edson, DJ Marky & DJ Patife Featuring Fernanda Porto'),
     (50, 'Metallica'),
     (51, 'Queen'),
     (52, 'Kiss'),
     (53, 'Spyro Gyra'),
     (54, 'Green Day'),
     (55, 'David Coverdale'),
     (56, 'Gonzaguinha'),
     (57, 'Os Mutantes'),
     (58, 'Deep Purple'),
     (59, 'Santana'),
     (60, 'Santana Feat. Dave Matthews'),
     (61, 'Santana Feat. Everlast'),
     (62, 'Santana Feat. Rob Thomas'),
     (63, 'Santana Feat. Lauryn Hill & Cee-Lo'),
     (64, 'Santana Feat. The Project G&B'),
     (65, 'Santana Feat. Maná'),
     (66, 'Santana Feat. Eagle-Eye Cherry'),
     (67, 'Santana Feat. Eric Clapton'),
     (68, 'Miles Davis'),
     (69, 'Gene Krupa'),
     (70, 'Toquinho & Vinícius'),
     (71, 'Vinícius De Moraes & Baden Powell'),
     (72, 'Vinícius De Moraes'),
     (73, 'Vinícius E Qurteto Em Cy'),
     (74, 'Vinícius E Odette Lara'),
     (75, 'Vinicius, Toquinho & Quarteto Em Cy'),
     (76, 'Creedence Clearwater Revival'),
     (77, 'Cássia Eller'),
     (78, 'Def Leppard'),
     (79, 'Dennis Chambers'),
     (80, 'Djavan'),
     (81, 'Eric Clapton'),
     (82, 'Faith No More'),
     (83, 'Falamansa'),
     (84, 'Foo Fighters'),
     (85, 'Frank Sinatra'),
     (86, 'Funk Como Le Gusta'),
     (87, 'Godsmack'),
     (88, "Guns N' Roses"),
     (89, 'Incognito'),
     (90, 'Iron Maiden'),
     (91, 'James Brown'),
     (92, 'Jamiroquai'),
     (93, 'JET'),
     (94, 'Jimi Hendrix'),
     (95, 'Joe Satriani'),
     (96, 'Jota Quest'),
     (97, 'João Suplicy'),
     (98, 'Judas Priest'),
     (99, 'Legião Urbana'),
     (100, 'Lenny Kravitz'),
     (101, 'Lulu Santos'),
     (102, 'Marillion'),
     (103, 'Marisa Monte'),
     (104, 'Marvin Gaye'),
     (105, 'Men At Work'),
     (106, 'Motörhead'),
     (107, 'Motörhead & Girlschool'),
     (108, 'Mônica Marianno'),
     (109, 'Mötley Crüe'),
     (110, 'Nirvana'),
     (111, 'O Terço'),
     (112, 'Olodum'),
     (113, 'Os Paralamas Do Sucesso'),
     (114, 'Ozzy Osbourne'),
     (115, 'Page & Plant'),
     (116, 'Passengers'),
     (117, "Paul D'Ianno"),
     (118, 'Pearl Jam'),
     (119, 'Peter Tosh'),
     (120, 'Pink Floyd'),
     (121, 'Planet Hemp'),
     (122, 'R.E.M. Feat. Kate Pearson'),
     (123, 'R.E.M. Feat. KRS-One'),
     (124, 'R.E.M.'),
     (125, 'Raimundos'),
     (126, 'Raul Seixas'),
     (127, 'Red Hot Chili Peppers'),
     (128, 'Rush'),
     (129, 'Simply Red'),
     (130, 'Skank'),
     (131, 'Smashing Pumpkins'),
     (132, 'Soundgarden'),
     (133, 'Stevie Ray Vaughan & Double Trouble'),
     (134, 'Stone Temple Pilots'),
     (135, 'System Of A Down'),
     (136, 'Terry Bozzio, Tony Levin & Steve Stevens'),
     (137, 'The Black Crowes'),
     (138, 'The Clash'),
     (139, 'The Cult'),
     (140, 'The Doors'),
     (141, 'The Police'),
     (142, 'The Rolling Stones'),
     (143, 'The Tea Party'),
     (144, 'The Who'),
     (145, 'Tim Maia'),
     (146, 'Titãs'),
     (147, 'Battlestar Galactica'),
     (148, 'Heroes'),
     (149, 'Lost'),
     (150, 'U2'),
     (151, 'UB40'),
     (152, 'Van Halen'),
     (153, 'Velvet Revolver'),
     (154, 'Whitesnake'),
     (155, 'Zeca Pagodinho'),
     (156, 'The Office'),
     (157, 'Dread Zeppelin'),
     (158, 'Battlestar Galactica (Classic)'),
     (159, 'Aquaman'),
     (160, 'Christina Aguilera featuring BigElf'),
     (161, "Aerosmith & Sierra Leone's Refugee Allstars"),
     (162, 'Los Lonely Boys'),
     (163, 'Corinne Bailey Rae'),
     (164, 'Dhani Harrison & Jakob Dylan'),
     (165, 'Jackson Browne'),
     (166, 'Avril Lavigne'),
     (167, 'Big & Rich'),
     (168, "Youssou N'Dour"),
     (169, 'Black Eyed Peas'),
     (170, 'Jack Johnson'),
     (171, 'Ben Harper'),
     (172, 'Snow Patrol'),
     (173, 'Matisyahu'),
     (174, 'The Postal Service'),
     (175, 'Jaguares'),
     (176, 'The Flaming Lips'),
     (177, "Jack's Mannequin & Mick Fleetwood"),
     (178, 'Regina Spektor'),
     (179, 'Scorpions'),
     (180, 'House Of Pain'),
     (181, 'Xis'),
     (182, 'Nega Gizza'),
     (183, 'Gustavo & Andres Veiga & Salazar'),
     (184, 'Rodox'),
     (185, 'Charlie Brown Jr.'),
     (186, 'Pedro Luís E A Parede'),
     (187, 'Los Hermanos'),
     (188, 'Mundo Livre S/A'),
     (189, 'Otto'),
     (190, 'Instituto'),
     (191, 'Nação Zumbi'),
     (192, 'DJ Dolores & Orchestra Santa Massa'),
     (193, 'Seu Jorge'),
     (194, 'Sabotage E Instituto'),
     (195, 'Stereo Maracana'),
     (196, 'Cake'),
     (197, 'Aisha Duo'),
     (198, 'Habib Koité and Bamada'),
     (199, 'Karsh Kale'),
     (200, 'The Posies'),
     (201, 'Luciana Souza/Romero Lubambo'),
     (202, 'Aaron Goldberg'),
     (203, 'Nicolaus Esterhazy Sinfonia'),
     (204, 'Temple of the Dog'),
     (205, 'Chris Cornell'),
     (206, 'Alberto Turco & Nova Schola Gregoriana'),
     (207, 'Richard Marlow & The Choir of Trinity College, Cambridge'),
     (208, 'English Concert & Trevor Pinnock'),
     (209, 'Anne-Sophie Mutter, Herbert Von Karajan & Wiener Philharmoniker'),
     (210,
      'Hilary Hahn, Jeffrey Kahane, Los Angeles Chamber Orchestra & Margaret Batjer'),
     (211, 'Wilhelm Kempff'),
     (212, 'Yo-Yo Ma'),
     (213, 'Scholars Baroque Ensemble'),
     (214, 'Academy of St. Martin in the Fields & Sir Neville Marriner'),
     (215,
      'Academy of St. Martin in the Fields Chamber Ensemble & Sir Neville Marriner'),
     (216, 'Berliner Philharmoniker, Claudio Abbado & Sabine Meyer'),
     (217, 'Royal Philharmonic Orchestra & Sir Thomas Beecham'),
     (218, 'Orchestre Révolutionnaire et Romantique & John Eliot Gardiner'),
     (219, 'Britten Sinfonia, Ivor Bolton & Lesley Garrett'),
     (220,
      'Chicago Symphony Chorus, Chicago Symphony Orchestra & Sir Georg Solti'),
     (221, 'Sir Georg Solti & Wiener Philharmoniker'),
     (222,
      'Academy of St. Martin in the Fields, John Birch, Sir Neville Marriner & Sylvia McNair'),
     (223, 'London Symphony Orchestra & Sir Charles Mackerras'),
     (224, 'Barry Wordsworth & BBC Concert Orchestra'),
     (225, 'Herbert Von Karajan, Mirella Freni & Wiener Philharmoniker'),
     (226, 'Eugene Ormandy'),
     (227, 'Luciano Pavarotti'),
     (228, 'Leonard Bernstein & New York Philharmonic'),
     (229, 'Boston Symphony Orchestra & Seiji Ozawa'),
     (230, 'Aaron Copland & London Symphony Orchestra'),
     (231, 'Ton Koopman'),
     (232, 'Sergei Prokofiev & Yuri Temirkanov'),
     (233, 'Chicago Symphony Orchestra & Fritz Reiner'),
     (234, 'Orchestra of The Age of Enlightenment'),
     (235, 'Emanuel Ax, Eugene Ormandy & Philadelphia Orchestra'),
     (236, 'James Levine'),
     (237, 'Berliner Philharmoniker & Hans Rosbaud'),
     (238, 'Maurizio Pollini'),
     (239,
      'Academy of St. Martin in the Fields, Sir Neville Marriner & William Bennett'),
     (240, 'Gustav Mahler'),
     (241, 'Felix Schmidt, London Symphony Orchestra & Rafael Frühbeck de Burgos'),
     (242, 'Edo de Waart & San Francisco Symphony'),
     (243, 'Antal Doráti & London Symphony Orchestra'),
     (244, 'Choir Of Westminster Abbey & Simon Preston'),
     (245, 'Michael Tilson Thomas & San Francisco Symphony'),
     (246,
      'Chor der Wiener Staatsoper, Herbert Von Karajan & Wiener Philharmoniker'),
     (247, "The King's Singers"),
     (248, 'Berliner Philharmoniker & Herbert Von Karajan'),
     (249, 'Sir Georg Solti, Sumi Jo & Wiener Philharmoniker'),
     (250, "Christopher O'Riley"),
     (251, 'Fretwork'),
     (252, 'Amy Winehouse'),
     (253, 'Calexico'),
     (254, 'Otto Klemperer & Philharmonia Orchestra'),
     (255, 'Yehudi Menuhin'),
     (256, 'Philharmonia Orchestra & Sir Neville Marriner'),
     (257,
      'Academy of St. Martin in the Fields, Sir Neville Marriner & Thurston Dart'),
     (258, 'Les Arts Florissants & William Christie'),
     (259, 'The 12 Cellists of The Berlin Philharmonic'),
     (260, 'Adrian Leaper & Doreen de Feis'),
     (261, 'Roger Norrington, London Classical Players'),
     (262, "Charles Dutoit & L'Orchestre Symphonique de Montréal"),
     (263,
      'Equale Brass Ensemble, John Eliot Gardiner & Munich Monteverdi Orchestra and Choir'),
     (264, "Kent Nagano and Orchestre de l'Opéra de Lyon"),
     (265, 'Julian Bream'),
     (266, 'Martin Roscoe'),
     (267, 'Göteborgs Symfoniker & Neeme Järvi'),
     (268, 'Itzhak Perlman'),
     (269, 'Michele Campanella'),
     (270, 'Gerald Moore'),
     (271, 'Mela Tenenbaum, Pro Musica Prague & Richard Kapp'),
     (272, 'Emerson String Quartet'),
     (273,
      'C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett & Sackbu'),
     (274, 'Nash Ensemble'),
     (275, 'Philip Glass Ensemble'),
     (276, 'Bud Powell'),
     (277, None),
     (278, 'Jake1 Powell'),
     (279, None),
     (280, None),
     (281, None),
     (282, 'Jake1 Powell'),
     (283, None),
     (284, 'Buddy Rich'),
     (285, 'Candido'),
     (286, 'Charlie Byrd'),
     (287, 'Buddy Rich'),
     (288, 'Candido'),
     (289, 'Charlie Byrd'),
     (290, 'Night Byrd'),
     (291, 'Shin Lim'),
     (292, 'Maya'),
     (293, 'Jake Powell'),
     (294, None),
     (295, 'Buddy Rich'),
     (296, 'Candido'),
     (297, 'Charlie Byrd'),
     (298, 'Night Byrd'),
     (299, 'Shin Lim'),
     (300, 'Maya'),
     (301, 'Jake Powell'),
     (302, None),
     (303, 'Buddy Rich'),
     (304, 'Candido'),
     (305, 'Charlie Byrd'),
     (306, 'Night Byrd'),
     (307, 'Shin Lim'),
     (308, 'Maya'),
     (309, None),
     (310, 'Buddy Rich'),
     (311, 'Candido'),
     (312, 'Charlie Byrd'),
     (313, 'Night Byrd'),
     (314, 'Shin Lim'),
     (315, 'Maya'),
     (316, 'Jake Powell'),
     (317, None),
     (318, 'Buddy Rich'),
     (319, 'Candido'),
     (320, 'Charlie Byrd'),
     (321, 'Night Byrd'),
     (322, 'Shin Lim'),
     (323, 'Maya'),
     (324, 'Jake Powell'),
     (325, None),
     (326, 'Buddy Rich'),
     (327, 'Candido'),
     (328, 'Charlie Byrd'),
     (329, 'Night Byrd'),
     (330, 'Shin Lim'),
     (331, 'Maya'),
     (332, 'Jake Powell'),
     (333, None),
     (334, 'Buddy Rich'),
     (335, 'Candido'),
     (336, 'Charlie Byrd'),
     (337, 'Night Byrd'),
     (338, 'Shin Lim'),
     (339, 'Maya')]




```python
len(rows)
```




    339




```python
for row in rows:
    # since row[1] can be None, make sure you're check if it's a valid string
    if row[1] and 'Def' in row[1]:
        print(row)
        print(f'artist id:{row[0]} \t artist name: {row[1]}')
```

    (78, 'Def Leppard')
    artist id:78 	 artist name: Def Leppard


### Note
- filtering the results in DB is better than filtering the results in Python!
- why?


```python
sql = """
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY 
    Name;
"""
```


```python
rows = db.select_many_rows(db_file, sql, ())
```


```python
for row in rows:
    print(row)
```

    ('"40"', 'U2')
    ('"Eine Kleine Nachtmusik" Serenade In G, K. 525: I. Allegro', 'Wolfgang Amadeus Mozart')
    ('#1 Zero', 'Cornell, Commerford, Morello, Wilk')
    ("'Round Midnight", 'Miles Davis')
    ('(Anesthesia) Pulling Teeth', 'Cliff Burton')
    ('(Da Le) Yaleo', 'Santana')
    ('(Oh) Pretty Woman', 'Bill Dees/Roy Orbison')
    ('(There Is) No Greater Love (Teo Licks)', 'Isham Jones & Marty Symes')
    ('(We Are) The Road Crew', 'Clarke/Kilmister/Taylor')
    ('(White Man) In Hammersmith Palais', 'Joe Strummer/Mick Jones')
    ('(Wish I Could) Hideaway', 'J.C. Fogerty')
    ('...And Justice For All', 'James Hetfield, Lars Ulrich & Kirk Hammett')
    ('01 - Prowler', 'Steve Harris')
    ('02 - Sanctuary', "David Murray/Paul Di'Anno/Steve Harris")
    ('03 - Remember Tomorrow', 'Harris/Paul Di´Anno')
    ('04 - Running Free', 'Harris/Paul Di´Anno')
    ('05 - Phantom of the Opera', 'Steve Harris')
    ('06 - Transylvania', 'Steve Harris')
    ('07 - Strange World', 'Steve Harris')
    ('08 - Charlotte the Harlot', 'Murray  Dave')
    ('09 - Iron Maiden', 'Steve Harris')
    ('1/2 Full', 'Jeff Ament')
    ('14 Years', "Izzy Stradlin'/W. Axl Rose")
    ('1979', 'Billy Corgan')
    ('19th Nervous Breakdown', 'Jagger/Richards')
    ('1º De Julho', 'Renato Russo')
    ('2 A.M.', 'Blaze Bayley/Janick Gers/Steve Harris')
    ('2 Minutes To Midnight', 'Adrian Smith/Bruce Dickinson')
    ('2 Minutes To Midnight', 'Smith/Dickinson')
    ('2 Minutes To Midnight', 'Adrian Smith/Bruce Dickinson')
    ('2 Minutes To Midnight', 'Smith/Dickinson')
    ('2 Minutes To Midnight', 'Adrian Smith/Bruce Dickinson')
    ('2 X 4', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('2,000 Man', 'Mick Jagger, Keith Richard')
    ('20 Flight Rock', 'Ned Fairchild')
    ('200 Years Old', 'Frank Zappa')
    ('2112 Overture', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('22 Acacia Avenue', 'Adrian Smith/Steve Harris')
    ('24 Caprices, Op. 1, No. 24, for Solo Violin, in A Minor', 'Niccolò Paganini')
    ('3 Gymnopédies: No.1 - Lent Et Grave, No.3 - Lent Et Douloureux', 'Erik Satie')
    ('32 Dentes', 'Titãs')
    ('5.15', 'Pete Townshend')
    ('51st Anniversary', 'Jimi Hendrix')
    ('A Carta', 'Djavan - Gabriel, O Pensador')
    ('A Castle Full Of Rascals', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('A Cor Do Sol', 'Bernardo Vilhena/Da Gama/Lazão')
    ('A Cor Do Sol', 'Bernardo Vilhena/Da Gama/Lazao')
    ('A Different Kind Of Blue', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('A E O Z', 'Mutantes')
    ('A Estrada', 'Bino Farias/Da Gama/Lazão/Toni Garrido')
    ('A Estrada', 'Da Gama/Lazao/Toni Garrido')
    ('A Kind Of Magic', 'Roger Taylor')
    ('A Luz De Tieta', 'Caetano Veloso')
    ('A Man And A Woman', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('A Melhor Forma', 'Titãs')
    ('A Menina Dança', 'Caetano Veloso e Gilberto Gil')
    ('A Moça e a Chuva', 'Mônica Marianno')
    ('A New Flame', 'Mick Hucknall')
    ('A Noite Do Meu Bem', 'Dolores Duran')
    ('A Novidade', 'Gilberto Gil')
    ('A Paz', 'Donato/Gilberto Gil')
    ('A Paz', 'Gilberto Gil')
    ('A Room At The Heartbreak Hotel', 'U2')
    ('A Sombra Da Maldade', 'Da Gama/Toni Garrido')
    ('A Sombra Da Maldade', 'Da Gama/Toni Garrido')
    ('A Sua', 'Rodolfo')
    ('A Touch Away', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('A Twist In The Tail', 'roger glover')
    ('A Via Láctea', 'Renato Russo')
    ('A Volta Da Asa Branca', 'Luiz Gonzaga/Zé Dantas')
    ('A World Without Heroes', 'Paul Stanley, Gene Simmons, Bob Ezrin, Lewis Reed')
    ('A Última Guerra', 'Leão, Rodrigo F./Lô Borges/Samuel Rosa')
    ('Abraham, Martin And John', 'Dick Holler')
    ('Abrir A Porta', 'Vários')
    ('Absolute Zero', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Ace Of Spades', 'Clarke/Kilmister/Taylor')
    ('Acelerou', 'Djavan')
    ('Aces High', 'Harris')
    ('Achilles Last Stand', 'Jimmy Page/Robert Plant')
    ('Acrobat', 'U2')
    ('Act IV, Symphony', 'Henry Purcell')
    ('Adagio for Strings from the String Quartet, Op. 11', 'Samuel Barber')
    ('Adios nonino', 'Astor Piazzolla')
    ('Advance Romance', 'Frank Zappa')
    ('Aeroplane Flies High', 'Billy Corgan')
    ('Afraid', 'Nikki Sixx')
    ('Afraid To Shoot Strangers', 'Steve Harris')
    ('Afraid To Shoot Strangers', 'Steve Harris')
    ('Africa Bamba', 'I. Toure, S. Tidiane Toure, Carlos Santana & K. Perazzo')
    ('After Midnight', 'Clapton/J. J. Cale')
    ('Aftermath', 'The Tea Party')
    ('Again', 'Lenny Kravitz')
    ('Age Of Innocence', 'David Murray/Steve Harris')
    ("Ain't My Bitch", 'James Hetfield, Lars Ulrich')
    ("Ain't Talkin' 'Bout Love", 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ("Ain't Talkin' 'bout Love", 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ('Ainda Lembro', 'Caetano Veloso e Gilberto Gil')
    ('Ainda É Cedo', 'Dado Villa-Lobos/Ico Ouro-Preto/Marcelo Bonfá')
    ('Alabama Song', 'Weill-Brecht')
    ('Alarum', 'The Tea Party')
    ('Alberta', 'Traditional')
    ('Alexander the Great', 'Steve Harris')
    ('Ali', 'Nando Reis/Samuel Rosa')
    ('Alice', 'Vários')
    ('Alive', 'Stone Gossard')
    ('All Along The Watchtower', 'Dylan, Bob')
    ('All Because Of You', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('All Dead, All Dead', 'May')
    ('All I Really Want', 'Alanis Morissette & Glenn Ballard')
    ('All I Want Is You', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('All I Want Is You', 'U2 & Van Dyke Parks')
    ('All My Life', 'Foo Fighters')
    ('All My Love', 'Robert Plant & John Paul Jones')
    ('All My Love', 'E. Schrody/L. Dimant')
    ('All Star', 'Nando Reis')
    ('All Within My Hands', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('All or None', 'Stone Gossard')
    ('Aloha', 'Renato Russo')
    ('Always Forever Now', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Always On The Run', 'Lenny Kravitz/Slash')
    ('Alô Alô Marciano', 'Vários')
    ('Am I Evil?', 'Harris/Tatler')
    ('Amanda', 'Luca Gusella')
    ('Amanhã Não Se Sabe', 'Sérgio Britto')
    ('Amar É Tudo', 'Djavan')
    ('Amazing', 'Steven Tyler, Richie Supa')
    ('American Gothic', 'Billy Duffy/Ian Astbury')
    ('American Idiot', 'Billie Joe Armstrong, Mike Dirnt, Tré Cool')
    ('American Woman', 'B. Cummings/G. Peterson/M.J. Kale/R. Bachman')
    ('Amor De Muito', 'Chico Science')
    ('Amy Amy Amy (Outro)', 'Astor Campbell, Delroy "Chris" Cooper, Donovan Jackson, Dorothy Fields, Earl Chinna Smith, Felix Howard, Gordon Williams, James Moody, Jimmy McHugh, Matt Rowe, Salaam Remi & Stefan Skarbek')
    ('And the Cradle Will Rock...', 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ('Ando Meio Desligado', 'Caetano Veloso')
    ('Ando Meio Desligado', 'Arnaldo Baptista - Rita Lee -  Sérgio Dias')
    ('Aneurysm', 'Nirvana')
    ('Angel', 'Steven Tyler, Desmond Child')
    ('Angel', 'Carolyn Franklin and Sonny Saunders')
    ('Angel Of Harlem', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Angel Of Harlem', 'U2')
    ('Animal', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Another Life', 'Steve Harris')
    ('Another One Bites The Dust', 'Deacon, John')
    ('Another Round', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Antes Das Seis', 'Dado Villa-Lobos')
    ('Anthem', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Any Colour You Like', 'Gilmour, Mason, Wright, Waters')
    ('Anya', 'jon lord/roger glover')
    ("Anyone's Daughter", 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('Anyway, Anyhow, Anywhere', 'Pete Townshend, Roger Daltrey')
    ('Ao Meu Redor', 'Caetano Veloso e Gilberto Gil')
    ('Aonde Quer Que Eu Va', 'Herbert Vianna/Paulo Sérgio Valle')
    ('Aos Leões', 'Mônica Marianno')
    ('Apache Rose Peacock', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Aquele Abraço', 'Gilberto Gil')
    ('Arc', 'Pearl Jam')
    ('Are We The Waiting', 'Green Day')
    ('Are You Experienced?', 'Jimi Hendrix')
    ('Are You Gonna Be My Girl', 'C. Muncey/N. Cester')
    ('Are You Gonna Go My Way', 'Craig Ross/Lenny Kravitz')
    ('Aria Mit 30 Veränderungen, BWV 988 "Goldberg Variations": Aria', 'Johann Sebastian Bach')
    ('Arms Around Your Love', 'Chris Cornell')
    ('Army Ants', 'The Tea Party')
    ('Army Reserve', 'Jeff Ament')
    ('Around The World', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Arrepio', 'Carlinhos Brown')
    ('As Dores do Mundo', 'Hyldon')
    ('As Pegadas Do Amor', 'Gilberto Gil')
    ('As Tears Go By', 'Jagger/Richards/Oldham')
    ('As The Years Go by', 'Albert King')
    ('Asa Branca', 'Humberto Teixeira/Luiz Gonzaga')
    ('Ashes And Ghosts', 'Billy Duffy/Bob Rock/Ian Astbury')
    ('Ashes To Ashes', 'Bill Gould/Jon Hudson/Mike Bordin/Mike Patton/Roddy Bottum')
    ('Assum Preto', 'Humberto Teixeira/Luiz Gonzaga')
    ('Astronomy', 'A.Bouchard/J.Bouchard/S.Pearlman')
    ('Atomic Punk', 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('Atrás Da Verd-E-Rosa Só Não Vai Quem Já Morreu', 'David Corrêa - Paulinho Carvalho - Carlos Sena - Bira do Ponto')
    ('Attitude', 'Hetfield, Ulrich')
    ('Até Que Enfim Encontrei Você', 'Tim Maia')
    ('Ava Adore', 'Billy Corgan')
    ('Ave Maria', 'Franz Schubert')
    ('Azul', 'Djavan')
    ('Azul Da Cor Do Mar', 'Tim Maia')
    ('Açai', 'Djavan')
    ('B.Y.O.B.', 'Tankian, Serj')
    ("Baba O'Riley", 'John Entwistle/Pete Townshend')
    ("Babe I'm Gonna Leave You", 'Jimmy Page/Robert Plant')
    ('Baby', 'Caetano Veloso')
    ('Baby Break It Down', 'Jagger/Richards')
    ('Babyface', 'U2; Bono')
    ('Babylon', 'The Tea Party')
    ('Babylon', 'The Tea Party')
    ('Back Door Man', 'Willie Dixon, C. Burnett')
    ('Back in the Village', 'Dickinson/Smith')
    ('Back to Black', 'Mark Ronson')
    ('Bad', 'U2')
    ('Bad Attitude', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord')
    ('Bad Boy', 'Larry Williams')
    ('Bad Boy Boogie', 'AC/DC')
    ('Bad Moon Rising', 'J. C. Fogerty')
    ('Bad Seed', 'Hetfield, Ulrich, Hammett')
    ('Bad, Bad Leroy Brown', 'jim croce')
    ('Badge', 'Clapton/Harrison')
    ('Baião Ambiental [Instrumental]', 'Chico Science')
    ('Balada Da Paula', 'Emerson Villani')
    ('Balada Do Amor Inabalável', 'Fausto Fawcett/Samuel Rosa')
    ('Balada Do Louco', 'Arnaldo Baptista - Rita Lee')
    ('Ballot or the Bullet', 'Van Halen')
    ('Baltimore, DC', 'John Scofield')
    ('Banho De Lua', 'B. de Filippi - F. Migliaci - Versão: Fred Jorge')
    ('Bankrobber', 'Joe Strummer/Mick Jones')
    ('Bark at the Moon', 'O. Osbourne')
    ('Basket Case', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Bass Trap', 'U2')
    ('Bastille Day', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Bat Macumba', 'Gilberto Gil - Caetano Veloso')
    ('Bate Lata', 'Fábio Nolasco/Gal Sales/Ivan Brasil')
    ('Battery', 'J.Hetfield/L.Ulrich')
    ('Be Mine', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Be Quick Or Be Dead', 'Bruce Dickinson/Janick Gers')
    ('Be Quick Or Be Dead', 'Bruce Dickinson/Janick Gers')
    ('Be Yourself', 'Cornell, Commerford, Morello, Wilk')
    ('Beach Sequence', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Beautiful Day', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Because You Are', 'Billy Corgan')
    ('Been A Son', 'Kurt Cobain')
    ('Before You Accuse Me', 'J.C. Fogerty')
    ('Before You Accuse Me', 'Eugene McDaniel')
    ('Beija Eu', 'Caetano Veloso e Gilberto Gil')
    ('Beija-Flor', 'Caruso/Cleber/Deo/Osmar')
    ('Beijo Partido', 'Toninho Horta')
    ('Beijo do Olhar', 'Mônica Marianno')
    ('Beira Mar', 'Gilberto Gil')
    ('Believe', 'Henry Hirsch/Lenny Kravitz')
    ('Believe', 'James Iha')
    ('Believer', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Bell Bottom Blues', 'Clapton')
    ('Belong', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Bem Devagar', 'Gilberto Gil')
    ('Bem Leve', 'Caetano Veloso e Gilberto Gil')
    ('Berlim', 'Da Gama/Toni Garrido')
    ('Best Of You', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('Beth', 'S. Penridge, Bob Ezrin, Peter Criss')
    ('Beth', 'Peter Criss, Stan Penridge, Bob Ezrin')
    ('Better Man', 'Eddie Vedder')
    ('Better Than You', 'Hetfield, Ulrich')
    ('Bichos Escrotos (Vinheta)', 'Titãs')
    ('Bicycle Race', 'Mercury, Freddie')
    ('Big Bad Bill (Is Sweet William Now)', 'Jack Yellen/Milton Ager')
    ('Big Machine', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Big Wave', 'Jeff Ament')
    ('Billie Jean', 'Michael Jackson')
    ('Binky The Doormat', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Bite The Bullet', 'Clarke/Kilmister/Taylor')
    ('Bitter Pill', 'Mick Mars/Nikki Sixx/Tommy Lee/Vince Neil')
    ('Bitter Suite: Brief Encounter / Lost Weekend / Blue Angel', 'Kelly, Mosley, Rothery, Trewaves')
    ('Bittersweet Me', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Black', 'Stone Gossard & Eddie Vedder')
    ('Black', 'Dave Krusen/Stone Gossard')
    ('Black Capricorn Day', 'Jay Kay')
    ('Black Country Woman', 'Robert Plant')
    ('Black Diamond', 'Paul Stanley')
    ('Black Dog', 'John Paul Jones/Robert Plant')
    ('Black Dog', 'Jimmy Page, Robert Plant, John Paul Jones')
    ('Black Hole Sun', 'Soundgarden')
    ('Black Light Syndrome', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Black Moon Creeping', 'Chris Robinson/Rich Robinson')
    ('Black Mountain Side', 'Jimmy Page')
    ('Black Night', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord, Ian Paice')
    ('Black Satin', 'Miles Davis')
    ('Black Velveteen', 'Lenny Kravitz')
    ('Blackened', 'James Hetfield, Lars Ulrich & Jason Newsted')
    ('Blanco', 'Marisa Monte/poema de Octavio Paz/versão: Haroldo de Campos')
    ('Bleed The Freak', 'Jerry Cantrell')
    ('Bleed Together', 'Chris Cornell')
    ('Bleeding Me', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('Blew', 'Kurt Cobain')
    ('Blind Curve: Vocal Under A Bloodlight / Passing Strangers / Mylo / Perimeter Walk / Threshold', 'Kelly, Mosley, Rothery, Trewaves')
    ('Blind Man', 'Steven Tyler, Joe Perry, Taylor Rhodes')
    ('Blinded By Rainbows', 'Jagger/Richards')
    ('Blissed & Gone', 'Billy Corgan')
    ('Blitzkrieg', 'Jones/Sirotto/Smith')
    ('Blood', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Blood Brothers', 'Steve Harris')
    ('Blood Brothers', 'Steve Harris')
    ("Blood On The World's Hands", 'Steve Harris')
    ('Blood Sugar Sex Magik', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Bloodsucker', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Blow Up The Outside World', 'Chris Cornell')
    ('Blow Your Mind', 'Smith, Toby')
    ('Blue Train', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Blues For Pablo', 'Gil Evans')
    ('Blues For Pablo (Alternate Take)', 'Gil Evans')
    ('Bodies', 'Rodolfo')
    ('Bohemian Rhapsody', 'Mercury, Freddie')
    ("Bonzo's Montreux", 'John Bonham')
    ('Boogie With Stu', 'Ian Stewart/John Bonham/John Paul Jones/Mrs. Valens/Robert Plant')
    ('Book Of Thel', 'Eddie Casillas/Roy Z')
    ('Book of Hours', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Bora-Bora', 'Herbert Vianna')
    ('Boris The Spider', 'John Entwistle')
    ('Born On The Bayou', 'J.C. Fogerty')
    ('Born To Move', 'J.C. Fogerty')
    ('Borogodo', 'João Suplicy')
    ('Boulevard Of Broken Dreams', 'Mike Dint, Billie Joe, Tré Cool')
    ('Brain Damage', 'Waters')
    ('Brain Stew', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Brand New Car', 'Jagger/Richards')
    ('Brasil', 'Milton Nascimento, Fernando Brant')
    ('Brasília 5:31', 'Herbert Vianna')
    ('Brave New World', 'Bruce Dickinson/David Murray/Steve Harris')
    ('Brave New World', 'Bruce Dickinson/David Murray/Steve Harris')
    ('Breadfan', 'Bourge/Phillips/Shelley')
    ('Break on Through', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('Breakdown', 'W. Axl Rose')
    ('Breakfast In Bed', 'Blackmore, Glover, Turner')
    ('Breaking The Girl', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Breaking The Rules', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Breakthru', 'Queen')
    ('Breathe', 'Billy Duffy/Ian Astbury/Marti Frederiksen/Mick Jones')
    ('Breed', 'Kurt Cobain')
    ('Breed', 'Kurt Cobain')
    ('Bring It On Home', 'Jimmy Page, Robert Plant')
    ('Bring Your Daughter... ...To The Slaughter', 'Bruce Dickinson')
    ('Bring Your Daughter... To The Slaughter', 'Bruce Dickinson')
    ("Bring'em Back Alive", 'Audioslave/Chris Cornell')
    ('Bron-Y-Aur Stomp', 'Jimmy Page, Robert Plant, John Paul Jones')
    ('Bron-Yr-Aur', 'Jimmy Page')
    ('Bullet The Blue Sky', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Bullet With Butterfly Wings', 'Billy Corgan')
    ('Bumbo Da Mangueira', 'Vários')
    ('Burden In My Hand', 'Chris Cornell')
    ('Burn', 'Coverdale/Lord/Paice')
    ('Burn Away', 'Foo Fighters')
    ('Burning Up', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Busca Vida', 'Herbert Vianna')
    ('Bushleager', 'Stone Gossard')
    ('Butterfly', 'Jay Kay/Toby Smith')
    ('By The Way', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('By-Tor And The Snow Dog', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Bye Bye Blackbird', 'Miles Davis')
    ('Bê-a-Bá', 'Rodolfo')
    ("C'Mon Everybody", 'Eddie Cochran/Jerry Capehart')
    ('C.O.D.', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Cabeça Dinossauro', 'Titãs')
    ('Cabron', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Cafezinho', 'João Suplicy')
    ('Cajueiro', 'Rodolfo')
    ('Caleidoscópio', 'Herbert Vianna')
    ('Californication', 'Red Hot Chili Peppers')
    ('Call Of The Wild', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord')
    ('Calling Dr. Love', 'Gene Simmons')
    ('Camarão que Dorme e Onda Leva', 'Acyi Marques/Arlindo Bruz/Braço, Beto Sem/Zeca Pagodinho')
    ('Can I Play With Madness', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('Can I Play With Madness', 'Adrian Smith; Bruce Dickinson; Steve Harris')
    ('Can You See Me', 'Jimi Hendrix')
    ("Can't Get There From Here", 'R.E.M.')
    ("Can't Get This Stuff No More", 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, David Lee Roth')
    ("Can't Get You Off My Mind", 'Lenny Kravitz')
    ("Can't Keep", 'Eddie Vedder')
    ("Can't Stand Losing You", 'G M Sumner')
    ("Can't Stop", 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ("Can't Stop Loving You", 'Van Halen')
    ('Candy Store Rock', 'Jimmy Page/Robert Plant')
    ('Canned Heat', 'Jay Kay')
    ('Canon and Gigue in D Major: I. Canon', 'Johann Pachelbel')
    ('Canção Do Novo Mundo', 'Beto Guedes, Ronaldo Bastos')
    ('Canção Noturna', 'Chico Amaral/Lelo Zanettik')
    ('Caprichosos', 'Gule/Jorge 101/Lequinho/Luiz Piao')
    ('Caralho Voador', 'Mike Bordin, Billy Gould, Mike Patton, Trey Spruance')
    ('Caras Como Eu', 'Toni Bellotto')
    ('Carmen: Overture', 'Georges Bizet')
    ('Carmina Burana: O Fortuna', 'Carl Orff')
    ('Carnival Of Sorts', 'R.E.M.')
    ('Carol', 'Chuck Berry')
    ('Carolina', 'Chico Buarque')
    ('Carolina Hard-Core Ecstasy', 'Frank Zappa')
    ('Carouselambra', 'John Paul Jones, Jimmy Page & Robert Plant')
    ('Carpe Diem Baby', 'Hetfield, Ulrich, Hammett')
    ("Cascades : I'm Not Your Lover", 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Casinha Feliz', 'Gilberto Gil')
    ('Caso Você Queira Saber', 'Beto Guedes, Márcio Borges')
    ('Cathedral', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Caught Somewhere in Time', 'Steve Harris')
    ('Cavalleria Rusticana \\ Act \\ Intermezzo Sinfonico', 'Pietro Mascagni')
    ('Caxangá', 'Milton Nascimento, Fernando Brant')
    ('Celebration Day', 'Jimmy Page, Robert Plant, John Paul Jones')
    ('Celebration Day', 'John Paul Jones/Robert Plant')
    ('Chains Of Misery', 'Bruce Dickinson/David Murray')
    ('Changes', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Changes', 'Sully Erna; Tony Rombola')
    ('Chaos-Control', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Chemical Wedding', 'Roy Z')
    ('Cherub Rock', 'Billy Corgan')
    ('Chico Não Vai na Corimba', 'Dudu Nobre/Zeca Pagodinho')
    ('Child In Time', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Child In Time (Son Of Aleric - Instrumental)', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord, Ian Paice')
    ("Childhood's End", 'Steve Harris')
    ('Childhoods End?', 'Kelly, Mosley, Rothery, Trewaves')
    ('Children Of The Damned', 'Steve Harris')
    ('Children Of The Grave', 'A. F. Iommi, W. Ward, T. Butler, J. Osbourne')
    ('Children of the Damned', 'Steve Harris')
    ('Chocolate', 'Tim Maia')
    ('Choramingando', 'João Suplicy')
    ('Chuva No Brejo', 'Morais')
    ('Chão De Estrelas', 'Orestes Barbosa-Sílvio Caldas')
    ('Cigaro', 'Tankian, Serj')
    ('City Of Blinding Lights', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Civil War', 'Duff McKagan/Slash/W. Axl Rose')
    ('Clash City Rockers', 'Joe Strummer/Mick Jones')
    ('Closer To The Heart', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Cocaine', 'Cale/Clapton')
    ('Cochise', 'Audioslave/Chris Cornell')
    ('Cold Day In The Sun', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Cold Gin', 'Ace Frehley')
    ('Cold Hard Bitch', 'C. Cester/C. Muncey/N. Cester')
    ('Cold Sweat', 'Alfred Ellis/James Brown')
    ('Colibri', 'Richard Bull')
    ('Collision', 'Jon Hudson/Mike Patton')
    ('Com A Perna No Mundo', 'Gonzaga Jr.')
    ('Comatose', 'Mike McCready & Stone Gossard')
    ('Come And Get Some Of This', 'E. Schrody/L. Muggerud/R. Medrano')
    ('Come Around Again', 'C. Muncey/N. Cester')
    ('Come As You Are', 'Kurt Cobain')
    ('Come Back', 'Foo Fighters')
    ('Come Back', 'Eddie Vedder & Mike McCready')
    ('Come Fly With Me', 'jimmy van heusen/sammy cahn')
    ('Comida', 'Titãs')
    ("Comin' Home", 'Bolin/Coverdale/Paice')
    ("Comin' Home", 'Paul Stanley, Ace Frehley')
    ('Commercial 1', 'L. Muggerud')
    ('Commercial 2', 'L. Muggerud')
    ('Commotion', 'J. C. Fogerty')
    ('Communication Breakdown', 'Jimmy Page/John Bonham/John Paul Jones')
    ('Communication Breakdown', 'Jimmy Page/John Bonham/John Paul Jones')
    ('Communication Breakdown(2)', 'Jimmy Page/John Bonham/John Paul Jones')
    ('Communication Breakdown(3)', 'Jimmy Page/John Bonham/John Paul Jones')
    ('Como Estais Amigos', 'Blaze Bayley/Janick Gers')
    ('Compadre', 'Tim Maia')
    ('Complete Control', 'Joe Strummer/Mick Jones')
    ('Comportamento Geral', 'Gonzaga Jr')
    ('Compulsion', 'Miles Davis')
    ('Concert pour 4 Parties de V**les, H. 545: I. Prelude', 'Marc-Antoine Charpentier')
    ('Concerto No. 1 in E Major, RV 269 "Spring": I. Allegro', 'Antonio Vivaldi')
    ('Concerto No.2 in F Major, BWV1047, I. Allegro', 'Johann Sebastian Bach')
    ('Concerto for 2 Violins in D Minor, BWV 1043: I. Vivace', 'Johann Sebastian Bach')
    ('Concerto for Cello and Orchestra in E minor, Op. 85: I. Adagio - Moderato', 'Edward Elgar')
    ('Concerto for Clarinet in A Major, K. 622: II. Adagio', 'Wolfgang Amadeus Mozart')
    ('Concerto for Piano No. 2 in F Minor, Op. 21: II. Larghetto', 'Frédéric Chopin')
    ('Concerto for Violin, Strings and Continuo in G Major, Op. 3, No. 9: I. Allegro', 'Pietro Antonio Locatelli')
    ('Conciliação', 'Da Gama/Lazão/Rás Bernardo')
    ('Confusion', 'Jerry Cantrell, Michael Starr, Layne Staley')
    ('Corazon Espinado', 'F. Olivera')
    ('Coração De Estudante', 'Wagner Tiso, Milton Nascimento')
    ('Coração Em Desalinho', 'Mauro Diniz/Ratino Sigem')
    ('Corduroy', 'Pearl Jam & Eddie Vedder')
    ('Corinna', 'Jesse Ed Davis III/Taj Mahal')
    ('Cornucopia', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Coroné Antonio Bento', 'Do Vale, João/Luiz Wanderley')
    ('Corpo De Lama', 'Chico Science')
    ('Corpse (These Chains Are Way Too Long)', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Cosmic Fiend', 'Chris Robinson/Rich Robinson')
    ('Cotton Fields', 'J.C. Fogerty')
    ('Country Feedback', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Crackerman', 'Kretz/R. DeLeo/Weiland')
    ('Crash Course In Brain Surgery', 'Bourge/Phillips/Shelley')
    ('Crazy', 'Steven Tyler, Joe Perry, Desmond Child')
    ('Crazy Little Thing Called Love', 'Mercury, Freddie')
    ('Crazy Train', 'B. Daisley, O. Osbourne & R. Rhoads')
    ('Crazy Train', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Creep', 'R. DeLeo/Weiland')
    ('Creeping Death', 'Apocalyptica')
    ('Creeping Death', 'Metallica')
    ('Criança De Domingo', 'Chico Science')
    ('Cristina Nº 2', 'Carlos Imperial/Tim Maia')
    ('Cropduster', 'Matt Cameron')
    ('Crossfire', 'B. Carter/C. Layton/R. Ellsworth/R. Wynans/T. Shannon')
    ('Crossroads', 'Clapton/Robert Johnson Arr: Eric Clapton')
    ('Crumbs From Your Table', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Cry For Love', 'Bossi/David Coverdale/Earl Slick')
    ("Cryin'", 'Steven Tyler, Joe Perry, Taylor Rhodes')
    ('Crying In The Rain', 'Coverdale')
    ('Cuando A Noite Vai Chegando', 'João Suplicy')
    ('Cuando Eu For Pro Ceu', 'João Suplicy')
    ('Cucamonga', 'Frank Zappa')
    ('Cuckoo For Caca', 'Mike Bordin, Billy Gould, Mike Patton, Trey Spruance')
    ('Cuitelinho', 'Folclore')
    ('Cure', 'James Hetfield, Lars Ulrich')
    ('Cursed Diamonds', 'Chris Robinson/Rich Robinson')
    ('Custard Pie', 'Jimmy Page/Robert Plant')
    ('Cuyahoga', 'R.E.M.')
    ('Cérebro Eletrônico', 'Gilberto Gil')
    ("D'Yer Mak'er", 'John Bonham/John Paul Jones')
    ('DOA', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ("Daddy's Gonna Pay For Your Crashed Car", 'U2; Bono')
    ('Damage Case', 'Clarke/Farren/Kilmister/Tayler')
    ('Damage Inc.', 'K.Hammett')
    ('Dance', 'Clarke/Kilmister/Taylor')
    ('Dance Of Death', 'Janick Gers/Steve Harris')
    ('Dance the Night Away', 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ('Dancing Barefoot', 'Ivan Kral/Patti Smith')
    ('Dancing Days', 'Jimmy Page/Jimmy Page & Robert Plant/Robert Plant')
    ('Dancing In The Street', 'Ivy Jo Hunter/Marvin Gaye/William Stevenson')
    ('Dandelion', 'Cornell, Commerford, Morello, Wilk')
    ('Daniela', 'Jorge Cardoso/Pierre Onasis')
    ('Danny Boy, Danny Boy', 'E. Schrody/L. Muggerud')
    ('Dança Da Solidão', 'Caetano Veloso e Gilberto Gil')
    ('Dark Corners', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Dark Side Of The Cog', 'Jean Paul Maunick')
    ('Darlene', 'Jimmy Page, Robert Plant, John Bonham, John Paul Jones')
    ('Das Lied Von Der Erde, Von Der Jugend', 'Gustav Mahler')
    ('Daughter', 'Dave Abbruzzese & Jeff Ament & Stone Gossard & Mike McCready & Eddie Vedder')
    ('Daughter', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Dazed And Confused', 'Jimmy Page/Led Zeppelin')
    ('Dazed And Confused', 'Jimmy Page')
    ('Dazed and Confused', 'Jimmy Page')
    ('Dazed and Confused', 'Jimmy Page')
    ('De Do Do Do, De Da Da Da', 'G M Sumner')
    ('De Ja Vu', 'David Murray/Steve Harris')
    ('De Noite Na Cama', 'Caetano Veloso e Gilberto Gil')
    ('Dead And Bloated', 'R. DeLeo/Weiland')
    ('Dead And Broken', 'Sully Erna')
    ('Dealer', 'Bolin/Coverdale')
    ('Debra Kadabra', 'Frank Zappa')
    ('Dee', 'R. Rhoads')
    ('Deep', 'Jeff Ament/Stone Gossard')
    ('Deep Waters', 'Richard Bull')
    ('Deeper Underground', 'Toby Smith')
    ('Demorou!', 'Mônica Marianno')
    ('Departure', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Desculpe Babe', 'Arnaldo Baptista - Rita Lee')
    ('Desire', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Desire', 'U2')
    ('Desordem', 'Charles Gavin/Marcelo Fromer/Sérgio Britto')
    ('Despertar', 'Andrea Dulbecco')
    ('Destitute Illusions', 'Derrick McKenzie/Jay Kay/Toby Smith')
    ('Detroit Rock City', 'Paul Stanley, B. Ezrin')
    ('Deuce', 'Gene Simmons')
    ('Deuces Are Wild', 'Steven Tyler, Jim Vallance')
    ("Devil's Dance", 'Hetfield, Ulrich')
    ('Dezesseis', 'Renato Russo')
    ('Dezesseis', 'Dado Villa-Lobos/Marcelo Bonfá')
    ("Didgin' Out", 'Buchanan, Wallis')
    ('Die Die My Darling', 'Danzig')
    ('Die Walküre: The Ride of the Valkyries', 'Richard Wagner')
    ('Die With Your Boots On', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('Die With Your Boots On', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('Die Zauberflöte, K.620: "Der Hölle Rache Kocht in Meinem Herze"', 'Wolfgang Amadeus Mozart')
    ('Dig-Dig, Lambe-Lambe (Ao Vivo)', 'Cassiano Costa/Cintia Maviane/J.F./Lucas Costa')
    ('Digging The Grave', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Din Din Wo (Little Child)', 'Habib Koité')
    ('Dirty Day', 'U2; Bono & Edge, The')
    ('Dirty Little Thing', 'Dave Kushner, Duff, Keith Nelson, Matt Sorum, Scott Weiland & Slash')
    ('Dirty Love', 'Clarke/Kilmister/Taylor')
    ('Dirty Water Dog', 'Van Halen')
    ('Dirty Window', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Disappearing Act', 'Chris Cornell')
    ('Disarm', 'Billy Corgan')
    ('Discotheque', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Disenchanted Lullaby', 'Foo Fighters')
    ('Disposable Heroes', 'J.Hetfield/L.Ulrich')
    ('Dissident', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Distance', 'Karsh Kale/Vishal Vaid')
    ('Diversão', 'Titãs')
    ('Do It For The Kids', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Do Nosso Amor', 'João Suplicy')
    ('Do The Evolution', 'Eddie Vedder & Stone Gossard')
    ('Do You Feel Loved', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Do You Like The Way', 'L. Hill')
    ('Do You Love Me', 'Paul Stanley, B. Ezrin, K. Fowley')
    ('Do You Love Me', 'Paul Stanley, Bob Ezrin, Kim Fowley')
    ('Do what cha wanna', 'George Duke')
    ("Doesn't Remind Me", 'Cornell, Commerford, Morello, Wilk')
    ('Dog Eat Dog', 'AC/DC')
    ('Dois Índios', 'Mônica Marianno')
    ('Doll', 'Dave, Taylor, Nate, Chris')
    ('Domingo', 'Sérgio Britto/Toni Bellotto')
    ('Domino', 'Gene Simmons')
    ("Don't Cry", "Izzy Stradlin'/W. Axl Rose")
    ("Don't Forget Me", 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ("Don't Go Away Mad (Just Go Away)", 'Mick Mars/Nikki Sixx')
    ("Don't Go Back To Rockville", 'R.E.M.')
    ("Don't Lie To Me", 'David Coverdale/Earl Slick')
    ("Don't Look Now", 'J.C. Fogerty')
    ("Don't Look To The Eyes Of A Stranger", 'Steve Harris')
    ("Don't Stand So Close to Me '86", 'G M Sumner')
    ("Don't Stand so Close to Me", 'G M Sumner')
    ("Don't Stop Me Now", 'Mercury, Freddie')
    ("Don't Tread On Me", 'Ulrich')
    ("Don't You Cry", 'David Coverdale')
    ('Dosed', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Doutor', 'Bino/Da Gama/Toni Garrido')
    ('Down By The Seaside', 'Robert Plant')
    ('Down On The Corner', 'J. C. Fogerty')
    ('Downtown', 'Cidade Negra')
    ('Dr. Feelgood', 'Mick Mars/Nikki Sixx')
    ('Drain You', 'Kurt Cobain')
    ('Drain You', 'Kurt Cobain')
    ('Dream Of Mirrors', 'Janick Gers/Steve Harris')
    ('Dream Of Mirrors', 'Janick Gers/Steve Harris')
    ('Dreams', 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, Sammy Hagar')
    ('Drifter', 'Bolin/Coverdale')
    ('Drifter', 'Steve Harris')
    ('Driver 8', 'R.E.M.')
    ('Drown', 'Billy Corgan')
    ('Drown Me Slowly', 'Cornell, Commerford, Morello, Wilk')
    ('Drowning Man', 'U2')
    ('Drão', 'Gilberto Gil')
    ('Drão', 'Gilberto Gil')
    ('Dude (Looks Like A Lady)', 'Steven Tyler, Joe Perry, Desmond Child')
    ('Duelists', 'Steve Harris')
    ('Duende', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Dyers Eve', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('E-Bow The Letter', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('E.S.P.', 'Miles Davis')
    ('Easily', 'Red Hot Chili Peppers')
    ('Eat The Rich', 'Steven Tyler, Joe Perry, Jim Vallance')
    ('Echo', 'J. Satriani')
    ('Eclipse', 'Waters')
    ('Eclipse Oculto', 'Caetano Veloso')
    ('Edge Of The World', 'Faith No More')
    ('Eduardo E Mônica', 'Renato Russo')
    ('Ego Tripping Out', 'Marvin Gaye')
    ('El Corazon Manda', 'E.Weiss')
    ('El Farol', 'Carlos Santana & KC Porter')
    ('Ela Desapareceu', 'Chico Amaral/Samuel Rosa')
    ('Ela Disse Adeus', 'Herbert Vianna')
    ('Elderly Woman Behind The Counter In A Small Town', 'Dave Abbruzzese & Jeff Ament & Stone Gossard & Mike McCready & Eddie Vedder')
    ('Elderly Woman Behind The Counter In A Small Town', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Electrolite', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Elevation', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Elvis Ate America', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Emerald', 'The Tea Party')
    ('Emergency', 'Dufort/Johnson/McAuliffe/Williams')
    ('Emergency On Planet Earth', 'Smith, Toby')
    ('Emit Remmus', 'Red Hot Chili Peppers')
    ('Encontrar Alguém', 'Marco Tulio Lara/Rogerio Flausino')
    ('End Of Romanticism', 'Rick Strauss')
    ('End Of The Night', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('End Over End', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('Endgame', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Endless Deep', 'U2')
    ('English Civil War', 'Mick Jones/Traditional arr. Joe Strummer')
    ('Enough Space', 'Dave Grohl')
    ('Enquanto O Dia Não Vem', 'João Suplicy')
    ('Enquanto O Mundo Explode', 'Chico Science')
    ('Enslaved', 'Mick Mars/Nikki Sixx/Tommy Lee')
    ('Enter Sandman', 'Apocalyptica')
    ('Enter Sandman', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('Epic', 'Faith No More')
    ('Equinocio', 'João Suplicy')
    ('Era Uma Vez', 'Arnaldo Anutnes/Branco Mello/Marcelo Fromer/Sergio Brotto/Toni Bellotto')
    ('Eruption', 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ('Eruption', 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('Escape', 'Metallica')
    ('Esotérico', 'Gilberto Gil')
    ('Esperando Na Janela', 'Manuca/Raimundinho DoAcordion/Targino Godim')
    ('Esperando Por Mim', 'Renato Russo')
    ('Espere Por Mim, Morena', 'Gonzaguinha')
    ('Esporrei Na Manivela', 'Rodolfo')
    ('Esse Cara', 'Caetano Veloso')
    ('Estranged', 'W. Axl Rose')
    ('Etnia', 'Chico Science')
    ('Eu Disse A Ela', 'Samuel Rosa')
    ('Eu E Ela', 'Nando Reis')
    ('Eu Também Quero Beijar', 'Fausto Nilo/Moraes Moreira/Pepeu Gomes')
    ('Eu Vim Da Bahia - Live', 'Vários')
    ('Even Better Than The Real Thing', 'U2')
    ('Even Flow', 'Stone Gossard & Eddie Vedder')
    ('Evenflow', 'Stone Gossard')
    ('Everlasting Love', 'Buzz Cason/Mac Gayden')
    ('Everlong', 'Dave Grohl')
    ('Every Breath You Take', 'G M Sumner')
    ('Every Little Thing She Does is Magic', 'G M Sumner')
    ('Every Time I Look At You', 'Paul Stanley, Vincent Cusano')
    ('Evidence', 'Mike Bordin, Billy Gould, Mike Patton, Trey Spruance')
    ('Evil Walks', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Exploder', 'Audioslave/Chris Cornell')
    ('Expresso 2222', 'Gilberto Gil')
    ('Extra', 'Gilberto Gil')
    ('Extraordinary Girl', 'Green Day')
    ('Eye', 'Billy Corgan')
    ('Eye Of The Beholder', 'James Hetfield, Lars Ulrich & Kirk Hammett')
    ('F**k Me Pumps', 'Salaam Remi')
    ("F*Ckin' Up", 'Neil Young')
    ('FX', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Face In The Sand', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('Faceless', 'Sully Erna')
    ('Fade To Black', 'Metallica')
    ('Failling', 'Jay Kay/Toby Smith')
    ('Fairground', 'Mick Hucknall')
    ('Faixa Amarela', 'Beto Gogo/Jessé Pai/Luiz Carlos/Zeca Pagodinho')
    ('Falar A Verdade', 'Bino/Da Gama/Ras Bernardo')
    ('Fall On Me', 'R.E.M.')
    ('Fall To Pieces', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Falling To Pieces', 'Faith No More')
    ('Falling in Circles', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('Família', 'Titãs')
    ('Fanfare for the Common Man', 'Aaron Copland')
    ('Fantasia On Greensleeves', 'Ralph Vaughan Williams')
    ('Faroeste Caboclo', 'Renato Russo')
    ('Fast And Loose', 'Clarke/Kilmister/Taylor')
    ('Fast As a Shark', 'F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman')
    ('Fat Bottomed Girls', 'May, Brian')
    ('Fates Warning', 'David Murray/Steve Harris')
    ('Fear Is The Key', 'Bruce Dickinson/Janick Gers')
    ('Fear Of The Dark', 'Steve Harris')
    ('Fear Of The Dark', 'Steve Harris')
    ('Fear Of The Dark', 'Steve Harris')
    ('February Stars', 'Dave, Taylor, Nate, Chris')
    ('Feel It', 'E. Schrody/R. Medrano')
    ('Feel Your Love Tonight', 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('Feira Moderna', 'Beto Guedes/Fernando Brant/L Borges')
    ('Feirinha da Pavuna/Luz do Repente/Bagaço da Laranja', 'Arlindo Cruz/Franco/Marquinhos PQD/Negro, Jovelina Pérolo/Zeca Pagodinho')
    ('Fell On Black Days', 'Chris Cornell')
    ('Fica', 'Chico Amaral/Samuel Rosa')
    ('Fight Fire With Fire', 'Metallica')
    ('Fight From The Inside', 'Taylor')
    ('Finally Forever', 'Chris Cornell')
    ('Finding My Way', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Fire', 'Jimi Hendrix')
    ('Fire Fire', 'Clarke/Kilmister/Taylor')
    ('Fire In The Basement', 'Blackmore, Glover, Turner, Lord, Paice')
    ('Fire In The Head', 'The Tea Party')
    ('Fire in the Hole', 'Van Halen')
    ('Fireball', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('Firmamento', 'Bino Farias/Da Gama/Henry Lawes/Lazão/Toni Garrido/Winston Foser-Vers')
    ('Firmamento', 'Harry Lawes/Winston Foster-Vers')
    ('First Time I Met The Blues', 'Eurreal Montgomery')
    ('Fixxxer', 'Hetfield, Ulrich, Hammett')
    ('Flash', 'May, Brian')
    ('Flash of The Blade', 'Dickinson')
    ('Flight Of Icarus', 'Smith/Dickinson')
    ('Flight Of The Icarus', 'Adrian Smith/Bruce Dickinson')
    ('Flight Of The Rat', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Flip The Switch', 'Jagger/Richards')
    ('Flor De Lis', 'Djavan')
    ('Flores', 'Titãs')
    ('Flower', 'Chris Cornell/Kim Thayil')
    ('Fly Away', 'Lenny Kravitz')
    ('Fly By Night', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Fly Me To The Moon', 'bart howard')
    ('Flying High Again', 'L. Kerslake, O. Osbourne, R. Daisley & R. Rhoads')
    ('Flying High Again', 'O. Osbourne, R. Daisley, R. Rhoads, L. Kerslake')
    ('Fool For Your Loving', 'Marsden/Moody')
    ('Fool In The Rain', 'Jimmy Page, Robert Plant & John Paul Jones')
    ('Fools', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('For Once In My Life', 'orlando murden/ronald miller')
    ('For Those About To Rock (We Salute You)', 'Angus Young, Malcolm Young, Brian Johnson')
    ('For Whom The Bell Tolls', 'Metallica')
    ('For Your Babies', 'Mick Hucknall')
    ('For Your Life', 'Jimmy Page/Robert Plant')
    ('Forgiven', 'Alanis Morissette & Glenn Ballard')
    ('Fortunate Son', 'J. C. Fogerty')
    ('Fortunes Of War', 'Steve Harris')
    ('Fortuneteller', 'Blackmore, Glover, Turner, Lord, Paice')
    ('Four Sticks', 'Jimmy Page, Robert Plant')
    ('Foxy Lady', 'Jimi Hendrix')
    ('Frantic', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Free Me', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('Free Speech For The Dumb', 'Molaney/Morris/Roberts/Wainwright')
    ('Freedom For My People', 'Mabins, Macie/Magee, Sterling/Robinson, Bobby')
    ('Freewill', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Fried Neckbones And Home Fries', 'W.Correa')
    ('Friend Of A Friend', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Friends', 'Jimmy Page, Robert Plant')
    ('Friends Will Be Friends', 'Freddie Mercury & John Deacon')
    ('From Afar', 'Van Halen')
    ('From Here To Eternity', 'Steve Harris')
    ('From Here To Eternity', 'Steve Harris')
    ('From Out Of Nowhere', 'Faith No More')
    ('Fuel', 'Hetfield, Ulrich, Hammett')
    ('Funky Monks', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Futureal', 'Blaze Bayley/Steve Harris')
    ('Fé Cega, Faca Amolada', 'Milton Nascimento, Ronaldo Bastos')
    ('Gallows Pole', 'Traditional')
    ('Gangland', 'Adrian Smith/Clive Burr/Steve Harris')
    ('Garden', 'Jeff Ament/Stone Gossard')
    ('Garota De Ipanema', 'Vários')
    ('Garota Nacional', 'Samuel Rosa')
    ('Garotas do Brasil', 'Garay, Ricardo Engels/Luca Predabom/Ludwig, Carlos Henrique/Maurício Vieira')
    ('Gasoline', 'Audioslave/Chris Cornell')
    ('Gates Of Tomorrow', 'Bruce Dickinson/Janick Gers/Steve Harris')
    ('Gates Of Urizen', 'Roy Z')
    ('Geek Stink Breath', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Generique', 'Miles Davis')
    ('Genghis Khan', 'Steve Harris')
    ('Geração Coca-Cola', 'Renato Russo')
    ('Get Down, Make Love', 'Mercury')
    ('Get In The Ring', 'Duff McKagan/Slash/W. Axl Rose')
    ('Get Me Outta Here', 'C. Cester/N. Cester')
    ('Get Off Of My Cloud', 'Jagger/Richards')
    ('Get On The Good Foot', 'Fred Wesley/James Brown/Joseph Mims')
    ('Get On The Snake', 'Chris Cornell/Kim Thayil')
    ('Get On Top', 'Red Hot Chili Peppers')
    ('Get Out', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Get Right', 'Matt Cameron')
    ('Get Up', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Get Up (I Feel Like Being A) Sex Machine', 'Bobby Byrd/James Brown/Ron Lenhoff')
    ('Get Up Offa That Thing', 'Deanna Brown/Deidra Jenkins/Yamma Brown')
    ('Get What You Need', 'C. Cester/C. Muncey/N. Cester')
    ('Getaway Car', 'Audioslave/Chris Cornell')
    ("Gettin' Tighter", 'Bolin/Hughes')
    ('Ghost', 'Jeff Ament')
    ('Ghost Of The Navigator', 'Bruce Dickinson/Janick Gers/Steve Harris')
    ('Ghost Of The Navigator', 'Bruce Dickinson/Janick Gers/Steve Harris')
    ('Ghosts', 'Chris Cornell')
    ('Gimmie Shelters', 'Jagger/Richards')
    ('Girassol', 'Bino Farias/Da Gama/Lazão/Pedro Luis/Toni Garrido')
    ('Girl From A Pawnshop', 'Chris Robinson/Rich Robinson')
    ('Girls, Girls, Girls', 'Mick Mars/Nikki Sixx/Tommy Lee')
    ('Give It Away', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Give Me Love', 'Caetano Veloso e Gilberto Gil')
    ('Give Me Novacaine', 'Green Day')
    ('Given To Fly', 'Eddie Vedder & Mike McCready')
    ('Giz', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Glitter', 'Bryan Adams/Nikki Sixx/Scott Humphrey')
    ('Glorified G', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Go', 'Dave Abbruzzese & Jeff Ament & Stone Gossard & Mike McCready & Eddie Vedder')
    ('Go', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Go Back', 'Titãs')
    ('Go Down', 'AC/DC')
    ("God Gave Rock 'n' Roll To You", 'Paul Stanley, Gene Simmons, Rus Ballard, Bob Ezrin')
    ('God Of Thunder', 'Paul Stanley')
    ('God Part II', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ("Goin' Blind", 'Gene Simmons, S. Coronel')
    ("Goin' Blind", 'Gene Simmons, Stephen Coronel')
    ('Going Down / Highway Star', 'Gillan/Glover/Lord/Nix - Blackmore/Paice')
    ('Going To California', 'Robert Plant')
    ('Going To California', 'Jimmy Page, Robert Plant')
    ('Gone', 'Eddie Vedder')
    ('Gone', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ("Gonna Give Her All The Love I've Got", 'Barrett Strong/Norman Whitfield')
    ("Gonna Keep On Tryin' Till I Win Your Love", 'Barrett Strong/Norman Whitfield')
    ('Good Golly Miss Molly', 'Little Richard')
    ('Good Golly Miss Molly', 'J.C. Fogerty')
    ('Good Old-Fashioned Lover Boy', 'Mercury, Freddie')
    ('Good Riddance (Time Of Your Life)', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Good Times Bad Times', 'Jimmy Page/John Bonham/John Paul Jones')
    ('Goodbye To Romance', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Got That Feeling', 'Mike Patton')
    ('Grace', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Gran Circo', 'Milton Nascimento, Márcio Borges')
    ('Grande Rio', 'Carlos Santos/Ciro/Claudio Russo/Zé Luiz')
    ('Greasy Grass River', 'Chris Robinson/Rich Robinson')
    ('Green Disease', 'Eddie Vedder')
    ('Green Grow The Rushes', 'R.E.M.')
    ('Green River', 'J. C. Fogerty')
    ('Grito De Alerta', 'Gonzaga Jr.')
    ('Groovus Interruptus', 'Jim Beard')
    ('Guanabara', 'Marcos Valle')
    ("Guess Who's Back", 'E. Schrody/L. Muggerud')
    ('Gypsy', 'Coverdale/Hughes/Lord/Paice')
    ('Gypsy', 'Kevin Robinson')
    ('Gyroscope', 'The Tea Party')
    ('Hail, Hail', 'Stone Gossard & Eddie Vedder & Jeff Ament & Mike McCready')
    ('Hairshirt', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Half A World Away', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Half The Man', 'Toby Smith')
    ('Hallelujah Here She Comes', 'U2')
    ('Hallowed Be Thy Name', 'Steve Harris')
    ('Hallowed Be Thy Name', 'Harris')
    ('Hallowed Be Thy Name', 'Steve Harris')
    ('Hallowed Be Thy Name', 'Steve Harris')
    ('Halo', 'Foo Fighters')
    ('Hammer To Fall', 'Brian May')
    ('Hand In My Pocket', 'Alanis Morissette & Glenn Ballard')
    ('Hands All Over', 'Chris Cornell/Kim Thayil')
    ("Hang 'Em High", 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Happy Jack', 'Pete Townshend')
    ('Happy Trails', 'Dale Evans')
    ("Hard Lovin' Man", 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Hard Luck Woman', 'Paul Stanley')
    ('Hard To Handle', 'A.Isbell/A.Jones/O.Redding')
    ('Harvester Of Sorrow', 'Apocalyptica')
    ('Harvester Of Sorrow', 'James Hetfield and Lars Ulrich')
    ('Hats Off To (Roy) Harper', 'Traditional')
    ('Have It All', 'Foo Fighters')
    ('Have You Ever Seen The Rain?', 'J. C. Fogerty')
    ('Hawkmoon 269', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('He Can Only Hold Her', 'Richard Poindexter & Robert Poindexter')
    ('Head Over Feet', 'Alanis Morissette & Glenn Ballard')
    ('Headlong', 'Queen')
    ('Headspace', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Heart In Your Hand', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Heart Of Lothian: Wide Boy / Curtain Call', 'Kelly, Mosley, Rothery, Trewaves')
    ('Heart Of Stone', 'Jagger/Richards')
    ('Heart-Shaped Box', 'Kurt Cobain')
    ('Heartbreaker', 'John Bonham/John Paul Jones/Robert Plant')
    ('Heartbreaker', 'Jimmy Page, Robert Plant, John Paul Jones, John Bonham')
    ('Heartland', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Heaven Can Wait', 'Steve Harris')
    ('Heaven Can Wait', 'Steve Harris')
    ('Heaven Coming Down', 'The Tea Party')
    ('Heaven Help', 'Gerry DeVeaux/Terry Britten')
    ("Heaven's Dead", 'Cornell, Commerford, Morello, Wilk')
    ('Heavy Love Affair', 'Marvin Gaye')
    ('Heliopolis', 'Jay Beckenstein')
    ('Hell', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ("Hell Ain't A Bad Place To Be", 'AC/DC')
    ('Hello Mary Lou', 'J.C. Fogerty')
    ('Help Help', 'Jeff Ament')
    ('Help Yourself', 'Freddy James, Jimmy hogarth & Larry Stock')
    ('Helpless', 'Bill Gould/Mike Bordin/Mike Patton')
    ('Helpless', 'Harris/Tatler')
    ('Helter Skelter', 'Lennon, John/McCartney, Paul')
    ('Here I Go Again', 'Marsden')
    ("Here's To The Atom Bomb", 'Billy Corgan')
    ('Hereditário', 'Titãs')
    ('Hero Of The Day', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('Hey America', 'Addie William Jones/Nat Jones')
    ('Hey Cisco', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Hey Hey', 'Big Bill Broonzy')
    ('Hey Joe', 'Billy Roberts')
    ('Hey Tonight', 'J. C. Fogerty')
    ('Hey, Johnny Park!', 'Dave, Taylor, Nate, Chris')
    ('High Ball Shooter', 'D.Coverdale/G.Hughes/Glenn Hughes/I.Paice/Ian Paice/J.Lord/John Lord/R.Blackmore/Ritchie Blackmore')
    ('High Head Blues', 'Chris Robinson/Rich Robinson')
    ('Highway Chile', 'Jimi Hendrix')
    ('Highway Star', 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('Hill of the Skull', 'J. Satriani')
    ('Hit The Lights', 'James Hetfield, Lars Ulrich')
    ("Hitchin' A Ride", 'Billie Joe Armstrong -Words Green Day -Music')
    ('Hitsville UK', 'The Clash')
    ('Hold On', 'D.Coverdal/G.Hughes/Glenn Hughes/I.Paice/Ian Paice/J.Lord/John Lord')
    ('Holding Back The Years', 'Mick Hucknall and Neil Moss')
    ('Holiday', 'Billie Joe Armstrong, Mike Dirnt, Tré Cool')
    ('Holier Than Thou', 'Ulrich')
    ('Holy Man', 'D.Coverdale/G.Hughes/Glenn Hughes/J.Lord/John Lord')
    ('Holy Smoke', 'Bruce Dickinson/Steve Harris')
    ('Home Sick Home', 'Mike Patton')
    ('Home Sweet Home', 'Nikki Sixx/Tommy Lee/Vince Neil')
    ("Homecoming / The Death Of St. Jimmy / East 12th St. / Nobody Likes You / Rock And Roll Girlfriend / We're Coming Home Again", 'Mike Dirnt/Tré Cool')
    ('Homem Primata', 'Titãs')
    ('Homem Primata (Vinheta)', 'Titãs')
    ('Hooked Up', 'Smith, Toby')
    ('Hooks In You', 'Adrian Smith/Bruce Dickinson')
    ('Hot Dog', 'Jimmy Page & Robert Plant')
    ('Hot Pants Pt.1', 'Fred Wesley/James Brown')
    ('Hots On For Nowhere', 'Jimmy Page/Robert Plant')
    ('House And The Rising Sun', 'E. Schrody/J. Vasquez/L. Dimant')
    ('House Of Love', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('House Of Pain Anthem', 'E. Schrody/L. Dimant')
    ('Houses Of The Holy', 'Jimmy Page/Robert Plant')
    ('How Many More Times', 'Chester Burnett/Jimmy Page/John Bonham/John Paul Jones/Robert Plant')
    ('How Many More Times', 'Jimmy Page/John Bonham/John Paul Jones')
    ('How Many Say I', 'Van Halen')
    ('How The West Was Won And Where It Got Us', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Humans Being', 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, Sammy Hagar')
    ('Hush', 'South')
    ('Hypnotize', 'Audioslave/Chris Cornell')
    ('Há Tempos', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('I Am', 'Sully Erna')
    ('I Am Mine', 'Eddie Vedder')
    ('I Believe', 'R.E.M.')
    ('I Belong To You', 'Lenny Kravitz')
    ('I Can See For Miles', 'Pete Townshend')
    ("I Can't Explain", 'Pete Townshend')
    ("I Can't Quit You Baby", 'Willie Dixon')
    ("I Can't Quit You Baby", 'Willie Dixon')
    ("I Can't Quit You Baby", 'Willie Dixon')
    ("I Can't Quit You Baby(2)", 'Willie Dixon')
    ("I Can't Remember", 'Jerry Cantrell, Layne Staley')
    ("I Can't Stand It", 'Clapton')
    ('I Could Die For You', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('I Could Have Lied', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ("I Don't Know", 'B. Daisley, O. Osbourne & R. Rhoads')
    ("I Don't Know", 'O. Osbourne, R. Daisley, R. Rhoads')
    ("I Don't Live Today", 'Jimi Hendrix')
    ("I Don't Wanna Be Kissed (By Anyone But You)", 'H. Spina, J. Elliott')
    ("I Don't Wanna Be Kissed (By Anyone But You) (Alternate Take)", 'H. Spina, J. Elliott')
    ('I Feel Free', 'Bruce/Clapton')
    ('I Feel Good (I Got You) - Sossego', 'James Brown/Tim Maia')
    ('I Fought The Law', 'Sonny Curtis')
    ('I Fucking Hate You', 'Sully Erna')
    ('I Get A Kick Out Of You', 'cole porter')
    ('I Go Wild', 'Jagger/Richards')
    ('I Got You (I Feel Good)', 'James Brown')
    ("I Guess You're Right", 'Darius "Take One" Minwalla/Jon Auer/Ken Stringfellow/Matt Harris')
    ('I Heard It Through The Grapevine', 'Whitfield-Strong')
    ('I Ka Barra (Your Work)', 'Habib Koité')
    ('I Know Somethin (Bout You)', 'Jerry Cantrell')
    ('I Like Dirt', 'Red Hot Chili Peppers')
    ('I Looked At You', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('I Need Love', 'Bolin/Coverdale')
    ('I Put A Spell On You', 'Jay Hawkins')
    ('I Remember California', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('I Shot The Sheriff', 'Marley')
    ('I Stand Alone', 'Sully Erna')
    ("I Still Haven't Found What I'm Looking For", 'U2')
    ("I Still Haven't Found What I'm Looking for", 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('I Still Love You', 'Paul Stanley')
    ('I Want It All', 'Queen')
    ('I Want To Break Free', 'John Deacon')
    ('I Was Made For Loving You', 'Paul Stanley, Vincent Poncia, Desmond Child')
    ('I Will Follow', 'U2')
    ('I Wish It Would Rain', 'Barrett Strong/Norman Whitfield/Roger Penzabene')
    ('I am the Highway', 'Audioslave/Chris Cornell')
    ("I'm A Boy", 'Pete Townshend')
    ("I'm A Greedy Man Pt.1", 'Charles Bobbitt/James Brown')
    ("I'm Going Slightly Mad", 'Queen')
    ("I'm Gonna Crawl", 'Jimmy Page, Robert Plant & John Paul Jones')
    ("I'm Real", 'Full Force/James Brown')
    ("I'm The One", 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ("I've Got You Under My Skin", 'cole porter')
    ('Ice Cream Man', 'John Brim')
    ('Idolatrada', 'Milton Nascimento, Fernando Brant')
    ('If God Will Send His Angels', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('If I Like It, I Do It', 'Gelder, Nick van')
    ("If You Don't Know Me By Now", 'Kenny Gamble and Leon Huff')
    ('If You Have To Ask', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('If You Wear That Velvet Dress', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Illegal I Song', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Immigrant Song', 'Robert Plant')
    ('Immigrant Song', 'Jimmy Page, Robert Plant')
    ('Imperatriz', 'Guga/Marquinho Lessa/Tuninho Professor')
    ('Império Serrano', 'Arlindo Cruz/Carlos Sena/Elmo Caetano/Mauricao')
    ('In A Little While', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('In Bloom', 'Kurt Cobain')
    ('In My Bed', 'Salaam Remi')
    ('In My Time Of Dying', 'John Bonham/John Paul Jones')
    ('In The Evening', 'Jimmy Page, Robert Plant & John Paul Jones')
    ('In The Light', 'John Paul Jones/Robert Plant')
    ('In Time', 'Sylvester Stewart')
    ('In Your Honor', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('Indifference', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Indios', 'Renato Russo')
    ('Infeliz Natal', 'Rodolfo')
    ('Infinite Dreams', 'Steve Harris')
    ('Inject The Venom', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Innocent Exile', 'Di´Anno/Harris')
    ('Innuendo', 'Queen')
    ('Insensível', 'Sérgio Britto')
    ('Inside Job', 'Eddie Vedder & Mike McCready')
    ('Interlude Zumbi', 'Chico Science')
    ('Into The Fire', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Into The Light', 'David Coverdale')
    ('Intoitus: Adorate Deum', 'Anonymous')
    ('Intro', 'Kurt Cobain')
    ('Intro', 'Jagger/Richards')
    ('Intruder', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Invaders', 'Steve Harris')
    ('Invisible Kid', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Invisible Sun', 'G M Sumner')
    ('Iron Maiden', 'Steve Harris')
    ('Iron Maiden', 'Harris')
    ('Iron Maiden', 'Steve Harris')
    ('Iron Maiden', 'Steve Harris')
    ('Iron Man', 'A. F. Iommi, W. Ward, T. Butler, J. Osbourne')
    ('Ironic', 'Alanis Morissette & Glenn Ballard')
    ('Is This Love', 'Sykes')
    ("It Ain't Like That", 'Jerry Cantrell, Michael Starr, Sean Kinney')
    ("It Ain't Over 'Til It's Over", 'Lenny Kravitz')
    ('It Came Out Of The Sky', 'J.C. Fogerty')
    ("It Doesn't Matter", 'Chet Catallo')
    ('It Was A Very Good Year', 'ervin drake')
    ("It's A Bitter Pill To Swallow", 'Smokey Robinson/Warren "Pete" Moore')
    ("It's A Hard Life", 'Freddie Mercury')
    ("It's A Man's Man's Man's World", 'Betty Newsome/James Brown')
    ("It's Electric", 'Harris/Tatler')
    ("It's Just A Thought", 'J.C. Fogerty')
    ("It's Late", 'May')
    ("It's Only Love", 'Jimmy and Vella Cameron')
    ("It's The End Of The World As We Know It (And I Feel Fine)", 'R.E.M.')
    ("It's Too Funky In Here", 'Brad Shapiro/George Jackson/Robert Miller/Walter Shaw')
    ('Ito Okashi', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('J.A.R. (Jason Andrew Relva)', 'Mike Dirnt -Words Green Day -Music')
    ("Jacob's Ladder", 'Julian Crampton')
    ('Jaded', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Jailbait', 'Clarke/Kilmister/Taylor')
    ("Jamie's Cryin'", 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ("Janie's Got A Gun", 'Steven Tyler, Tom Hamilton')
    ('Jean Pierre (Live)', 'Miles Davis')
    ('Jeremy', 'Jeff Ament')
    ('Jeru', 'Miles Davis')
    ('Jerusalem', 'Roy Z')
    ('Jesus Christ Pose', 'Ben Shepherd/Chris Cornell/Kim Thayil/Matt Cameron')
    ("Jesus Of Suburbia / City Of The Damned / I Don't Care / Dearly Beloved / Tales Of Another Broken Home", 'Billie Joe Armstrong/Green Day')
    ('Jingo', 'M.Babatunde Olantunji')
    ('Johnny B. Goode', 'Chuck Berry')
    ('Join Together', 'Pete Townshend')
    ('Jorge Da Capadócia', 'Jorge Ben')
    ('Josephina', 'Van Halen')
    ('Journey Into Sunlight', 'Jean Paul Maunick')
    ('Journey To Arnhemland', 'Toby Smith/Wallis Buchanan')
    ('Journeyman', 'Bruce Dickinson/David Murray/Steve Harris')
    ('Juazeiro', 'Humberto Teixeira/Luiz Gonzaga')
    ('Jubilee', 'Jeremy Wall')
    ('Judas Be My Guide', 'Bruce Dickinson/David Murray')
    ('Judgement Day', 'Vandenberg')
    ('Judgement Of Heaven', 'Steve Harris')
    ('Jump', 'Edward Van Halen, Alex Van Halen, David Lee Roth')
    ('Jump Around', 'E. Schrody/L. Muggerud')
    ('Jump Around (Pete Rock Remix)', 'E. Schrody/L. Muggerud')
    ('Jump In The Fire', 'James Hetfield, Lars Ulrich, Dave Mustaine')
    ('Jupiter, the Bringer of Jollity', 'Gustav Holst')
    ('Just A Man', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Just Another Story', 'Toby Smith')
    ('Já Foi', 'Bino Farias/Da Gama/Lazão/Toni Garrido')
    ('Já Foi', 'Mônica Marianno')
    ('Karelia Suite, Op.11: 2. Ballade (Tempo Di Menuetto)', 'Jean Sibelius')
    ('Kashmir', 'John Bonham')
    ('Kayleigh', 'Kelly, Mosley, Rothery, Trewaves')
    ('Keep It To Myself (Aka Keep It To Yourself)', 'Sonny Boy Williamson [I]')
    ('Kickstart My Heart', 'Nikki Sixx')
    ('Killer Queen', 'Mercury, Freddie')
    ('Killers', 'Steve Harris')
    ('Killers', "Paul Di'Anno/Steve Harris")
    ('Killing Birds', 'Chris Cornell')
    ('Killing Floor', 'Adrian Smith')
    ('Killing Time', 'Sweet Savage')
    ('King For A Day', 'Mike Bordin, Billy Gould, Mike Patton, Trey Spruance')
    ('King For A Day', 'Jay Kay/Toby Smith')
    ('King In Crimson', 'Roy Z')
    ('King Nothing', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('King Of Dreams', 'Blackmore, Glover, Turner')
    ('King Of Pain', 'G M Sumner')
    ('Kir Royal', 'Mônica Marianno')
    ('Kite', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Knockin On Heavens Door', 'Clapton/Dylan')
    ("Knockin' On Heaven's Door", 'Bob Dylan')
    ('Knocking At Your Back Door', 'Richie Blackmore, Ian Gillian, Roger Glover')
    ('Know Your Rights', 'The Clash')
    ('Koyaanisqatsi', 'Philip Glass')
    ("L'Arc En Ciel De Miles", 'Kevin Robinson/Richard Bull')
    ("L'Avventura", 'Renato Russo')
    ("L'orfeo, Act 3, Sinfonia (Orchestra)", 'Claudio Monteverdi')
    ('L.A. Is My Lady', 'alan bergman/marilyn bergman/peggy lipton jones/quincy jones')
    ('La Bella Luna', 'Herbert Vianna')
    ('La Puesta Del Sol', 'E.Weiss')
    ('La Villa Strangiato', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Lady Double Dealer', 'Coverdale')
    ('Lady Double Dealer', 'D.Coverdale/R.Blackmore/Ritchie Blackmore')
    ('Lady Luck', 'Cook/Coverdale')
    ('Laguna Sunrise', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Lament', 'J.J. Johnson')
    ('Lamentations of Jeremiah, First Set \\ Incipit Lamentatio', 'Thomas Tallis')
    ('Lamento Sertanejo', 'Dominguinhos/Gilberto Gil')
    ('Landslide', 'Stevie Nicks')
    ('Last Caress/Green Hell', 'Danzig')
    ('Last Chance', 'C. Cester/C. Muncey')
    ('Last Cup Of Sorrow', 'Bill Gould/Mike Patton')
    ('Last Night On Earth', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Latinha de Cerveja', 'Adriano Bernandes/Edmar Neves')
    ('Lavadeira', 'Do Vale, Valverde/Gal Oliveira/Luciano Pinto')
    ('Lavender', 'Kelly, Mosley, Rothery, Trewaves')
    ('Lay Down Sally', 'Clapton/Levy')
    ('Layla', 'Clapton/Gordon')
    ('Layla', 'Eric Clapton, Jim Gordon')
    ('Lazy', 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('Lazy Gun', 'C. Cester/N. Cester')
    ('Le Sacre Du Printemps: I.iv. Spring Rounds', 'Igor Stravinsky')
    ('Leash', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Leave', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Leave My Girl Alone', 'Buddy Guy')
    ('Leave My Girl Alone', 'B. Guy')
    ('Leila', 'Renato Russo')
    ('Leila (Venha Ser Feliz)', 'Milton Nascimento')
    ('Lemon', 'U2; Bono')
    ('Leper Messiah', 'C.Burton')
    ('Let It Grow', 'Clapton')
    ('Let Love Rule', 'Lenny Kravitz')
    ('Let Me Love You Baby', 'Willie Dixon')
    ('Let Me Love You Baby', 'Willie Dixon')
    ('Let There Be Rock', 'AC/DC')
    ("Let's Get It Up", 'Angus Young, Malcolm Young, Brian Johnson')
    ("Let's See Action", 'Pete Townshend')
    ("Let's Spend The Night Together", 'Jagger/Richards')
    ('Letterbomb', 'Green Day')
    ('Levada do Amor (Ailoviu)', 'Luiz Wanderley/Paulo Levi')
    ('Lick It Up', 'roger glover')
    ("Lickin'", 'Chris Robinson/Rich Robinson')
    ('Life During Wartime', 'Chris Frantz/David Byrne/Jerry Harrison/Tina Weymouth')
    ('Life Goes On', 'E. Schrody/R. Medrano')
    ('Life Line', 'The Tea Party')
    ('Life Wasted', 'Stone Gossard')
    ('Light My Fire', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('Light My Way', 'Audioslave/Chris Cornell')
    ('Light Years', 'Toby Smith')
    ('Lightning Strikes Twice', 'David Murray/Steve Harris')
    ('Like A Song...', 'U2')
    ('Like a Stone', 'Audioslave/Chris Cornell')
    ('Lindo Lago Do Amor', 'Gonzaga Jr.')
    ('Linha Do Equador', 'Caetano Veloso - Djavan')
    ('Linha Do Horizonte', 'Vários')
    ('Lithium', 'Kurt Cobain')
    ('Lithium', 'Kurt Cobain')
    ('Little Church (Live)', 'Miles Davis')
    ('Little Dreamer', 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('Little Guitars', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Little Guitars (Intro)', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Little Linda', 'Jeremy Wall')
    ('Live To Win', 'Clarke/Kilmister/Taylor')
    ('Live With Me', 'Jagger/Richards')
    ("Livin' On The Edge", 'Steven Tyler, Joe Perry, Mark Hudson')
    ('Living In America', 'Charlie Midnight/Dan Hartman')
    ("Living Loving Maid (She's Just A Woman)", 'Jimmy Page, Robert Plant')
    ('Living On Love', 'Bossi/David Coverdale/Earl Slick')
    ('Living Wreck', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Locomotive', 'Slash/W. Axl Rose')
    ('Lodi', 'J. C. Fogerty')
    ('London Calling', 'Joe Strummer/Mick Jones')
    ('Lonely As You', 'Foo Fighters')
    ('Lonely Stranger', 'Eric Clapton')
    ('Long As I Can See The Light', 'J. C. Fogerty')
    ('Long Tall Sally', 'Enotris Johnson/Little Richard/Robert "Bumps" Blackwell')
    ('Longe Do Meu Lado', 'Renato Russo - Marcelo Bonfá')
    ('Longview', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Look For The Truth', 'Blaze Bayley/Janick Gers/Steve Harris')
    ("Look What You've Done", 'N. Cester')
    ("Lookin' For A Reason", 'J.C. Fogerty')
    ("Lookin' Out My Back Door", 'J. C. Fogerty')
    ('Looking For Love', 'Sykes')
    ('Looks That Kill', 'Nikki Sixx')
    ('Loosen My Strings', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Lord Of The Flies', 'Janick Gers/Steve Harris')
    ('Lords Of The Backstage', 'Kelly, Mosley, Rothery, Trewaves')
    ('Lords of Karma', 'J. Satriani')
    ('Los Pretos', 'Samuel Rosa')
    ('Losfer Words', 'Steve Harris')
    ('Losing My Religion', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Lost in Hollywood', 'Tankian, Serj')
    ('Loud Love', 'Chris Cornell')
    ('Lounge Act', 'Kurt Cobain')
    ('Lourinha Bombril', 'Bahiano/Diego Blanco/Herbert Vianna')
    ("Love Ain't No Stranger", 'Galley')
    ('Love And Marriage', 'jimmy van heusen/sammy cahn')
    ('Love And Peace Or Else', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Love Boat Captain', 'Eddie Vedder')
    ('Love Child', 'Bolin/Coverdale')
    ('Love Comes', 'Darius "Take One" Minwalla/Jon Auer/Ken Stringfellow/Matt Harris')
    ('Love Comes Tumbling', 'U2')
    ('Love Conquers All', 'Blackmore, Glover, Turner')
    ("Love Don't Mean a Thing", 'D.Coverdale/G.Hughes/Glenn Hughes/I.Paice/Ian Paice/J.Lord/John Lord/R.Blackmore/Ritchie Blackmore')
    ('Love Gun', 'Paul Stanley')
    ('Love In An Elevator', 'Steven Tyler, Joe Perry')
    ('Love Is Blind', 'David Coverdale/Earl Slick')
    ('Love Is Blindness', 'U2')
    ('Love Is Strong', 'Jagger/Richards')
    ('Love Is The Colour', 'R. Carless')
    ("Love Me Darlin'", 'C. Burnett')
    ('Love Me Like A Reptile', 'Clarke/Kilmister/Taylor')
    ('Love Of My Life', 'Carlos Santana & Dave Matthews')
    ('Love Or Confusion', 'Jimi Hendrix')
    ('Love Rescue Me', 'Bono/Clayton, Adam/Dylan, Bob/Mullen Jr., Larry/The Edge')
    ('Love, Hate, Love', 'Jerry Cantrell, Layne Staley')
    ('Loverman', 'Cave')
    ('Loves Been Good To Me', 'rod mckuen')
    ('Loving The Alien', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Loving You Is Sweeter Than Ever', 'Ivy Hunter/Stevie Wonder')
    ('Low', 'Foo Fighters')
    ('Low', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Low Desert', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ("Low Man's Lyric", 'Hetfield, Ulrich')
    ('Lua de Ogum', 'Ratinho/Zeca Pagodinho')
    ('Lucky 13', 'Billy Corgan')
    ('Lugar Nenhum', 'Arnaldo Antunes/Charles Gavin/Marcelo Fromer/Sérgio Britto/Toni Bellotto')
    ('Luis Inacio (300 Picaretas)', 'Herbert Vianna')
    ('Luminous Times (Hold On To Love)', 'Brian Eno/U2')
    ('MFC', 'Eddie Vedder')
    ('Machine Men', 'Adrian Smith')
    ('Mack The Knife', 'bert brecht/kurt weill/marc blitzstein')
    ("Macy's Day Parade", 'Billie Joe Armstrong -Words Green Day -Music')
    ('Macô', 'Chico Science')
    ('Madama Butterfly: Un Bel Dì Vedremo', 'Giacomo Puccini')
    ('Magamalabares', 'Carlinhos Brown')
    ('Magic Bus', 'Pete Townshend')
    ('Magnetic Ocean', 'Patrick Claher/Richard Bull')
    ('Make It Funky Pt.1', 'Charles Bobbitt/James Brown')
    ('Make Me Believe', 'Sully Erna')
    ('Malted Milk', 'Robert Johnson')
    ('Mama Said', 'James Hetfield, Lars Ulrich')
    ("Mama, I'm Coming Home", 'L. Kilmister, O. Osbourne & Z. Wylde')
    ('Man In The Box', 'Jerry Cantrell, Layne Staley')
    ('Man On The Edge', 'Blaze Bayley/Janick Gers')
    ('Man Or Animal', 'Cornell, Commerford, Morello, Wilk')
    ('Man With The Woman Head', 'Don Van Vliet')
    ('Mangueira', "Bizuca/Clóvis Pê/Gilson Bernini/Marelo D'Aguia")
    ('Manguetown', 'Chico Science')
    ('Manguetown', 'Chico Science/Dengue/Lúcio Maia')
    ('Manic Depression', 'Jimi Hendrix')
    ('Manifest Destiny', 'Toby Smith')
    ('Maquinarama', 'Chico Amaral/Samuel Rosa')
    ('Maracatu Atômico', 'Chico Science')
    ('Maracatu Atômico [Atomic Version]', 'Chico Science')
    ('Maracatu Atômico [Ragga Mix]', 'Chico Science')
    ('Maracatu Atômico [Trip Hop]', 'Chico Science')
    ('Maraçá', 'Carlinhos Brown')
    ('Maria', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Maria Fumaça', 'Luiz Carlos/Oberdan')
    ('Maria Maria', 'W. Jean, J. Duplessis, Carlos Santana, K. Perazzo & R. Rekow')
    ('Maria, Maria', 'Milton Nascimento, Fernando Brant')
    ('Marker In The Sand', 'Mike McCready')
    ('Marquis In Spades', 'Billy Corgan')
    ('Marvin', 'Titãs')
    ('Mary Jane', 'Alanis Morissette & Glenn Ballard')
    ('Mas Que Nada', 'Jorge Ben')
    ('Master Of Puppets', 'Apocalyptica')
    ('Master Of Puppets', 'K.Hammett')
    ('Mateus Enter', 'Chico Science')
    ('May This Be Love', 'Jimi Hendrix')
    ("Maybe I'm A Leo", 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('Me In Honey', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Me Wise Magic', 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, David Lee Roth')
    ('Mean Disposition', 'Jagger/Richards')
    ('Meditação', 'Tom Jobim - Newton Mendoça')
    ('Mel', 'Caetano Veloso - Waly Salomão')
    ('Mellowship Slinky In B Major', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Memory Motel', 'Jagger/Richards')
    ('Menestrel Das Alagoas', 'Milton Nascimento, Fernando Brant')
    ('Menina Bonita', 'Alexandre Brazil/Pedro Luis/Rodrigo Cabelo')
    ('Menino do Rio', 'Caetano Veloso')
    ('Meninos E Meninas', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Mensagem', 'Bino Farias/Da Gama/Lazão/Rás Bernardo')
    ('Mensagen De Amor (2000)', 'Herbert Vianna')
    ('Mercyful Fate', 'Diamond/Shermann')
    ('Merry Christmas', 'Rodolfo')
    ('Message in a Bottle', 'G M Sumner')
    ('Message in a Bottle (new classic rock mix)', 'G M Sumner')
    ('Metal Militia', 'James Hetfield, Lars Ulrich, Dave Mustaine')
    ('Metopes, Op. 29: Calypso', 'Karol Szymanowski')
    ('Meu Erro', 'Herbert Vianna')
    ('Meu Refrigerador Não Funciona', 'Arnaldo Baptista - Rita Lee - Sérgio Dias')
    ('Miami', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Midnight', 'J. Satriani')
    ('Midnight', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Midnight Blue', 'David Coverdale/Earl Slick')
    ('Midnight From The Inside Out', 'Chris Robinson/Rich Robinson')
    ('Migra', 'R. Taha, Carlos Santana & T. Lindsay')
    ('Mil Pedaços', 'Renato Russo')
    ('Miles Ahead', 'Miles Davis, Gil Evans')
    ('Miles Runs The Voodoo Down', 'Miles Davis')
    ('Milk It', 'Kurt Cobain')
    ('Millenium', 'Maxton Gig Beesley Jnr.')
    ('Minas', 'Milton Nascimento, Caetano Veloso')
    ('Minha Fé', 'Murilão')
    ('Minor Thing', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Minority', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Miracle', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Miracle Drug', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Miracle To Me', 'Chris Robinson/Rich Robinson')
    ('Miserere mei, Deus', 'Gregorio Allegri')
    ('Miss Sarajevo', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Missa Papae Marcelli: Kyrie', 'Giovanni Pierluigi da Palestrina')
    ('Mistreated', 'Coverdale')
    ('Mistreated (Alternate Version)', 'Blackmore/Coverdale')
    ('Misty Mountain Hop', 'Jimmy Page, Robert Plant, John Paul Jones')
    ('Mistério da Raça', 'Luiz Melodia/Ricardo Augusto')
    ('Miséria', 'Arnaldo Antunes/Britto, SergioMiklos, Paulo')
    ('Moby Dick', 'John Bonham, John Paul Jones, Jimmy Page')
    ('Moby Dick', 'John Bonham/John Paul Jones')
    ('Mocidade', 'Domenil/J. Brito/Joaozinho/Rap, Marcelo Do')
    ('Mofo', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Molina', 'J.C. Fogerty')
    ('Momentos Que Marcam', 'Vários')
    ('Money', 'Berry Gordy, Jr./Janie Bradford')
    ('Money', 'Waters')
    ("Money's Too Tight To Mention", 'John and William Valentine')
    ('Monkey Wrench', 'Dave, Taylor, Nate, Chris')
    ('Montsegur', 'Bruce Dickinson/Janick Gers/Steve Harris')
    ('Moon Is Up', 'Jagger/Richards')
    ('Moon River', 'henry mancini/johnny mercer')
    ('Moon germs', 'Billy Cobham')
    ('Moonchild', 'Adrian Smith; Bruce Dickinson')
    ('Morning Dance', 'Jay Beckenstein')
    ('Morning Glory', 'J. Kay/Jay Kay')
    ('Most High', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Mother Russia', 'Steve Harris')
    ("Mother's Little Helper", 'Jagger/Richards')
    ('Motorbreath', 'James Hetfield')
    ('Mouth To Mouth', 'Bill Gould/Jon Hudson/Mike Bordin/Mike Patton')
    ('Move On', 'C. Cester/N. Cester')
    ('Mr Funk Samba', 'Vários')
    ('Mr. Cab Driver', 'Lenny Kravitz')
    ('Mr. Crowley', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Mr. Moon', 'Stuard Zender/Toby Smith')
    ('Muffin Man', 'Frank Zappa')
    ('Muita Bobeira', 'Luciana Souza')
    ('Murders In The Rue Morgue', 'Steve Harris')
    ('Murders In The Rue Morgue', 'Steve Harris')
    ('Music Of The Wind', 'Smith, Toby')
    ('Music for the Funeral of Queen Mary: VI. "Thou Knowest, Lord, the Secrets of Our Hearts"', 'Henry Purcell')
    ('Music for the Royal Fireworks, HWV351 (1749): La Réjouissance', 'George Frideric Handel')
    ('Muçulmano', 'Leão, Rodrigo F./Samuel Rosa')
    ('My Baby Left Me', 'J.C. Fogerty')
    ('My Bridges Burn', 'Billy Duffy/Ian Astbury')
    ('My Friend Of Misery', 'James Hetfield, Lars Ulrich and Jason Newsted')
    ('My Funny Valentine (Live)', 'Miles Davis')
    ('My Generation', 'John Entwistle/Pete Townshend')
    ('My Hero', 'Dave, Taylor, Nate, Chris')
    ('My Kind Of Town', 'jimmy van heusen/sammy cahn')
    ('My Love', 'Jauperi/Zeu Góes')
    ('My Lovely Man', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('My Melancholy Blues', 'Mercury')
    ('My Mistake', 'Billy Corgan')
    ('My Poor Brain', 'Dave, Taylor, Nate, Chris')
    ('My Ship', 'Ira Gershwin, Kurt Weill')
    ('My Time After Awhile', 'Robert Geddins/Ron Badger/Sheldon Feinberg')
    ('My Way', 'claude françois/gilles thibault/jacques revaux/paul anka')
    ('My World', 'W. Axl Rose')
    ('My World', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Mysterious Ways', 'U2')
    ('Música Ambiente', 'Renato Russo')
    ('Música De Trabalho', 'Renato Russo')
    ('Música No Ar', 'Tim Maia')
    ('Na Frente Da TV', 'Bino/Da Gama/Lazao/Ras Bernardo')
    ('Nabucco: Chorus, "Va, Pensiero, Sull\'ali Dorate"', 'Giuseppe Verdi')
    ('Naked In Front Of The Computer', 'Mike Patton')
    ('Naked In The Rain', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Naked Sunday', 'D. DeLeo/Kretz/R. DeLeo/Weiland')
    ('Naquele Dia', 'João Suplicy')
    ('Nasty Piece Of Work', 'jon lord/roger glover')
    ('Natália', 'Renato Russo')
    ('Navegar Impreciso', 'Herbert Vianna')
    ('Near Wild Heaven', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Nebulosa Do Amor', 'Herbert Vianna')
    ('Nefertiti', 'Miles Davis')
    ('Negative Creep', 'Kurt Cobain')
    ('Nem 5 Minutos Guardados', 'Titãs')
    ('Nem Um Dia', 'Djavan')
    ('Never Before', 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('New Faces', 'Jagger/Richards')
    ('New Frontier', 'Adrian Smith/Bruce Dickinson/Nicko McBrain')
    ('New Love', 'Tim Maia')
    ('New Rhumba', 'Miles Davis')
    ('New Rhumba', 'A. Jamal')
    ('New Test Leper', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('New Way Home', 'Dave, Taylor, Nate, Chris')
    ("New Year's Day", 'U2')
    ("New Year's Day", 'U2')
    ('New York', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('New York, New York', 'fred ebb/john kander')
    ('Neworld', 'Van Halen')
    ('Nice Guys Finish Last', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Nico', 'Billy Duffy/Ian Astbury')
    ('Night Flight', 'John Paul Jones/Robert Plant')
    ('Night Of The Long Knives', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Night Time Is The Right Time', 'J.C. Fogerty')
    ('Night Train', 'Jimmy Forrest/Lewis C. Simpkins/Oscar Washington')
    ('Nimrod (Adagio) from Variations On an Original Theme, Op. 36 "Enigma"', 'Edward Elgar')
    ('No Bone Movies', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('No Clima', 'Mônica Marianno')
    ('No Futuro', 'João Suplicy')
    ('No Good Without You', 'William "Mickey" Stevenson')
    ('No Memory', 'Dean Deleo')
    ('No More Lies', 'Steve Harris')
    ('No More Tears', 'J. Purdell, M. Inez, O. Osbourne, R. Castillo & Z. Wylde')
    ('No No No', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('No One Came', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('No Prayer For The Dying', 'Steve Harris')
    ('No Quarter', 'John Paul Jones')
    ('No Quarter', 'John Paul Jones/Robert Plant')
    ('No Remorse', 'James Hetfield, Lars Ulrich')
    ('No Such Thing', 'Chris Cornell')
    ('No Way Back', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ("Nobody Knows You When You're Down & Out", 'Jimmy Cox')
    ("Nobody's Fault But Mine", 'Jimmy Page/Robert Plant')
    ("Nobody's Home", 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord, Ian Paice')
    ('Noite Negra', 'Mônica Marianno')
    ('Norwegian Wood', 'John Lennon, Paul McCartney')
    ('Nos Bailes Da Vida', 'Milton Nascimento, Fernando Brant')
    ('Not The Doctor', 'Alanis Morissette & Glenn Ballard')
    ("Nothin' To Lose", 'Gene Simmons')
    ('Nothing Else Matters', 'Ulrich')
    ('Nothing To Say', 'Chris Cornell/Kim Thayil')
    ('Nothingman', 'Jeff Ament & Eddie Vedder')
    ("Now I'm Here", 'May, Brian')
    ("Now You're Gone", 'Vandenberg')
    ("Now's The Time", 'Miles Davis')
    ('Numb', 'U2; Edge, The')
    ('Não Sou Mais Disso', 'Jorge Aragão/Zeca Pagodinho')
    ('Não Vou Ficar', 'Tim Maia')
    ('Não Vou Lutar', 'Titãs')
    ('Não Vou Me Adaptar', 'Arnaldo Antunes')
    ('O Amor Daqui De Casa', 'Gilberto Gil')
    ('O Amor Nao Sabe Esperar', 'Herbert Vianna')
    ('O Cidadão Do Mundo', 'Chico Science')
    ('O Descobridor Dos Sete Mares', 'Gilson Mendonça/Michel')
    ('O Encontro De Isaac Asimov Com Santos Dumont No Céu', 'Chico Science')
    ('O Erê', 'Bernardo Vilhena/Bino Farias/Da Gama/Lazão/Toni Garrido')
    ('O Erê', 'Bernardo Vilhena/Bino/Da Gama/Lazao/Toni Garrido')
    ('O Livro Dos Dias', 'Renato Russo')
    ('O Pulso', 'Titãs')
    ('O Que Vai Em Meu Coração', 'Mônica Marianno')
    ('O Trem Da Juventude', 'Herbert Vianna')
    ('O Xote Das Meninas', 'Caetano Veloso e Gilberto Gil')
    ("OAM's Blues", 'Aaron Goldberg')
    ('Oceano', 'Djavan')
    ('Oceans', 'Jeff Ament/Stone Gossard')
    ('October Song', 'Matt Rowe & Stefan Skarbek')
    ('Odara', 'Caetano Veloso')
    ('Of Wolf And Man', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('Off He Goes', 'Eddie Vedder')
    ('Old Love', 'Eric Clapton, Robert Cray')
    ('Old School Hollywood', 'Dolmayan, John/Malakian, Daron/Odadjian, Shavo')
    ('On A Plain', 'Kurt Cobain')
    ('On Fire', 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('On Mercury', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('On The Mend', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('On The Run', 'Gilmour, Waters')
    ('On the Beautiful Blue Danube', 'Johann Strauss II')
    ('Once', 'Stone Gossard')
    ('Once', 'Van Halen')
    ('Onde Você Mora?', 'Marisa Monte/Nando Reis')
    ('Onde Você Mora?', 'Marisa Monte/Nando Reis')
    ('One', 'James Hetfield & Lars Ulrich')
    ('One', 'U2')
    ('One For The Road', 'E. Schrody/L. Dimant/L. Muggerud')
    ('One I Want', 'Van Halen')
    ("One Man's Meat", 'roger glover')
    ('One Minute Warning', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('One Step Beyond', 'Karsh Kale')
    ('One Step Closer', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('One Vision', 'Queen')
    ('Only A Dream In Rio', 'Vários')
    ('Only the Good Die Young', 'Bruce Dickinson; Harris')
    ('Orange Crush', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Original Of The Species', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Orion', 'K.Hammett')
    ('Os Cegos Do Castelo', 'Titãs')
    ('Os Exilados', 'Samuel Rosa')
    ('Otay', 'John Scofield, Robert Aries, Milton Chambers and Gary Grainger')
    ('Otherside', 'Red Hot Chili Peppers')
    ('Out Of Control', 'Jagger/Richards')
    ('Out Of Exile', 'Cornell, Commerford, Morello, Wilk')
    ('Out Of Sight', 'Ted Wright')
    ('Out Of Tears', 'Jagger/Richards')
    ('Out Of The Silent Planet', 'Bruce Dickinson/Janick Gers/Steve Harris')
    ('Out On The Tiles', 'Jimmy Page, Robert Plant, John Bonham')
    ('Outbreak', 'Jim Beard & Jon Herington')
    ('Outshined', 'Chris Cornell')
    ('Over Again', 'Tim Maia')
    ('Over And Out', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Over The Hills And Far Away', 'Jimmy Page/Jimmy Page & Robert Plant/Robert Plant')
    ('Overdose', 'AC/DC')
    ('Overdrive', 'Foo Fighters')
    ('Overkill', 'Clarke/Kilmister/Tayler')
    ('Ozone Baby', 'Jimmy Page, Robert Plant')
    ('Pagan Baby', 'J.C. Fogerty')
    ('Paint It Black', 'Jagger/Richards')
    ('Paint It Black', 'Keith Richards/Mick Jagger')
    ('Pais E Filhos', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Paisagem Na Janela', 'Lô Borges, Fernando Brant')
    ('Palavras', 'Titãs')
    ('Palco', 'Gilberto Gil')
    ('Palhas Do Coqueiro', 'Rodolfo')
    ('Panama', 'Edward Van Halen, Alex Van Halen, David Lee Roth')
    ('Panis Et Circenses', 'Caetano Veloso - Gilberto Gil')
    ('Panis Et Circenses', 'Caetano Veloso e Gilberto Gil')
    ("Papa's Got A Brand New Bag Pt.1", 'James Brown')
    ('Papeau Nuky Doe', 'Rodolfo')
    ('Papel Principal', 'Almir Guineto/Dedé Paraiso/Luverci Ernesto')
    ('Papelão', 'João Suplicy')
    ('Para Lennon E McCartney', 'Lô Borges, Márcio Borges, Fernando Brant')
    ('Parabolicamará', 'Gilberto Gil')
    ('Parachutes', 'Stone Gossard')
    ('Parallel Universe', 'Red Hot Chili Peppers')
    ('Paranoid', 'A. F. Iommi, W. Ward, T. Butler, J. Osbourne')
    ('Paris On Mine', 'Jon Herington')
    ('Partita in E Major, BWV 1006A: I. Prelude', 'Johann Sebastian Bach')
    ('Paschendale', 'Adrian Smith/Steve Harris')
    ('Paths Of Glory', 'Bill Gould/Jon Hudson/Mike Bordin/Mike Patton/Roddy Bottum')
    ('Pau-De-Arara', 'Guio De Morais E Seus "Parentes"/Luiz Gonzaga')
    ('Paula E Bebeto', 'Milton Nascimento, Caetano Veloso')
    ('Pavan, Lachrimae Antiquae', 'John Dowland')
    ('Peace On Earth', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Peer Gynt Suite No.1, Op.46: 1. Morning Mood', 'Edvard Grieg')
    ('Pensamento', 'Bino Farias/Da Gamma/Lazão/Rás Bernard')
    ('Pensamento', 'Bino/Da Gama/Ras Bernardo')
    ('Pererê', 'Augusto Conceição/Chiclete Com Banana')
    ('Perfect', 'Alanis Morissette & Glenn Ballard')
    ('Perfect', 'Billy Corgan')
    ('Perfect Circle', 'R.E.M.')
    ('Perfect Strangers', 'Richie Blackmore, Ian Gillian, Roger Glover')
    ('Perfeição', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Persuasion', 'Carlos Santana')
    ('Pescador de Ilusões', 'Macelo Yuka/O Rappa')
    ('Petits Machins (Little Stuff)', 'Miles Davis')
    ('Phantom Lord', 'James Hetfield, Lars Ulrich, Dave Mustaine')
    ('Phantom Of The Opera', 'Steve Harris')
    ('Phantom Of The Opera', 'Steve Harris')
    ('Piano Sonata No. 14 in C Sharp Minor, Op. 27, No. 2, "Moonlight": I. Adagio sostenuto', 'Ludwig van Beethoven')
    ('Pictures Of Home', 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('Pictures Of Lily', 'Pete Townshend')
    ('Piece Of Pie', 'R. DeLeo/Weiland')
    ('Pinball Wizard', 'John Entwistle/Pete Townshend')
    ('Plan B', 'Dean Brown, Dennis Chambers & Jim Beard')
    ('Planet Home', 'Jay Kay/Toby Smith')
    ('Plaster Caster', 'Gene Simmons')
    ('Plaster Caster', 'Gene Simmons')
    ('Play The Game', 'Mercury, Freddie')
    ('Play With Fire', 'Nanker Phelge')
    ('Please', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ("Please Don't Touch", 'Heath/Robinson')
    ('Please Mr. Postman', 'Brian Holland/Freddie Gorman/Georgia Dobbins/Robert Bateman/William Garrett')
    ('Please Please Please', 'James Brown/Johnny Terry')
    ('Please Read The Letter', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Plot 180', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Plush', 'R. DeLeo/Weiland')
    ('Poconé', 'Samuel Rosa')
    ('Pode Parar', 'Jorge Vercilo/Jota Maranhao')
    ('Podes Crer', 'Bino Farias/Da Gama/Lazão/Toni Garrido')
    ('Poison Eye', 'Chris Cornell')
    ('Polly', 'Kurt Cobain')
    ('Polly', 'Kurt Cobain')
    ('Polícia (Vinheta)', 'Titãs')
    ('Ponta de Areia', 'Milton Nascimento, Fernando Brant')
    ("Poofter's Froth Wyoming Plans Ahead", 'Frank Zappa')
    ('Poor Tom', 'Jimmy Page/Robert Plant')
    ('Poor Twisted Me', 'James Hetfield, Lars Ulrich')
    ('Pop Song 89', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Poprocks And Coke', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Por Merecer', 'João Suplicy')
    ('Por Você', 'Vários')
    ('Porcelain', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Porch', 'Eddie Vedder')
    ('Portela', 'Flavio Bororo/Paulo Apparicio/Wagner Alves/Zeca Sereno')
    ('Portia', 'Miles Davis')
    ('Posso Até Me Apaixonar', 'Dudu Nobre')
    ('Posso Perder Minha Mulher, Minha Mãe, Desde Que Eu Tenha O Rock And Roll', 'Arnaldo Baptista - Rita Lee - Arnolpho Lima Filho')
    ('Poundcake', 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, Sammy Hagar')
    ('Powerslave', 'Dickinson')
    ('Praise', 'Marvin Gaye')
    ('Prenda Minha', 'Tradicional')
    ('Preto Damião', 'Chico Amaral/Samuel Rosa')
    ('Pretty Baby', 'Willie Dixon')
    ('Pretty Noose', 'Chris Cornell')
    ('Pretty Persuasion', 'R.E.M.')
    ('Pretty Tied Up', "Izzy Stradlin'")
    ('Pride (In The Name Of Love)', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Pride (In The Name Of Love)', 'U2')
    ('Primal Scream', 'Mick Mars/Nikki Sixx/Tommy Lee/Vince Neil')
    ('Primary', 'Van Halen')
    ('Primavera', 'KC Porter & JB Eckl')
    ('Primavera', 'Genival Cassiano/Silvio Rochael')
    ('Prince Charming', 'Hetfield, Ulrich')
    ('Princess of the Dawn', 'Deaffy & R.A. Smith-Diesel')
    ('Pristina', 'Bill Gould/Mike Patton')
    ('Problem Child', 'AC/DC')
    ('Prodigal Son', 'Steve Harris')
    ('Prometheus Overture, Op. 43', 'Ludwig van Beethoven')
    ('Promises', 'Clapton/F.eldman/Linn')
    ('Proud Mary', 'J. C. Fogerty')
    ('Prowler', 'Steve Harris')
    ('Prowler', 'Steve Harris')
    ('Prá Dizer Adeus', 'Titãs')
    ('Pseudo Silk Kimono', 'Kelly, Mosley, Rothery, Trewaves')
    ('Psychopomp', 'The Tea Party')
    ('Psychopomp', 'The Tea Party')
    ('Public Enema Number One', 'Bruce Dickinson/David Murray')
    ('Pulse', 'The Tea Party')
    ('Pura Elegancia', 'João Suplicy')
    ('Purgatory', 'Steve Harris')
    ('Purify', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Purple Haze', 'Jimi Hendrix')
    ('Purple Stain', 'Red Hot Chili Peppers')
    ('Put On Your Shit Kickers', 'E. Schrody/L. Muggerud')
    ('Put The Finger On You', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Put You Down', 'Jerry Cantrell')
    ('Put Your Head Out', 'E. Schrody/L. Freese/L. Muggerud')
    ('Put Your Lights On', 'E. Shrody')
    ('Puteiro Em João Pessoa', 'Rodolfo')
    ('Quadrant', 'Billy Cobham')
    ('Quando Você Voltar', 'Renato Russo')
    ('Que País É Este', 'Renato Russo')
    ('Que País É Este', 'Renato Russo')
    ('Querem Meu Sangue', 'Titãs')
    ('Quest For Fire', 'Steve Harris')
    ('Question!', 'Tankian, Serj')
    ('Qui Nem Jiló', 'Humberto Teixeira/Luiz Gonzaga')
    ('Quilombo Groove [Instrumental]', 'Chico Science')
    ('Quintet for Horn, Violin, 2 Violas, and Cello in E Flat Major, K. 407/386c: III. Allegro', 'Wolfgang Amadeus Mozart')
    ('Radio Free Aurope', 'R.E.M.')
    ('Radio GA GA', 'Roger Taylor')
    ('Radio Song', 'C. Cester/C. Muncey/N. Cester')
    ('Radio Song', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Radio/Video', 'Dolmayan, John/Malakian, Daron/Odadjian, Shavo')
    ('Rag Doll', 'Steven Tyler, Joe Perry, Jim Vallance, Holly Knight')
    ('Rain Song', 'Robert Plant')
    ('Rainmaker', 'Bruce Dickinson/David Murray/Steve Harris')
    ('Ramble On', 'Jimmy Page, Robert Plant')
    ('Ramshackle Man', 'roger glover')
    ('Rasul', 'Jeremy Wall')
    ('Rats', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Razor', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Re-Align', 'Sully Erna')
    ('Real Love', 'Billy Corgan')
    ('Real Thing', 'Jerry Cantrell, Layne Staley')
    ('Realce', 'Gilberto Gil')
    ('Realidade Virtual', 'Bino Farias/Da Gama/Lazão/Toni Garrido')
    ('Realidade Virtual', 'Bino/Da Gamma/Lazao/Toni Garrido')
    ('Realword', 'Roy Z')
    ('Rearviewmirror', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Rebelião', 'Chico Amaral/Samuel Rosa')
    ('Reboladeira', 'Cal Adan/Ferrugem/Julinho Carioca/Tríona Ní Dhomhnaill')
    ('Red House', 'Jimi Hendrix')
    ('Red Light', 'U2')
    ('Red Mosquito', 'Jeff Ament & Stone Gossard & Jack Irons & Mike McCready & Eddie Vedder')
    ('Redundant', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Refazenda', 'Gilberto Gil')
    ('Reggae Tchan', 'Cal Adan/Del Rey, Tension/Edu Casanova')
    ('Release', 'Jeff Ament/Mike McCready/Stone Gossard')
    ('Release', 'The Tea Party')
    ('Release', 'The Tea Party')
    ('Releasing The Demons', 'Sully Erna')
    ('Relvelation (Mother Earth)', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Remedy', 'Chris Robinson/Rich Robinson')
    ('Remember', 'Jimi Hendrix')
    ('Remember Tomorrow', "Paul Di'Anno/Steve Harris")
    ('Remember Tomorrow', "Paul Di'Anno/Steve Harris")
    ('Remote Control', 'Joe Strummer/Mick Jones')
    ('Requiem, Op.48: 4. Pie Jesu', 'Gabriel Fauré')
    ('Resolve', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('Respectable', 'Jagger/Richards')
    ('Restless and Wild', 'F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman')
    ('Revelations', 'Dickinson')
    ('Revelations', 'Bruce Dickinson')
    ('Revenga', 'Tankian, Serj')
    ('Revolution 1993', 'Smith, Toby')
    ('Rhinocerous', 'Billy Corgan')
    ('Ricochet', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Ride The Lightning', 'Metallica')
    ('Right Now', 'Van Halen')
    ('Right On Time', 'Red Hot Chili Peppers')
    ('Right Through You', 'Alanis Morissette & Glenn Ballard')
    ('Rime of the Ancient Mariner', 'Harris')
    ('Rise', 'Billy Duffy/Ian Astbury')
    ('Rita Lee', 'Arnaldo Baptista/Rita Lee/Sérgio Dias')
    ('River Song', 'David Coverdale')
    ('Riviera Paradise', 'Stevie Ray Vaughan')
    ("Road Trippin'", 'Red Hot Chili Peppers')
    ('Roadrunner', 'Bo Diddley')
    ('Rock & Roll', 'Jimmy Page, Robert Plant, John Paul Jones, John Bonham')
    ('Rock & Roll', 'John Bonham/John Paul Jones/Robert Plant')
    ("Rock 'N' Roll Music", 'Chuck Berry')
    ('Rock And Roll All Nite', 'Paul Stanley, Gene Simmons')
    ('Rock And Roll All Nite', 'Paul Stanley, Gene Simmons')
    ('Rock And Roll Is Dead', 'Lenny Kravitz')
    ('Rock Bottom', 'Paul Stanley, Ace Frehley')
    ('Rock On', 'David Cook')
    ('Rock The Casbah', 'The Clash')
    ('Roll Call', 'Jim Beard')
    ("Rollin' And Tumblin'", 'McKinley Morgenfield (Muddy Waters)')
    ('Rollover D.J.', 'C. Cester/N. Cester')
    ('Ronnie', 'James Hetfield, Lars Ulrich')
    ("Rosa's Cantina", 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Roxanne', 'G M Sumner')
    ('Royal Orleans', 'John Bonham/John Paul Jones')
    ('Ruby Tuesday', 'Jagger/Richards')
    ('Rugas', 'Augusto Garcez/Nelson Cavaquinho')
    ('Run Silent Run Deep', 'Bruce Dickinson/Steve Harris')
    ('Run Through The Jungle', 'J. C. Fogerty')
    ('Run To The Hills', 'Harris')
    ('Run To The Hills', 'Steve Harris')
    ('Run To The Hilss', 'Steve Harris')
    ('Run to the Hills', 'Steve Harris')
    ("Runnin' With The Devil", 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ("Runnin' With The Devil", 'Edward Van Halen, Alex Van Halen, Michael Anthony and David Lee Roth')
    ('Running Free', "Paul Di'Anno/Steve Harris")
    ('Running Free', 'Harris/Di Anno')
    ('Running Free', "Paul Di'Anno/Steve Harris")
    ('Running On Faith', 'Jerry Lynn Williams')
    ('Rusty Cage', 'Chris Cornell')
    ('Réu Confesso', 'Tim Maia')
    ('Sabbra Cadabra', 'Black Sabbath')
    ('Saber Amar', 'Herbert Vianna')
    ('Sad But True', 'Apocalyptica')
    ('Sad But True', 'Ulrich')
    ('Sad Statue', 'Tankian, Serj')
    ('Safe and Sound', 'Chris Cornell')
    ('Saint Of Me', 'Jagger/Richards')
    ('Salgueiro', 'Augusto/Craig Negoescu/Rocco Filho/Saara, Ze Carlos Da')
    ('Salutations', 'E. Schrody/L. Dimant')
    ('Salve Nossa Senhora', 'Carlos Imperial/Edardo Araújo')
    ('Sam With The Showing Scalp Flat Top', 'Don Van Vliet')
    ('Samba Do Lado', 'Chico Science')
    ('Samba da Bençaco', 'Baden Powell/Vinicius de Moraes')
    ('Samba pras moças', 'Grazielle/Roque Ferreira')
    ('Sambassim (dj patife remix)', 'Alba Carvalho/Fernando Porto')
    ("Same Ol' Situation", 'Mick Mars/Nikki Sixx/Tommy Lee/Vince Neil')
    ('Samidarish [Instrumental]', 'Chico Science')
    ('Sampa', 'Gilberto Gil')
    ('Samurai', 'Djavan')
    ('San Francisco Bay Blues', 'Jesse Fuller')
    ('Sanctuary', "David Murray/Paul Di'Anno/Steve Harris")
    ('Sanctuary', "David Murray/Paul Di'Anno/Steve Harris")
    ('Sanctuary', "David Murray/Paul Di'Anno/Steve Harris")
    ('Sangrando', 'Gonzaga Jr/Gonzaguinha')
    ('Sangue De Bairro', 'Chico Science')
    ('Santana Jam', 'Carlos Santana')
    ('Santo Antonio', 'Vários')
    ('Sapopemba e Maxambomba', 'Nei Lopes/Wilson Moreira')
    ('Satisfaction', 'Jagger/Richards')
    ('Saturnine', 'Billy Corgan')
    ('Saudade Dos Aviões Da Panair (Conversando No Bar)', 'Milton Nascimento, Fernando Brant')
    ('Saudade Louca', 'Acyr Marques/Arlindo Cruz/Franco')
    ('Saudosismo', 'Caetano Veloso')
    ('Save Me', 'May, Brian')
    ('Save Me (Remix)', 'The Tea Party')
    ('Save The Children', 'Al Cleveland/Marvin Gaye/Renaldo Benson')
    ('Save You', 'Eddie Vedder/Jeff Ament/Matt Cameron/Mike McCready/Stone Gossard')
    ('Savior', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ("Say It Loud, I'm Black And I'm Proud Pt.1", 'Alfred Ellis/James Brown')
    ('Scam', 'Stuart Zender')
    ('Scar On the Sky', 'Chris Cornell')
    ('Scar Tissue', 'Red Hot Chili Peppers')
    ('Scentless Apprentice', 'Nirvana')
    ("Scheherazade, Op. 35: I. The Sea and Sindbad's Ship", 'Nikolai Rimsky-Korsakov')
    ('School', 'Kurt Cobain')
    ('Scratch-N-Sniff', 'Doyle Bramhall/Stevie Ray Vaughan')
    ('Sea Of Sorrow', 'Jerry Cantrell')
    ('Sea of Madness', 'Adrian Smith')
    ('Seconds', 'U2')
    ('Secrets', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('Seduzir', 'Djavan')
    ('See You', 'Dave, Taylor, Nate, Chris')
    ('See You Tonight', 'Gene Simmons')
    ('Seek & Destroy', 'James Hetfield, Lars Ulrich')
    ('Seek And You Shall Find', 'Ivy Hunter/William "Mickey" Stevenson')
    ('Segue O Seco', 'Caetano Veloso e Gilberto Gil')
    ('Selvagem', 'Bi Ribeiro/Herbert Vianna/João Barone')
    ('Sem Essa de Malandro Agulha', 'Aldir Blanc/Jayme Vignoli')
    ('Sem Terra', 'Samuel Rosa')
    ('Senhor Delegado/Eu Não Aguento', 'Antonio Lopes')
    ('Senhora E Senhor', 'Arnaldo Anutnes/Marcelo Fromer/Paulo Miklos')
    ('Serenity', 'Sully Erna; Tony Rombola')
    ('Serrado', 'Djavan')
    ('Será', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Set It Off', 'Audioslave/Chris Cornell')
    ('Set Me Free', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Set The Ray To Jerry', 'Billy Corgan')
    ('Seu Balancê', 'Paulinho Rezende/Toninho Geraes')
    ('Seven Seas Of Rhye', 'Mercury, Freddie')
    ('Seventh Son of a Seventh Son', 'Steve Harris')
    ('Severed Hand', 'Eddie Vedder')
    ('Sex Type Thing', 'D. DeLeo/Kretz/Weiland')
    ('Shadow on the Sun', 'Audioslave/Chris Cornell')
    ('Shamrocks And Shenanigans', 'E. Schrody/L. Dimant')
    ('Shamrocks And Shenanigans (Boom Shalock Lock Boom/Butch Vig Mix)', 'E. Schrody/L. Dimant')
    ('Shape The Sky', 'Billy Duffy/Ian Astbury')
    ('She', 'Gene Simmons, S. Coronel')
    ('She', 'Billie Joe Armstrong -Words Green Day -Music')
    ('She Give Me ...', 'David Coverdale')
    ('She Loves Me Not', 'Bill Gould/Mike Bordin/Mike Patton')
    ('She Suits Me To A Tee', 'Buddy Guy')
    ('She Talks To Angels', 'Chris Robinson/Rich Robinson')
    ('She Wears Black', 'G Harvey/R Hope-Taylor')
    ("She'll Never Be Your Man", 'Chris Cornell')
    ("She's A Rebel", 'Green Day')
    ('Sheer Heart Attack', 'Taylor')
    ('Shining In The Light', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Shiny Happy People', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Shock Me', 'Ace Frehley')
    ('Shoot Me Again', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Shoot You In The Back', 'Clarke/Kilmister/Taylor')
    ('Shotgun Blues', 'W. Axl Rose')
    ('Should I Stay Or Should I Go', 'The Clash')
    ('Shout At The Devil', 'Nikki Sixx')
    ('Shout It Out Loud', 'Paul Stanley, Gene Simmons, B. Ezrin')
    ('Show Me How to Live', 'Audioslave/Chris Cornell')
    ('Sick Again', 'Robert Plant')
    ('Sign Of The Cross', 'Steve Harris')
    ('Sign Of The Cross', 'Steve Harris')
    ('Signe', 'Eric Clapton')
    ('Silence the Voices', 'Chris Cornell')
    ('Silver And Gold', 'Bono')
    ('Silver And Gold', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Simples', 'Nelson Angelo')
    ('Sin', 'R. DeLeo/Weiland')
    ('Sina', 'Djavan')
    ("Since I've Been Loving You", 'John Paul Jones/Robert Plant')
    ("Since I've Been Loving You", 'Jimmy Page, Robert Plant, John Paul Jones')
    ('Sincero Breu', 'C. A./C.A./Celso Alvim/Herbert Vianna/Mário Moura/Pedro Luís/Sidon Silva')
    ('Sing Joyfully', 'William Byrd')
    ('Sir Psycho Sexy', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Sister Awake', 'The Tea Party')
    ('Sister Morphine', 'Faithfull/Jagger/Richards')
    ('Siva', 'Billy Corgan')
    ('Slave', 'David Coverdale/Earl Slick')
    ('Sleep On The Sidewalk', 'May')
    ('Slide It In', 'Coverdale')
    ('Slither', 'Hetfield, Ulrich, Hammett')
    ('Slither', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Sliver', 'Kurt Cobain')
    ("Slow An' Easy", 'Moody')
    ('Slow Dawn', 'Billy Corgan')
    ('Slow Down', 'Larry Williams')
    ('Slug', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Smells Like Teen Spirit', 'Nirvana')
    ('Smells Like Teen Spirit', 'Kurt Cobain')
    ('Smoke On The Water', 'Gillan/Glover/Lord/Paice')
    ('Smoke On The Water', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord, Ian Paice')
    ('Smoke On The Water', 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ("Smokin' in The Boys Room", 'Cub Coda/Michael Lutz')
    ('Smooth', 'M. Itaal Shur & Rob Thomas')
    ("Snoopy's search-Red baron", 'Billy Cobham')
    ('Snowballed', 'Angus Young, Malcolm Young, Brian Johnson')
    ('Snowblind', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('So Beautiful', 'Mick Hucknall')
    ('So Central Rain', 'R.E.M.')
    ('So Cruel', 'U2')
    ('So Fast, So Numb', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('So Fine', 'Duff McKagan')
    ('So What', 'Miles Davis')
    ('So What', 'Culmer/Exalt')
    ('Sobremesa', 'Chico Science')
    ('Solar', 'Milton Nascimento, Fernando Brant')
    ('Soldado Da Paz', 'Herbert Vianna')
    ('Soldier Of Fortune', 'D.Coverdale/R.Blackmore/Ritchie Blackmore')
    ('Soldier Side - Intro', 'Dolmayan, John/Malakian, Daron/Odadjian, Shavo')
    ('Solitaire', 'roger glover')
    ('Solo-Panhandler', 'Billy Cobham')
    ('Solomon HWV 67: The Arrival of the Queen of Sheba', 'George Frideric Handel')
    ('Some Days Are Better Than Others', 'U2; Bono')
    ('Some Kind Of Monster', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Somebody Stole My Guitar', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Somebody To Love', 'Mercury, Freddie')
    ('Someday My Prince Will Come', 'Miles Davis')
    ('Someday Never Comes', 'J. C. Fogerty')
    ("Somethin' Else", 'Bob Cochran/Sharon Sheeley')
    ('Something For Nothing', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Something Got Me Started', 'Mick Hucknall and Fritz McIntyre')
    ('Something In The Way', 'Kurt Cobain')
    ('Something Stupid', 'carson c. parks')
    ('Sometimes I Feel Like Screaming', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Sometimes Salvation', 'Chris Robinson/Rich Robinson')
    ("Sometimes You Can't Make It On Your Own", 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Sonata for Solo Violin: IV: Presto', 'Béla Bartók')
    ('Song For Lorraine', 'Jay Beckenstein')
    ('Sonifera Ilha', 'Branco Mello/Carlos Barmack/Ciro Pessoa/Marcelo Fromer/Toni Belloto')
    ('Sons Of Freedom', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Soon Forgotten', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Soot & Stars', 'Billy Corgan')
    ('Soul Education', 'Jay Kay/Toby Smith')
    ('Soul Kitchen', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('Soul Parsifal', 'Renato Russo - Marisa Monte')
    ('Soul Power (Live)', 'James Brown')
    ('Soul Sacrifice', 'Carlos Santana')
    ('Soul Singing', 'Chris Robinson/Rich Robinson')
    ('South Bound Saurez', 'John Paul Jones & Robert Plant')
    ('Sozinho', 'Peninha')
    ('Space Cowboy', 'J. Kay/Jay Kay')
    ("Space Truckin'", 'Blackmore/Gillan/Glover/Lord/Paice')
    ("Space Truckin'", 'Ian Gillan/Ian Paice/Jon Lord/Ritchie Blckmore/Roger Glover')
    ('Space Trucking', 'Richie Blackmore, Ian Gillian, Roger Glover, Jon Lord, Ian Paice')
    ('Spanish Eyes', 'U2')
    ('Spanish moss-"A sound portrait"-Spanish moss', 'Billy Cobham')
    ('Spank Thru', 'Kurt Cobain')
    ('Sparks Will Fly', 'Jagger/Richards')
    ('Sparrow', 'Billy Corgan')
    ('Speak To Me/Breathe', 'Mason/Waters, Gilmour, Wright')
    ('Spectacle', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Speed King', 'Blackmore, Gillan, Glover, Lord, Paice')
    ('Speed Of Light', 'Billy Duffy/Bob Rock/Ian Astbury')
    ('Spellbound', 'Angus Young, Malcolm Young, Brian Johnson')
    ("Spirit's in the Material World", 'G M Sumner')
    ('Spoonman', 'Chris Cornell')
    ('Spread Your Wings', 'Deacon')
    ('Springsville', 'J. Carisi')
    ('Springsville (Alternate Take)', 'J. Carisi')
    ('Squeeze Box', 'Pete Townshend')
    ('St. Anger', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('St. Jimmy', 'Green Day')
    ('St. Vitus Dance', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Stairway To Heaven', 'Robert Plant')
    ('Stairway To Heaven', 'Jimmy Page, Robert Plant')
    ('Stairway To Heaven', 'Robert Plant')
    ('Stand', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Stand By My Woman', 'Henry Kirssch/Lenny Kravitz/S. Pasch A. Krizan')
    ('Stand Inside Your Love', 'Billy Corgan')
    ('Star A.D.', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Starburst', 'Jeremy Wall')
    ('Staring At The Sun', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Stars', 'Mick Hucknall')
    ('Stay (Faraway, So Close!)', 'U2; Bono')
    ('Stay Away', 'Kurt Cobain')
    ('Steal Away (The Night)', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Still', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Still Life', 'David Murray/Steve Harris')
    ('Still Of The Night', 'Sykes')
    ('Stillness In Time', 'Toby Smith')
    ('Sting Me', 'Chris Robinson/Rich Robinson')
    ('Stone Cold Crazy', 'Deacon/May/Mercury/Taylor')
    ('Stone Crazy', 'Buddy Guy')
    ('Stone Dead Forever', 'Clarke/Kilmister/Tayler')
    ('Stone Free', 'Jimi Hendrix')
    ('Stormbringer', 'Coverdale')
    ('Stormbringer', 'D.Coverdale/R.Blackmore/Ritchie Blackmore')
    ('Straight Out Of Line', 'Sully Erna')
    ('Strange Brew', 'Clapton/Collins/Pappalardi')
    ('Strange Kind Of Woman', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('Stranger in a Strange Land', 'Adrian Smith')
    ('Strangers In The Night', 'berthold kaempfert/charles singleton/eddie snyder')
    ('Stratus', 'Billy Cobham')
    ('String Quartet No. 12 in C Minor, D. 703 "Quartettsatz": II. Andante - Allegro assai', 'Franz Schubert')
    ('Stripsearch', 'Jon Hudson/Mike Bordin/Mike Patton')
    ('Strutter', 'Paul Stanley, Gene Simmons')
    ("Stuck In A Moment You Can't Get Out Of", 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Stuck With Me', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Sua Impossivel Chance', 'Nando Reis')
    ('Substitute', 'Pete Townshend')
    ('Suck My Kiss', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Suck On The Jugular', 'Jagger/Richards')
    ('Sucker Train Blues', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Suicide Solution (With Guitar Solo)', 'O. Osbourne, R. Daisley, R. Rhoads')
    ('Suite No. 3 in D, BWV 1068: III. Gavotte I & II', 'Johann Sebastian Bach')
    ('Suite for Solo Cello No. 1 in G Major, BWV 1007: I. Prélude', 'Johann Sebastian Bach')
    ('Sul Da América', 'Samuel Rosa')
    ('Summer Love', 'hans bradtke/heinz meier/johnny mercer')
    ('Summertime', 'Miles Davis')
    ('Sun And Steel', 'Adrian Smith/Bruce Dickinson')
    ('Sunchild', 'Graham Harvey')
    ('Sunday Bloody Sunday', 'U2')
    ('Sunday Bloody Sunday', 'U2')
    ('Sunshine', 'Jerry Cantrell')
    ('Sunshine Of Your Love', 'Bruce/Clapton')
    ('Superhuman', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('Supernaut', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Supersonic', 'Jay Kay')
    ('Sure Know Something', 'Paul Stanley, Vincent Poncia')
    ('Sure Know Something', 'Paul Stanley, Vincent Poncia')
    ("Surprise! You're Dead!", 'Faith No More')
    ('Surrender', 'U2')
    ('Susie Q', 'Hawkins-Lewis-Broadwater')
    ('Suzie-Q, Pt. 2', 'J.C. Fogerty')
    ('Sweet Amber', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('Sweet Hitch-Hiker', 'J. C. Fogerty')
    ('Sweet Lady Luck', 'Vandenberg')
    ('Sweetest Thing', 'U2')
    ('Sweetest Thing', "U2 & Daragh O'Toole")
    ('Sweethearts Together', 'Jagger/Richards')
    ('Swing Low Sweet Chariot', 'Clapton/Trad. Arr. Clapton')
    ("Symphonie Fantastique, Op. 14: V. Songe d'une nuit du sabbat", 'Hector Berlioz')
    ('Symphony No. 104 in D Major "London": IV. Finale: Spiritoso', 'Franz Joseph Haydn')
    ('Symphony No. 2, Op. 16 -  "The Four Temperaments": II. Allegro Comodo e Flemmatico', 'Carl Nielsen')
    ('Symphony No. 2: III. Allegro vivace', 'Kurt Weill')
    ('Symphony No. 3 Op. 36 for Orchestra and Soprano "Symfonia Piesni Zalosnych" \\ Lento E Largo - Tranquillissimo', 'Henryk Górecki')
    ('Symphony No. 3 in E-flat major, Op. 55, "Eroica" - Scherzo: Allegro Vivace', 'Ludwig van Beethoven')
    ('Symphony No. 41 in C Major, K. 551, "Jupiter": IV. Molto allegro', 'Wolfgang Amadeus Mozart')
    ('Symphony No.1 in D Major, Op.25 "Classical", Allegro Con Brio', 'Sergei Prokofiev')
    ('Symphony No.5 in C Minor: I. Allegro con brio', 'Ludwig van Beethoven')
    ('Sábado A Noite', 'Lulu Santos')
    ('Sítio Do Pica-Pau Amarelo', 'Gilberto Gil')
    ('Só Se For Pelo Cabelo', 'Mônica Marianno')
    ('Só Tinha De Ser Com Você', 'Vários')
    ('Tailgunner', 'Bruce Dickinson/Steve Harris')
    ('Tailgunner', 'Bruce Dickinson/Steve Harris')
    ('Take It As It Comes', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('Take It Or Leave It', 'C. Muncey/N. Cester')
    ('Take The Power', 'Billy Duffy/Ian Astbury')
    ('Take This Bottle', 'Mike Bordin, Billy Gould, Mike Patton, Trey Spruance')
    ('Take the Box', 'Luke Smith')
    ('Talk About Love', 'roger glover')
    ('Talk About The Passion', 'R.E.M.')
    ('Talkin Loud and Saying Nothin', 'James Brown & Bobby Byrd')
    ("Talkin' 'Bout Women Obviously", 'Amos Blakemore/Buddy Guy')
    ('Tangerine', 'Jimmy Page')
    ('Tanto Tempo', 'Vários')
    ('Tapa Aqui, Descobre Ali', 'Paulo Levi/W. Rangel')
    ('Tarde Em Itapoã', 'Vários')
    ('Tea For One', 'Jimmy Page/Robert Plant')
    ('Tear', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Tears Dry On Their Own', 'Nickolas Ashford & Valerie Simpson')
    ('Tears In Heaven', 'Eric Clapton, Will Jennings')
    ('Televisão', 'Titãs')
    ('Tempo Perdido', 'Renato Russo')
    ('Tempo Rei', 'Gilberto Gil')
    ('Tempos Modernos', 'Lulu Santos')
    ('Temptation', 'The Tea Party')
    ('Temptation', 'The Tea Party')
    ('Tempus Fugit', 'Miles Davis')
    ('Ten Years Gone', 'Robert Plant')
    ('Tendo A Lua', 'Herbert Vianna/Tet Tillett')
    ('Tendo A Lua', 'Herbert Vianna/Tetê Tillet')
    ('Tenho Sede', 'Gilberto Gil')
    ('Tequila - Lourinha Bombril (Parate Y Mira)', 'Bahiano/Chuck Rio/Diego Blanco/Herbert Vianna')
    ('Terra', 'Caetano Veloso')
    ('Territorial Pissings', 'Kurt Cobain')
    ('Texarkana', 'Bill Berry/Michael Stipe/Mike Mills/Peter Buck')
    ('Texto "Verdade Tropical"', 'Caetano Veloso')
    ('Thank You', 'Robert Plant')
    ('Thank You', 'Jimmy Page, Robert Plant')
    ("That's Life", 'dean kay thompson/kelly gordon')
    ("That's The Way", 'Robert Plant')
    ("That's The Way", 'Jimmy Page, Robert Plant')
    ('The Aftermath', 'Blaze Bayley/Janick Gers/Steve Harris')
    ('The Alchemist', 'Roy Z')
    ('The Angel And The Gambler', 'Steve Harris')
    ('The Apparition', 'Janick Gers/Steve Harris')
    ('The Assassin', 'Steve Harris')
    ('The Aviator', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('The Awakening', 'Sully Erna')
    ('The Battle Of Evermore', 'Jimmy Page, Robert Plant')
    ('The Battle Rages On', 'ian paice/jon lord')
    ('The Bazaar', 'The Tea Party')
    ('The Best Is Yet To Come', 'carolyn leigh/cy coleman')
    ('The Call Of Ktulu', 'Metallica')
    ('The Call Up', 'The Clash')
    ('The Calling', 'Carlos Santana & C. Thompson')
    ('The Chase Is Better Than The Catch', 'Clarke/Kilmister/Taylor')
    ('The Clairvoyant', 'Steve Harris')
    ('The Clairvoyant', 'Adrian Smith; Bruce Dickinson; Steve Harris')
    ('The Clansman', 'Steve Harris')
    ('The Clansman', 'Steve Harris')
    ('The Crunge', 'John Bonham/John Paul Jones')
    ('The Crystal Ship', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('The Curse', 'Cornell, Commerford, Morello, Wilk')
    ('The Cut Runs Deep', 'Blackmore, Glover, Turner, Lord, Paice')
    ('The Day I Tried To Live', 'Chris Cornell')
    ('The Deeper The Love', 'Vandenberg')
    ('The Deepest Blues Are Black', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('The Duke', 'Dave Brubeck')
    ('The Edge Of Darkness', 'Blaze Bayley/Janick Gers/Steve Harris')
    ('The Educated Fool', 'Steve Harris')
    ('The End', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('The Everlasting Gaze', 'Billy Corgan')
    ('The Evil That Men Do', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('The Evil That Men Do', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('The Evil That Men Do', 'Adrian Smith; Bruce Dickinson; Steve Harris')
    ('The Fallen Angel', 'Adrian Smith/Steve Harris')
    ('The Finest Worksong', 'R.E.M.')
    ('The First Time', 'U2; Bono')
    ('The Fly', 'U2')
    ('The Four Horsemen', 'James Hetfield, Lars Ulrich, Dave Mustaine')
    ('The Frayed Ends Of Sanity', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('The Fugitive', 'Steve Harris')
    ('The Full Bug', 'Alex Van Halen/David Lee Roth/Edward Van Halen/Michael Anthony')
    ('The Gentle Art Of Making Enemies', 'Mike Bordin, Billy Gould, Mike Patton')
    ('The Girl From Ipanema', 'antonio carlos jobim/norman gimbel/vinicius de moraes')
    ('The Girl I Love She Got Long Black Wavy Hair', 'Jimmy Page/John Bonham/John Estes/John Paul Jones/Robert Plant')
    ('The God That Failed', 'Ulrich')
    ('The Great Gig In The Sky', 'Wright, Waters')
    ('The Greeting Song', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('The Gypsy', 'D.Coverdale/G.Hughes/Glenn Hughes/I.Paice/Ian Paice/J.Lord/John Lord/R.Blackmore/Ritchie Blackmore')
    ('The Hammer', 'Clarke/Kilmister/Taylor')
    ("The House Is Rockin'", 'Doyle Bramhall/Stevie Ray Vaughan')
    ('The House Jack Built', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('The Ides Of March', 'Steve Harris')
    ('The Invisible Man', 'Queen')
    ('The Kids', 'Toby Smith')
    ('The Lady Is A Tramp', 'lorenz hart/richard rodgers')
    ('The Last Remaining Light', 'Audioslave/Chris Cornell')
    ('The Last Song', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett')
    ('The Last Time', 'Jagger/Richards')
    ('The Last To Know', 'Mike Bordin, Billy Gould, Mike Patton')
    ('The Lemon Song', 'Jimmy Page, Robert Plant, John Paul Jones, John Bonham')
    ('The Loneliness of the Long Dis', 'Steve Harris')
    ('The Magnificent Seven', 'The Clash')
    ('The Maids Of Cadiz', 'L. Delibes')
    ('The Meaning Of The Blues', 'R. Troup, L. Worth')
    ('The Meaning Of The Blues/Lament (Alternate Take)', 'J.J. Johnson/R. Troup, L. Worth')
    ('The Memory Remains', 'Hetfield, Ulrich')
    ('The Mercenary', 'Janick Gers/Steve Harris')
    ('The Mercenary', 'Janick Gers/Steve Harris')
    ('The Messenger', 'Daniel Lanois')
    ('The Messiah: Behold, I Tell You a Mystery... The Trumpet Shall Sound', 'George Frideric Handel')
    ('The Midnight Special', 'J.C. Fogerty')
    ('The Miracle', 'Queen')
    ('The More I See', 'Molaney/Morris/Roberts/Wainwright')
    ('The Morning After', 'Faith No More')
    ('The Mule', 'Ritchie Blackmore, Ian Gillan, Roger Glover, Jon Lord, Ian Paice')
    ('The Nomad', 'David Murray/Steve Harris')
    ('The Number Of The Beast', 'Steve Harris')
    ('The Number Of The Beast', 'Harris')
    ('The Number Of The Beast', 'Steve Harris')
    ('The Number Of The Beast', 'Steve Harris')
    ('The Nutcracker, Op. 71a, Act II: Scene 14: Pas de deux: Dance of the Prince & the Sugar-Plum Fairy', 'Peter Ilyich Tchaikovsky')
    ('The Ocean', 'John Bonham/John Paul Jones')
    ('The One I Love', 'R.E.M.')
    ('The Other Side', 'Steven Tyler, Jim Vallance')
    ('The Outlaw Torn', 'James Hetfield, Lars Ulrich')
    ('The Pan Piper', 'Miles Davis')
    ('The Playboy Mansion', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('The Power Of Equality', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('The Prince', 'Harris/Tatler')
    ('The Prisoner', 'Adrian Smith/Steve Harris')
    ('The Prophecy', 'Dave Murray; Steve Harris')
    ('The Purpendicular Waltz', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('The Rain Song', 'Jimmy Page/Jimmy Page & Robert Plant/Robert Plant')
    ('The Real Thing', 'Faith No More')
    ('The Refugee', 'U2')
    ('The Right Thing', 'Mick Hucknall')
    ('The Righteous & The Wicked', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('The River (Remix)', 'The Tea Party')
    ('The Rover', 'Jimmy Page/Robert Plant')
    ('The Saint', 'Billy Duffy/Ian Astbury')
    ('The Seeker', 'Pete Townshend')
    ('The Shortest Straw', 'James Hetfield and Lars Ulrich')
    ('The Show Must Go On', 'Queen')
    ('The Small Hours', 'Holocaust')
    ('The Song Remains The Same', 'Jimmy Page/Jimmy Page & Robert Plant/Robert Plant')
    ('The Song Remains The Same', 'Robert Plant')
    ('The Spirit Of Radio', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('The Star Spangled Banner', 'Hendrix, Jimi')
    ('The Struggle Within', 'Ulrich')
    ('The Sun Road', 'Terry Bozzio, Steve Stevens, Tony Levin')
    ('The Temples Of Syrinx', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('The Thin Line Between Love & Hate', 'David Murray/Steve Harris')
    ('The Thing That Should Not Be', 'K.Hammett')
    ('The Three Sunrises', 'U2')
    ('The Tower', 'Roy Z')
    ('The Trees', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('The Trooper', 'Steve Harris')
    ('The Trooper', 'Harris')
    ('The Trooper', 'Steve Harris')
    ('The Trooper', 'Steve Harris')
    ('The Unbeliever', 'Janick Gers/Steve Harris')
    ('The Unforgettable Fire', 'U2')
    ('The Unforgiven', 'Apocalyptica')
    ('The Unforgiven', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('The Unforgiven II', 'Hetfield, Ulrich, Hammett')
    ('The Unnamed Feeling', 'Bob Rock/James Hetfield/Kirk Hammett/Lars Ulrich')
    ('The Unwritten Law', 'Richie Blackmore, Ian Gillian, Roger Glover, Ian Paice')
    ('The Wait', 'Killing Joke')
    ('The Wake-Up Bomb', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('The Wanderer', 'U2; Bono')
    ('The Wanton Song', 'Robert Plant')
    ('The Wicker Man', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('The Wicker Man', 'Adrian Smith/Bruce Dickinson/Steve Harris')
    ('The Wind Cries Mary', 'Jimi Hendrix')
    ('The Worm', 'Cornell, Commerford, Morello, Wilk')
    ('The Worst', 'Jagger/Richards')
    ('The Wrong Child', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('The Zephyr Song', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('The pleasant pheasant', 'Billy Cobham')
    ("Theme From Let's Go Native", 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Theme From The Swan', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ("They Can't Take That Away From Me", 'george gershwin/ira gershwin')
    ("They're Red Hot", 'Robert Johnson')
    ('Thick & Thin', 'Chris Robinson/Rich Robinson')
    ('Thief In The Night', 'De Beauport/Jagger/Richards')
    ('Think', 'Lowman Pauling')
    ("Thinking 'Bout Tomorrow", 'Fayyaz Virgi/Richard Bull')
    ('Third Stone From The Sun', 'Jimi Hendrix')
    ("This Cocaine Makes Me Feel Like I'm On This Song", 'Tankian, Serj')
    ('This Is Radio Clash', 'The Clash')
    ('This Is The Place', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ("This Time Around / Owed to 'G' [Instrumental]", 'Bolin/Hughes/Lord')
    ('This Velvet Glove', 'Red Hot Chili Peppers')
    ('Thorn Within', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('Thrill Me', 'Mick Hucknall and Fritz McIntyre')
    ('Through The Never', 'James Hetfield, Lars Ulrich and Kirk Hammett')
    ('Throw Away Your Television', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Thru And Thru', 'Jagger/Richards')
    ('Thumbing My Way', 'Eddie Vedder')
    ('Tightrope', 'Doyle Bramhall/Stevie Ray Vaughan')
    ('Tim Tim Por Tim Tim', 'Vários')
    ('Time', 'Mason, Waters, Wright, Gilmour')
    ('Time After Time', 'Miles Davis')
    ('Time Is On My Side', 'Jerry Ragavoy')
    ('Time To Kill', 'roger glover')
    ('Times Like These', 'Foo Fighters')
    ('Timothy', 'C. Cester')
    ('Tired Of You', 'Foo Fighters')
    ('Title Song', 'Chris Robinson/Rich Robinson')
    ('To Live Is To Die', 'James Hetfield, Lars Ulrich and Cliff Burton')
    ('To Tame A Land', 'Steve Harris')
    ('Toccata and Fugue in D Minor, BWV 565: I. Toccata', 'Johann Sebastian Bach')
    ('Toda Cor', 'Ciro Pressoa/Marcelo Fromer')
    ('Toda Menina Baiana', 'Gilberto Gil')
    ('Today', 'Billy Corgan')
    ('Tombstone Shadow', 'J.C. Fogerty')
    ('Tommy Gun', 'Joe Strummer/Mick Jones')
    ("Tomorrow's Dream", 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Tonight, Tonight', 'Billy Corgan')
    ('Too Fast For Love', 'Nikki Sixx')
    ('Too Late Too Late', 'Clarke/Kilmister/Tayler')
    ('Too Many Tears', 'Adrian Vanderberg/David Coverdale')
    ('Too Many Ways (Alternate)', 'Willie Dixon')
    ('Too Much Is Not Enough', 'Turner, Held, Greenwood')
    ('Too Young To Die', 'Smith, Toby')
    ("Top O' The Morning To Ya", 'E. Schrody/L. Dimant')
    ('Top Top', 'Os Mutantes - Arnolpho Lima Filho')
    ("Tourette's", 'Kurt Cobain')
    ('Trac Trac', 'Fito Paez/Herbert Vianna')
    ('Tradição', 'Adalto Magalha/Lourenco')
    ('Train In Vain', 'Joe Strummer/Mick Jones')
    ('Trampled Under Foot', 'John Paul Jones')
    ('Transmission', 'The Tea Party')
    ('Transylvania', 'Steve Harris')
    ('Trapped Under Ice', 'Metallica')
    ('Trash, Trampoline And The Party Girl', 'U2')
    ('Trastevere', 'Milton Nascimento, Ronaldo Bastos')
    ("Travelin' Band", 'J. C. Fogerty')
    ('Travelling Riverside Blues', 'Jimmy Page/Robert Johnson/Robert Plant')
    ('Travis Walk', 'Stevie Ray Vaughan')
    ('TriboTchan', 'Cal Adan/Paulo Levi')
    ('True Believers', 'Billy Duffy/Ian Astbury')
    ('Trupets Of Jericho', 'Roy Z')
    ('Truth Hurts', 'Blackmore, Glover, Turner')
    ("Tryin' To Throw Your Arms Around The World", 'U2')
    ('Três Lados', 'Chico Amaral/Samuel Rosa')
    ("Tuesday's Gone", 'Collins/Van Zandt')
    ('Tuiuti', 'Claudio Martins/David Lima/Kleber Rodrigues/Livre, Cesare Som')
    ('Turandot, Act III, Nessun dorma!', 'Giacomo Puccini')
    ('Turn The Page', 'Seger')
    ('Turn You Inside-Out', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Twentienth Century Fox', 'Robby Krieger, Ray Manzarek, John Densmore, Jim Morrison')
    ('Twice As Hard', 'Chris Robinson/Rich Robinson')
    ('Twist And Shout', 'Bert Russell/Phil Medley')
    ('Two Fanfares for Orchestra: II. Short Ride in a Fast Machine', 'John Adams')
    ('Two Hearts Beat As One', 'U2')
    ('Ty Cobb', 'Ben Shepherd/Chris Cornell')
    ('Tão Seu', 'Samuel Rosa')
    ('Ugly In The Morning', 'Mike Bordin, Billy Gould, Mike Patton')
    ('Ultraviolet (Light My Way)', 'U2')
    ('Um Amor Puro', 'Djavan')
    ('Um Amor, Um Lugar', 'Herbert Vianna')
    ('Um Dia Qualquer', 'Samuel Rosa')
    ('Um Gosto De Sol', 'Milton Nascimento, Ronaldo Bastos')
    ('Um Jantar Pra Dois', 'Vários')
    ('Um Passeio No Mundo Livre', 'Chico Science')
    ('Um Satélite Na Cabeça', 'Chico Science')
    ('Uma Brasileira', 'Carlinhos Brown/Herbert Vianna')
    ('Unchained', 'Edward Van Halen, Alex Van Halen, David Lee Roth, Michael Anthony')
    ('Unchained Melody', 'Alex North/Hy Zaret')
    ('Under My Thumb', 'Jagger/Richards')
    ('Under Pressure', 'Queen & David Bowie')
    ('Under The Bridge', 'Anthony Kiedis/Chad Smith/Flea/John Frusciante')
    ('Under The Sun/Every Day Comes and Goes', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Undertow', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Underwater Love', 'Faith No More')
    ('Unemployable', 'Matt Cameron & Mike McCready')
    ('Unidos Da Tijuca', 'Douglas/Neves, Vicente Das/Silva, Gilmar L./Toninho Gentil/Wantuir')
    ('United Colours', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Universally Speaking', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('União Da Ilha', 'Dito/Djalma Falcao/Ilha, Almir Da/Márcio André')
    ('Uns Dias', 'Herbert Vianna')
    ('Until It Sleeps', 'James Hetfield, Lars Ulrich')
    ('Until The End Of The World', 'U2')
    ('Untitled', 'Pearl Jam')
    ('Untitled', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Up Around The Bend', 'J. C. Fogerty')
    ('Up In Arms', 'Dave, Taylor, Nate, Chris')
    ('Upon A Golden Horse', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Us And Them', 'Waters, Wright')
    ('Vai Adiar', 'Alcino Corrêa/Monarco')
    ('Vai Valer', 'Herbert Vianna')
    ('Vamo Batê Lata', 'Herbert Vianna')
    ("Van Diemen's Land", 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('Vavoom : Ted The Mechanic', 'Ian Gillan, Roger Glover, Jon Lord, Steve Morse, Ian Paice')
    ('Venice Queen', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Vento No Litoral', 'Dado Villa-Lobos/Marcelo Bonfá')
    ('Verdade', 'Carlinhos Santana/Nelson Rufino')
    ('Vertigo', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Vida Boa', 'Fausto Nilo - Armandinho')
    ('Vida De Cachorro', 'Rita Lee - Arnaldo Baptista - Sérgio Baptista')
    ('Violent Pornography', 'Dolmayan, John/Malakian, Daron/Odadjian, Shavo')
    ('Viradouro', 'Dadinho/Gilbreto Gomes/Gustavo/P.C. Portugal/R. Mocoto')
    ('Virginia Moon', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('Vivo Isolado Do Mundo', 'Alcides Dias Lopes')
    ('Voce Inteira', 'João Suplicy')
    ('Você Fugiu', 'Genival Cassiano')
    ('Vulcão Dub - Fui Eu', 'Bi Ribeira/Herbert Vianna/João Barone')
    ('Vôo Sobre o Horizonte', 'J.r.Bertami/Parana')
    ('W.M.A.', 'Dave Abbruzzese/Eddie Vedder/Jeff Ament/Mike McCready/Stone Gossard')
    ('Wainting On A Friend', 'Jagger/Richards')
    ('Waiting', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Waiting', 'Billy Corgan')
    ('Waiting On A Sign', 'The Tea Party')
    ('Wake Me Up When September Ends', 'Mike Dint, Billie Joe, Tré Cool')
    ('Wake Up', 'Alanis Morissette & Glenn Ballard')
    ('Wake Up Alone', "Paul O'duffy")
    ('Wake Up Dead Man', 'Bono, The Edge, Adam Clayton, and Larry Mullen')
    ('Walk On', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Walk On Water', 'Steven Tyler, Joe Perry, Jack Blades, Tommy Shaw')
    ('Walk To The Water', 'U2')
    ("Walkin'", 'Miles Davis')
    ("Walkin' Blues", 'Robert Johnson')
    ('Walking After You', 'Dave Grohl')
    ('Walking Contradiction', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Walking Into Clarksdale', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('Walking On The Water', 'J.C. Fogerty')
    ('Walking Wounded', 'The Tea Party')
    ('Walking on the Moon', 'G M Sumner')
    ('Wall Of Denial', 'Doyle Bramhall/Stevie Ray Vaughan')
    ("Walter's Walk", 'Jimmy Page, Robert Plant')
    ('War (The Process)', 'Billy Duffy/Ian Astbury')
    ('War Pigs', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('Warm Tape', 'Anthony Kiedis, Flea, John Frusciante, and Chad Smith')
    ('Warning', 'Billie Joe Armstrong -Words Green Day -Music')
    ('Wasted My Hate', 'James Hetfield, Lars Ulrich, Kirk Hammett')
    ('Wasted Reprise', 'Stone Gossard')
    ('Wasted Years', 'Adrian Smith')
    ('Wasting Love', 'Bruce Dickinson/Janick Gers')
    ('Wasting Love', 'Bruce Dickinson/Janick Gers')
    ('Waterhole (Expresso Bongo)', 'Kelly, Mosley, Rothery, Trewaves')
    ('Wave (Vou te Contar)', 'Antonio Carlos Jobim')
    ('We Are The Champions', 'Mercury, Freddie')
    ('We Are The Champions', 'Mercury')
    ('We Die Young', 'Jerry Cantrell')
    ('We Will Rock You', 'Deacon, John/May, Brian')
    ('We Will Rock You', 'May')
    ("We're Gonna Groove", 'Ben E.King/James Bethea')
    ('Wearing And Tearing', 'Jimmy Page, Robert Plant')
    ('Weekend Warrior', 'Janick Gers/Steve Harris')
    ('Welcome Home (Sanitarium)', 'Apocalyptica')
    ('Welcome Home (Sanitarium)', 'K.Hammett')
    ('Welcome To Paradise', 'Billie Joe Armstrong -Words Green Day -Music')
    ("Wellington's Victory or the Battle Symphony, Op.91: 2. Symphony of Triumph", 'Ludwig van Beethoven')
    ('Were Do We Go From Here', 'Jay Kay')
    ('Wet My Bed', 'R. DeLeo/Weiland')
    ('What A Day', 'Mike Bordin, Billy Gould, Mike Patton')
    ('What If I Do?', 'Dave Grohl, Taylor Hawkins, Nate Mendel, Chris Shiflett/FOO FIGHTERS')
    ('What Is And What Should Never Be', 'Jimmy Page, Robert Plant')
    ('What Is It About Men', 'Delroy "Chris" Cooper, Donovan Jackson, Earl Chinna Smith, Felix Howard, Gordon Williams, Luke Smith, Paul Watson & Wilburn Squiddley Cole')
    ('What It Takes', 'Steven Tyler, Joe Perry, Desmond Child')
    ('What Now My Love', 'carl sigman/gilbert becaud/pierre leroyer')
    ('What You Are', 'Audioslave/Chris Cornell')
    ('What is and Should Never Be', 'Jimmy Page/Robert Plant')
    ("Whatever It Is, I Just Can't Stop", 'Jay Kay/Kay, Jay')
    ('Whatsername', 'Green Day')
    ('Wheels Of Confusion / The Straightener', 'Tony Iommi, Bill Ward, Geezer Butler, Ozzy Osbourne')
    ('When I Come Around', 'Billie Joe Armstrong -Words Green Day -Music')
    ('When I Had Your Love', 'Robert Rogers/Warren "Pete" Moore/William "Mickey" Stevenson')
    ('When I Look At The World', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('When I Was A Child', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ("When It's Love", 'Edward Van Halen, Alex Van Halen, Michael Anthony,/Edward Van Halen, Alex Van Halen, Michael Anthony, Sammy Hagar')
    ('When Love Comes To Town', 'Bono/Clayton, Adam/Mullen Jr., Larry/The Edge')
    ('When Love Comes To Town', 'U2')
    ('When My Left Eye Jumps', 'Al Perkins/Willie Dixon')
    ('When The Levee Breaks', 'Jimmy Page, Robert Plant, John Paul Jones, John Bonham, Memphis Minnie')
    ('When The World Was Young', 'Jimmy Page, Robert Plant, Charlie Jones, Michael Lee')
    ('When Two Worlds Collide', 'Blaze Bayley/David Murray/Steve Harris')
    ('When You Gonna Learn (Digeridoo)', 'Jay Kay/Kay, Jay')
    ('Where Eagles Dare', 'Steve Harris')
    ('Where Eagles Dare', 'Steve Harris')
    ('Where Have All The Good Times Gone?', 'Ray Davies')
    ('Where The River Goes', 'D. DeLeo/Kretz/Weiland')
    ('Where The Streets Have No Name', 'U2')
    ('Where The Wild Things Are', 'Hetfield, Ulrich, Newsted')
    ('Wherever I May Roam', 'Apocalyptica')
    ('Wherever I May Roam', 'Ulrich')
    ('Wherever You May Go', 'David Coverdale')
    ('Whiplash', 'James Hetfield, Lars Ulrich')
    ('Whiskey In The Jar', 'Traditional')
    ('White Feather', 'Kelly, Mosley, Rothery, Trewaves')
    ('White Riot', 'Joe Strummer/Mick Jones')
    ('White Room', 'Bruce/Clapton')
    ('Who Are You (Single Edit Version)', 'John Entwistle/Pete Townshend')
    ('Who Needs You', 'Deacon')
    ('Who Wants To Live Forever', 'Brian May')
    ("Who'll Stop The Rain", 'J. C. Fogerty')
    ("Who's Gonna Ride Your Wild Horses", 'U2')
    ('Whole Lotta Love', 'Jimmy Page/John Bonham/John Paul Jones/Robert Plant/Willie Dixon')
    ('Whole Lotta Love', 'Jimmy Page, Robert Plant, John Paul Jones, John Bonham')
    ('Whole Lotta Love', 'John Bonham/John Paul Jones/Robert Plant/Willie Dixon')
    ('Whole Lotta Love (Medley)', 'Arthur Crudup/Bernard Besman/Bukka White/Doc Pomus/John Bonham/John Lee Hooker/John Paul Jones/Mort Shuman/Robert Plant/Willie Dixon')
    ('Whole Lotta Rosie', 'AC/DC')
    ("Why Can't This Be Love", 'Van Halen')
    ('Why Go', 'Jeff Ament')
    ('Wicked Garden', 'D. DeLeo/R. DeLeo/Weiland')
    ('Wicked Ways', 'Blackmore, Glover, Turner, Lord, Paice')
    ('Wild Honey', 'Adam Clayton, Bono, Larry Mullen, The Edge')
    ('Wild Side', 'Nikki Sixx/Tommy Lee/Vince Neil')
    ('Wildest Dreams', 'Adrian Smith/Steve Harris')
    ('Wind Up', 'Dave, Taylor, Nate, Chris')
    ('Winterlong', 'Billy Corgan')
    ('Wiser Time', 'Chris Robinson/Rich Robinson')
    ('Wishing It Was', 'Eale-Eye Cherry, M. Simpson, J. King & M. Nishita')
    ('With Or Without You', 'U2')
    ('Without You', 'Mick Mars/Nikki Sixx')
    ('Without You', 'Van Halen')
    ('Women In Uniform', 'Greg Macainsh')
    ("Won't Get Fooled Again (Full Length Version)", 'John Entwistle/Pete Townshend')
    ('Wonderful Tonight', 'Clapton')
    ('Woodpecker From Mars', 'Faith No More')
    ('World Leader Pretend', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('World Wide Suicide', 'Eddie Vedder')
    ('Wrapped Around Your Finger', 'G M Sumner')
    ('Wrathchild', 'Steve Harris')
    ('Wrathchild', 'Steve Harris')
    ('Wrathchild', 'Steve Harris')
    ('Wrathchild', 'Steve Harris')
    ('Wrote A Song For Everyone', 'J.C. Fogerty')
    ('Xanadu', 'Geddy Lee And Alex Lifeson/Geddy Lee And Neil Peart/Rush')
    ('Yahweh', 'Adam Clayton, Bono, Larry Mullen & The Edge')
    ('Year to the Day', 'Van Halen')
    ('Yesterday To Tomorrow', 'Cornell, Commerford, Morello, Wilk')
    ('Yesterdays', 'Billy/Del James/W. Axl Rose/West Arkeen')
    ('You Are', 'Matt Cameron')
    ('You Are The Everything', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('You Better You Bet', 'Pete Townshend')
    ("You Can't Do it Right (With the One You Love)", 'D.Coverdale/G.Hughes/Glenn Hughes/R.Blackmore/Ritchie Blackmore')
    ('You Could Be Mine', "Izzy Stradlin'/W. Axl Rose")
    ('You Fool No One', 'Coverdale/Lord/Paice')
    ('You Fool No One (Alternate Version)', 'Blackmore/Coverdale/Lord/Paice')
    ('You Got Me Rocking', 'Jagger/Richards')
    ('You Got Me Rocking', 'Jagger/Richards')
    ('You Got No Right', 'Dave Kushner, Duff, Matt Sorum, Scott Weiland & Slash')
    ('You Keep On Moving', 'Coverdale/Hughes')
    ('You Know My Name', 'Chris Cornell')
    ('You Learn', 'Alanis Morissette & Glenn Ballard')
    ('You Oughta Know', 'Alanis Morissette & Glenn Ballard')
    ('You Oughta Know (Alternate)', 'Alanis Morissette & Glenn Ballard')
    ('You Really Got Me', 'Ray Davies')
    ('You Shook Me', 'J B Lenoir/Willie Dixon')
    ('You Shook Me', 'J. B. Lenoir/Willie Dixon')
    ('You Shook Me(2)', 'J B Lenoir/Willie Dixon')
    ('You Sure Love To Ball', 'Marvin Gaye')
    ("You're Gonna Break My Hart Again", 'Sykes')
    ("You're My Best Friend", 'Deacon, John')
    ("You're What's Happening (In The World Today)", 'Allen Story/George Gordy/Robert Gordy')
    ("You've Been A Long Time Coming", 'Brian Holland/Eddie Holland/Lamont Dozier')
    ("You've Got It", 'Mick Hucknall and Lamont Dozier')
    ('Your Blue Room', 'Brian Eno, Bono, Adam Clayton, The Edge & Larry Mullen Jnr.')
    ('Your Mirror', 'Mick Hucknall')
    ('Your Soul Today', 'Chris Cornell')
    ('Your Time Has Come', 'Cornell, Commerford, Morello, Wilk')
    ('Your Time Is Gonna Come', 'Jimmy Page/John Paul Jones')
    ('Your Time Is Gonna Come', 'Page, Jones')
    ('Zero', 'Billy Corgan')
    ('Zither', 'Bill Berry-Peter Buck-Mike Mills-Michael Stipe')
    ('Zombie Eaters', 'Faith No More')
    ('Zoo Station', 'U2')
    ('Zooropa', 'U2; Bono')
    ('Zé Trindade', 'Samuel Rosa')
    ('[Untitled]', 'Billy Corgan')
    ('À Vontade (Live Mix)', 'Bombom/Ed Motta')
    ('Água E Fogo', 'Chico Amaral/Edgard Scandurra/Samuel Rosa')
    ('Água de Beber', 'Antonio Carlos Jobim/Vinicius de Moraes')
    ('É Fogo', 'Mônica Marianno')
    ('É Preciso Saber Viver', 'Erasmo Carlos/Roberto Carlos')
    ('É Uma Partida De Futebol', 'Samuel Rosa')
    ('É que Nessa Encarnação Eu Nasci Manga', 'Lucina/Luli')
    ('Último Pau-De-Arara', 'Corumbá/José Gumarães/Venancio')



```python
sql = """
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Name like ? || '%'
ORDER BY 
    Name;
"""
```


```python
# Name like 'As%'
rows = db.select_many_rows(db_file, sql, ('As',))
```


```python
print(rows[:5])
```

    [('As Aparências Enganam', None), ('As Dores do Mundo', 'Hyldon'), ('As Pegadas Do Amor', 'Gilberto Gil'), ('As Profecias', None), ('As Rosas Não Falam (Beth Carvalho)', None)]



```python
sql = """
SELECT 
    EmployeeId, FirstName, LastName, Title
FROM
    employees
WHERE 
    EmployeeId in (?, ?, ?);
"""
ids = (1, 5, 8)
```


```python
rows = db.select_many_rows(db_file, sql, ids)
```


```python
print(rows)
```

    [(1, 'Andrew', 'Adams', 'General Manager'), (5, 'Steve', 'Johnson', 'Sales Support Agent'), (8, 'Laura', 'Callahan', 'IT Specialist')]


## Work with datetime


```python
query = """
    SELECT FirstName, LastName, BirthDate 
    FROM Employees; 
"""
```


```python
rows = db.select_many_rows(db_file, query, ())
```


```python
print(rows)
```

    [('Andrew', 'Adams', '1962-02-18 00:00:00'), ('Nancy', 'Edwards', '1958-12-08 00:00:00'), ('Jane', 'Peacock', '1973-08-29 00:00:00'), ('Margaret', 'Park', '1947-09-19 00:00:00'), ('Steve', 'Johnson', '1965-03-03 00:00:00'), ('Michael', 'Mitchell', '1973-07-01 00:00:00'), ('Robert', 'King', '1970-05-29 00:00:00'), ('Laura', 'Callahan', '1968-01-09 00:00:00'), ('Doe', 'John', '1990-01-01 00:00:00')]



```python
for row in rows:
    print(row[2])
```

    1962-02-18 00:00:00
    1958-12-08 00:00:00
    1973-08-29 00:00:00
    1947-09-19 00:00:00
    1965-03-03 00:00:00
    1973-07-01 00:00:00
    1970-05-29 00:00:00
    1968-01-09 00:00:00
    1990-01-01 00:00:00



```python
from datetime import datetime
```


```python
help(datetime)
```

    Help on class datetime in module datetime:
    
    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |      The optional argument timespec specifies the number of additional terms
     |      of the time to include. Valid options are 'auto', 'hours', 'minutes',
     |      'seconds', 'milliseconds' and 'microseconds'.
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  fromisoformat(...) from builtins.type
     |      string -> datetime from datetime.isoformat() output
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  isocalendar(...)
     |      Return a named tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from date:
     |  
     |  fromisocalendar(...) from builtins.type
     |      int, int, int -> Construct a date from the ISO year, week number and weekday.
     |      
     |      This is the inverse of the date.isocalendar() function
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    



```python
# format: Y - 4 digits year, y for 2 digit year 
for row in rows:
    dob = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
    print(f'{row[0]} {row[1]} was born on {dob.month}/{dob.day}/{dob.year}')
```

    Andrew Adams was born on 2/18/1962
    Nancy Edwards was born on 12/8/1958
    Jane Peacock was born on 8/29/1973
    Margaret Park was born on 9/19/1947
    Steve Johnson was born on 3/3/1965
    Michael Mitchell was born on 7/1/1973
    Robert King was born on 5/29/1970
    Laura Callahan was born on 1/9/1968
    Doe John was born on 1/1/1990



```python

```
