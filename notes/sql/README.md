# Some SQL notes

I just finished the Codeacadamy SQL course. Wanted to write some things down here:



### 1) table manipulation, querying tables 

* ``SELECT  * FROM celebs`` 
  * this gets all info from the table ``celebs``
* ``INSERT INTO tablename (col ids) VALUES (record values)``
  * insert new row into talbe
* ``SELCT col id FROM tablename;``
  * get column for col id
* Note that results from a ``SELECT`` statement are special tables called a **result set**
* ``UPDATE tablename SET colname1 = x WHERE colname2 = y;``
  * edit rows
* ``ALTER TABLE celebs ADD COLUMN handle TEXT``
  * modify table, add col (automatically populated with NULL)
* ``DELETE FROM celebs WHERE handle IS x;``
  * delete rows matching x in requested col
* ``SELECT col1, col2, ... FROM tablename'``
  * get requested cols from table
* ``SELECT DISTINCT col FROM table;``
  * ``DISTINCT`` filters out dups from result set
* ``SELECT row FROM table WHERE conditional``
  * filter result set by condition. e.g. conditional is ``rowname > 8``
* ``WHERE row LIKE regex-ish``
  * filter result set by regex-type thingy. supports ``_`` (used for ``.``) and ``%`` (``.*``)
* ``LIKE`` is **NOT** case sensitive
* ``BETWEEN low AND high``
  * conditional that tests low \le x \le high
* ``AND`` combines conditionals for ``WHERE`` clause
* ``OR`` same as ^ but does or
* ``ORDER BY colname DESC``
  * sort result set by col name descending (>)
* ``LIMIT x``
  * limit num rows in result set to x
  
### 2) Aggregation
* ``SELECT COUNT(*) FROM fake_apps``
  * count num rows.
  * ``COUNT(*)`` counts num rows in column
* ``SEELCT price, COUNT(*) FROM fake_apps GROUP BY price``
  * count num apps at each price
* ```SELECT price, COUNT(*) FROM fake_apps```  
     ``WHERE downloads > 20000``  
     ``GROUP BY price;``
  * count num apps at each price w 20k+ downloads
* ``SELECT category, SUM(downloads) FROM fake_apps``  
  ``GROUP BY category;``
  * sum downloads for each **category**
* ``SELECT name, category, MAX(downloads) FROM fake_apps``  
  ``GROUP BY category``
  * max downloaded app for each category
* ``MIN()`` is a thing too
* ``SELECT price, AVG(downloads) FROM fake_apps``  
  ``GROUP BY price;``
  * avg num dl for each price
* ``ROUND(variable, percision)`` is a thing too

### 3) Multiple tables
* ``CREATE TABLE artsits (id INTEGER PRIMARY KEY, name TEXT);``
  * creates tale ``artsist``
  * ``PRIMARY KEY``: SQL ensures inuque, non-nul values
* a **foreign key** is a col that contains the primary key of another table in the db
  * foreign keys don't need to be unique and can be null
  * e.g. ``artist_id`` field in an ``albums`` table could point to the primary keys of this ``artists`` table
* ``SELECT albums.name, albums.year, artists.name FROM albums, artists``
  * **CROSS JOIN**: select rows from multiple tables for your result set
  * this query is n^2: combines every row of ``albums`` w every row of ``artists``
* ``SELECT * FROM albums``  
  ``INNER JOIN artists ON albums.artist_id = artist.id;``
  * **INNER JOIN** combines rows where join condition is true.
  * this statment gets all the fields from both tables (``SELECT *``)
* ``SELECT * FROM albums``  
  ``LEFT OUTER JOIN artists ON albums.artist_id = artists.id``
  * **LEFT OUTER JOIN** gets every row in left table (first mentioned, ``albums`` in this case) for the result set. 
  * if join condition not met, NULL is used to populate cols from right table
* ``SELECT albums.name AS 'album', albums.year, albums.name AS 'artist'``  
  ``FROM albums``  
  ``JOIN ON albums.artist_id = artists.id``  
  ``WHERE albums.year > 1980;``  
  * ``AS`` lets you rename cols/tables with an **alias** of your choice
  * alias only appears in result set - doesn't change preexisting tables
  * result set has column names "album" (instead of "name"), "year", "artist" (instead of "name"). It only contains records with a year > 1980
