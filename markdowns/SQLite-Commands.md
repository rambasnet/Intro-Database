# SQLite DB Installation and Command Line Tools

## Download and Install Tools

- go to the official download page: https://sqlite.org/download.html
- download the appropriate version based-on your Operating System and platform
- E.g., on Windows, download: [sqlite-tools-win32-x86-3420000.zip](https://sqlite.org/2023/sqlite-tools-win32-x86-3420000.zip)
- unzip/extract binary files to some folder of your choice
    - Users/<your name>/sqlite-tools is a good place
- add the path to the extracted binary files to your system environemnt
    - Windows users follow these instructions: https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/
    - Mac/Linux users follow these instructions: https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/
    
## GUI DB Tools

- download and install DBeaver Community - https://dbeaver.io/download/
- install the driver and sample SQLite database file
    
## Chinook Database
- https://github.com/lerocha/chinook-database
- it represents a digital media store, including tables for artists, albums, media tracks, invoices, and customers
- can be used to test and demo various databases
- chinook.sqlite database file is provided in data folder of Intro-Database repository

## Run SQLite Command line tool

- open a Terminal on Mac/Linux or Command Prompt on Windows
- type sqlite3 command
    - if you get sqlite3 not found error, add path to the file to your system environment path following the instructions above
    - here's how it looks on my MacBook Pro:

```bash
(base) ╭─rbasnet@M-rbasnetMBP ~ 
╰─$ sqlite3                                                                                    127 ↵
SQLite version 3.39.3 2022-09-05 11:02:23
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> 
```

### useful commands:
    - .help
    - .quit
    - .open <SQLITEDB_FILENAME>
    - .database


###  Connect to an SQLite db file

```bash
$ sqlite3 <db file path/name>
```

- download SQLite Sample Database - https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
- unzip the db file and open it using sqlite3 commands as shown below

```bash
(base) ╭─rbasnet@M-rbasnetMBP ~ 
╰─$ sqlite3 ~/Downloads/chinook.db 
SQLite version 3.39.3 2022-09-05 11:02:23
Enter ".help" for usage hints.
sqlite> .tables
albums          employees       invoices        playlists     
artists         genres          media_types     tracks        
customers       invoice_items   playlist_track
sqlite> .quit
```

- open db file using .open command
- must provide absolute path to the file

```bash
$ sqlite3
sqlite> .open DB_FILEPATH/NAME
```

### Show tables in DB file

- .tables

```bash
(base) ╭─rbasnet@M-rbasnetMBP ~ 
╰─$ sqlite3 ~/Downloads/chinook.db
SQLite version 3.39.3 2022-09-05 11:02:23
Enter ".help" for usage hints.
sqlite> .tables
albums          employees       invoices        playlists     
artists         genres          media_types     tracks        
customers       invoice_items   playlist_track
sqlite> 

```

### Show the structure of a table

- .schema <tablename>
    
```bash
sqlite> .schema employees
CREATE TABLE IF NOT EXISTS "employees"
(
    [EmployeeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [FirstName] NVARCHAR(20)  NOT NULL,
    [Title] NVARCHAR(30),
    [ReportsTo] INTEGER,
    [BirthDate] DATETIME,
    [HireDate] DATETIME,
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60),
    FOREIGN KEY ([ReportsTo]) REFERENCES "employees" ([EmployeeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE INDEX [IFK_EmployeeReportsTo] ON "employees" ([ReportsTo]);
sqlite> 
```

### use pattern to list tables
- show all the tables ending with **es**
- .table '%es'
    
### Show indexes
    
    - .indexes
- show the indexes of a specific table
    - .indexes albums
- show indexes whose names end with 'es'
    - .indexes %es
    - quotes are optional
    
### Save the result of a query to a file
- use `.output [FILENAME]` command
    - all the results of the subsequent queries will be saved to the file specified
- the following commands select title from the albums table and write the result to the albums.txt files
    
```bash
sqlite> .output albums.txt
sqlite> SELECT title from albums;

```
    
- let's check the contents of the file albums.txt file
- .output without file name will write the output to the console


```python
! cat ~/albums.txt
```

    For Those About To Rock We Salute You
    Balls to the Wall
    Restless and Wild
    Let There Be Rock
    Big Ones
    Jagged Little Pill
    Facelift
    Warner 25 Anos
    Plays Metallica By Four Cellos
    Audioslave
    Out Of Exile
    BackBeat Soundtrack
    The Best Of Billy Cobham
    Alcohol Fueled Brewtality Live! [Disc 1]
    Alcohol Fueled Brewtality Live! [Disc 2]
    Black Sabbath
    Black Sabbath Vol. 4 (Remaster)
    Body Count
    Chemical Wedding
    The Best Of Buddy Guy - The Millenium Collection
    Prenda Minha
    Sozinho Remix Ao Vivo
    Minha Historia
    Afrociberdelia
    Da Lama Ao Caos
    Acústico MTV [Live]
    Cidade Negra - Hits
    Na Pista
    Axé Bahia 2001
    BBC Sessions [Disc 1] [Live]
    Bongo Fury
    Carnaval 2001
    Chill: Brazil (Disc 1)
    Chill: Brazil (Disc 2)
    Garage Inc. (Disc 1)
    Greatest Hits II
    Greatest Kiss
    Heart of the Night
    International Superhits
    Into The Light
    Meus Momentos
    Minha História
    MK III The Final Concerts [Disc 1]
    Physical Graffiti [Disc 1]
    Sambas De Enredo 2001
    Supernatural
    The Best of Ed Motta
    The Essential Miles Davis [Disc 1]
    The Essential Miles Davis [Disc 2]
    The Final Concerts (Disc 2)
    Up An' Atom
    Vinícius De Moraes - Sem Limite
    Vozes do MPB
    Chronicle, Vol. 1
    Chronicle, Vol. 2
    Cássia Eller - Coleção Sem Limite [Disc 2]
    Cássia Eller - Sem Limite [Disc 1]
    Come Taste The Band
    Deep Purple In Rock
    Fireball
    Knocking at Your Back Door: The Best Of Deep Purple in the 80's
    Machine Head
    Purpendicular
    Slaves And Masters
    Stormbringer
    The Battle Rages On
    Vault: Def Leppard's Greatest Hits
    Outbreak
    Djavan Ao Vivo - Vol. 02
    Djavan Ao Vivo - Vol. 1
    Elis Regina-Minha História
    The Cream Of Clapton
    Unplugged
    Album Of The Year
    Angel Dust
    King For A Day Fool For A Lifetime
    The Real Thing
    Deixa Entrar
    In Your Honor [Disc 1]
    In Your Honor [Disc 2]
    One By One
    The Colour And The Shape
    My Way: The Best Of Frank Sinatra [Disc 1]
    Roda De Funk
    As Canções de Eu Tu Eles
    Quanta Gente Veio Ver (Live)
    Quanta Gente Veio ver--Bônus De Carnaval
    Faceless
    American Idiot
    Appetite for Destruction
    Use Your Illusion I
    Use Your Illusion II
    Blue Moods
    A Matter of Life and Death
    A Real Dead One
    A Real Live One
    Brave New World
    Dance Of Death
    Fear Of The Dark
    Iron Maiden
    Killers
    Live After Death
    Live At Donington 1992 (Disc 1)
    Live At Donington 1992 (Disc 2)
    No Prayer For The Dying
    Piece Of Mind
    Powerslave
    Rock In Rio [CD1]
    Rock In Rio [CD2]
    Seventh Son of a Seventh Son
    Somewhere in Time
    The Number of The Beast
    The X Factor
    Virtual XI
    Sex Machine
    Emergency On Planet Earth
    Synkronized
    The Return Of The Space Cowboy
    Get Born
    Are You Experienced?
    Surfing with the Alien (Remastered)
    Jorge Ben Jor 25 Anos
    Jota Quest-1995
    Cafezinho
    Living After Midnight
    Unplugged [Live]
    BBC Sessions [Disc 2] [Live]
    Coda
    Houses Of The Holy
    In Through The Out Door
    IV
    Led Zeppelin I
    Led Zeppelin II
    Led Zeppelin III
    Physical Graffiti [Disc 2]
    Presence
    The Song Remains The Same (Disc 1)
    The Song Remains The Same (Disc 2)
    A TempestadeTempestade Ou O Livro Dos Dias
    Mais Do Mesmo
    Greatest Hits
    Lulu Santos - RCA 100 Anos De Música - Álbum 01
    Lulu Santos - RCA 100 Anos De Música - Álbum 02
    Misplaced Childhood
    Barulhinho Bom
    Seek And Shall Find: More Of The Best (1963-1981)
    The Best Of Men At Work
    Black Album
    Garage Inc. (Disc 2)
    Kill 'Em All
    Load
    Master Of Puppets
    ReLoad
    Ride The Lightning
    St. Anger
    ...And Justice For All
    Miles Ahead
    Milton Nascimento Ao Vivo
    Minas
    Ace Of Spades
    Demorou...
    Motley Crue Greatest Hits
    From The Muddy Banks Of The Wishkah [Live]
    Nevermind
    Compositores
    Olodum
    Acústico MTV
    Arquivo II
    Arquivo Os Paralamas Do Sucesso
    Bark at the Moon (Remastered)
    Blizzard of Ozz
    Diary of a Madman (Remastered)
    No More Tears (Remastered)
    Tribute
    Walking Into Clarksdale
    Original Soundtracks 1
    The Beast Live
    Live On Two Legs [Live]
    Pearl Jam
    Riot Act
    Ten
    Vs.
    Dark Side Of The Moon
    Os Cães Ladram Mas A Caravana Não Pára
    Greatest Hits I
    News Of The World
    Out Of Time
    Green
    New Adventures In Hi-Fi
    The Best Of R.E.M.: The IRS Years
    Cesta Básica
    Raul Seixas
    Blood Sugar Sex Magik
    By The Way
    Californication
    Retrospective I (1974-1980)
    Santana - As Years Go By
    Santana Live
    Maquinarama
    O Samba Poconé
    Judas 0: B-Sides and Rarities
    Rotten Apples: Greatest Hits
    A-Sides
    Morning Dance
    In Step
    Core
    Mezmerize
    [1997] Black Light Syndrome
    Live [Disc 1]
    Live [Disc 2]
    The Singles
    Beyond Good And Evil
    Pure Cult: The Best Of The Cult (For Rockers, Ravers, Lovers & Sinners) [UK]
    The Doors
    The Police Greatest Hits
    Hot Rocks, 1964-1971 (Disc 1)
    No Security
    Voodoo Lounge
    Tangents
    Transmission
    My Generation - The Very Best Of The Who
    Serie Sem Limite (Disc 1)
    Serie Sem Limite (Disc 2)
    Acústico
    Volume Dois
    Battlestar Galactica: The Story So Far
    Battlestar Galactica, Season 3
    Heroes, Season 1
    Lost, Season 3
    Lost, Season 1
    Lost, Season 2
    Achtung Baby
    All That You Can't Leave Behind
    B-Sides 1980-1990
    How To Dismantle An Atomic Bomb
    Pop
    Rattle And Hum
    The Best Of 1980-1990
    War
    Zooropa
    UB40 The Best Of - Volume Two [UK]
    Diver Down
    The Best Of Van Halen, Vol. I
    Van Halen
    Van Halen III
    Contraband
    Vinicius De Moraes
    Ao Vivo [IMPORT]
    The Office, Season 1
    The Office, Season 2
    The Office, Season 3
    Un-Led-Ed
    Battlestar Galactica (Classic), Season 1
    Aquaman
    Instant Karma: The Amnesty International Campaign to Save Darfur
    Speak of the Devil
    20th Century Masters - The Millennium Collection: The Best of Scorpions
    House of Pain
    Radio Brasil (O Som da Jovem Vanguarda) - Seleccao de Henrique Amaro
    Cake: B-Sides and Rarities
    LOST, Season 4
    Quiet Songs
    Muso Ko
    Realize
    Every Kind of Light
    Duos II
    Worlds
    The Best of Beethoven
    Temple of the Dog
    Carry On
    Revelations
    Adorate Deum: Gregorian Chant from the Proper of the Mass
    Allegri: Miserere
    Pachelbel: Canon & Gigue
    Vivaldi: The Four Seasons
    Bach: Violin Concertos
    Bach: Goldberg Variations
    Bach: The Cello Suites
    Handel: The Messiah (Highlights)
    The World of Classical Favourites
    Sir Neville Marriner: A Celebration
    Mozart: Wind Concertos
    Haydn: Symphonies 99 - 104
    Beethoven: Symhonies Nos. 5 & 6
    A Soprano Inspired
    Great Opera Choruses
    Wagner: Favourite Overtures
    Fauré: Requiem, Ravel: Pavane & Others
    Tchaikovsky: The Nutcracker
    The Last Night of the Proms
    Puccini: Madama Butterfly - Highlights
    Holst: The Planets, Op. 32 & Vaughan Williams: Fantasies
    Pavarotti's Opera Made Easy
    Great Performances - Barber's Adagio and Other Romantic Favorites for Strings
    Carmina Burana
    A Copland Celebration, Vol. I
    Bach: Toccata & Fugue in D Minor
    Prokofiev: Symphony No.1
    Scheherazade
    Bach: The Brandenburg Concertos
    Chopin: Piano Concertos Nos. 1 & 2
    Mascagni: Cavalleria Rusticana
    Sibelius: Finlandia
    Beethoven Piano Sonatas: Moonlight & Pastorale
    Great Recordings of the Century - Mahler: Das Lied von der Erde
    Elgar: Cello Concerto & Vaughan Williams: Fantasias
    Adams, John: The Chairman Dances
    Tchaikovsky: 1812 Festival Overture, Op.49, Capriccio Italien & Beethoven: Wellington's Victory
    Palestrina: Missa Papae Marcelli & Allegri: Miserere
    Prokofiev: Romeo & Juliet
    Strauss: Waltzes
    Berlioz: Symphonie Fantastique
    Bizet: Carmen Highlights
    English Renaissance
    Handel: Music for the Royal Fireworks (Original Version 1749)
    Grieg: Peer Gynt Suites & Sibelius: Pelléas et Mélisande
    Mozart Gala: Famous Arias
    SCRIABIN: Vers la flamme
    Armada: Music from the Courts of England and Spain
    Mozart: Symphonies Nos. 40 & 41
    Back to Black
    Frank
    Carried to Dust (Bonus Track Version)
    Beethoven: Symphony No. 6 'Pastoral' Etc.
    Bartok: Violin & Viola Concertos
    Mendelssohn: A Midsummer Night's Dream
    Bach: Orchestral Suites Nos. 1 - 4
    Charpentier: Divertissements, Airs & Concerts
    South American Getaway
    Górecki: Symphony No. 3
    Purcell: The Fairy Queen
    The Ultimate Relexation Album
    Purcell: Music for the Queen Mary
    Weill: The Seven Deadly Sins
    J.S. Bach: Chaconne, Suite in E Minor, Partita in E Major & Prelude, Fugue and Allegro
    Prokofiev: Symphony No.5 & Stravinksy: Le Sacre Du Printemps
    Szymanowski: Piano Works, Vol. 1
    Nielsen: The Six Symphonies
    Great Recordings of the Century: Paganini's 24 Caprices
    Liszt - 12 Études D'Execution Transcendante
    Great Recordings of the Century - Shubert: Schwanengesang, 4 Lieder
    Locatelli: Concertos for Violin, Strings and Continuo, Vol. 3
    Respighi:Pines of Rome
    Schubert: The Late String Quartets & String Quintet (3 CD's)
    Monteverdi: L'Orfeo
    Mozart: Chamber Music
    Koyaanisqatsi (Soundtrack from the Motion Picture)


### Execute SQL statements from a file
- create a file commands.sql
- open it using .read [COMMAND_FILE]

- type the following content:

```txt
SELECT albumid, title
FROM albums
ORDER BY title
LIMIT 10;
```
- run the following

```bash
sqlite> .mode column
sqlite> .header on
sqlite> .read /Users/rbasnet/projects/Intro-Database/command.sql

AlbumId  Title                                                       
-------  ------------------------------------------------------------
156      ...And Justice For All                                      
257      20th Century Masters - The Millennium Collection: The Best o
         f Scorpions                                                 
296      A Copland Celebration, Vol. I                               
94       A Matter of Life and Death                                  
95       A Real Dead One                                             
96       A Real Live One                                             
285      A Soprano Inspired                                          
139      A TempestadeTempestade Ou O Livro Dos Dias                  
203      A-Sides                                                     
160      Ace Of Spades                                               
sqlite> 
```




```python

```
