# Basic SQL queries revision study

## Select
To select all columns from a database
SELECT * FROM movies;

To select specific columns from a database
SELECT title, industry FROM movies;

To select with clauses
SELECT * FROM movies WHERE industry="Hollywood";

To count how many items in a query:
SELECT COUNT(*) FROM movies WHERE industry="Hollywood";

To select distinct values in a column
```
SELECT distinct industry FROM movies;
```

To select with string contains
```
SELECT * FROM movies WHERE title LIKE "%THOR%";
```

To select with conditions (AND, OR)
```
SELECT * FROM movies WHERE rating>=6 AND rating<=8;
```
or
```
SELECT * FROM movies WHERE rating BETWEEN 6 AND 8;
```

Can use IN
```
SELECT * FROM movies WHERE release_year IN (2022, 2019, 2018);
```
Using NULL:
```
SELECT * FROM movies WHERE rating is NULL;
SELECT * FROM movies WHERE rating is NOT NULL;
```

Ordering:
```
SELECT * FROM movies WHERE industry="Hollywood" ORDER BY rating;
SELECT * FROM movies WHERE industry="Hollywood" ORDER BY rating ASC;
SELECT * FROM movies WHERE industry="Hollywood" ORDER BY rating DESC;
```

Limiting:
```
SELECT * FROM movies WHERE industry="Hollywood" ORDER BY rating LIMIT 5;
```

Offset (offset is number of items to be skiped):
```
SELECT * FROM movies WHERE industry="Hollywood" ORDER BY rating LIMIT 5 OFFSET 1;
```

## Funcs for analytics
```
SELECT MAX(rating) FROM movies WHERE industry="hollywood";
SELECT MIN(rating) FROM movies WHERE industry="hollywood";
```

```
SELECT AVG(rating) FROM movies WHERE studio="marvel";
SELECT ROUND(AVG(rating), 2) FROM movies WHERE studio="marvel"; with 2 decimal points
```

```
SELECT ROUND(AVG(rating), 2) as average FROM movies WHERE studio="marvel"; renaming the result to average
```

```
SELECT industry, COUNT(*) FROM movies GROUP BY industry; to count for each industry
```

```
SELECT industry, COUNT(*) as count FROM movies GROUP BY industry ORDER BY count DESC; to count for each industry and order
```

```
SELECT *, YEAR(CURDATE())-birth_year as age FROM actors;
```

```
SELECT *, (revenue-budget) as profit FROM financials;
```

```
SELECT *,
  IF(currency='USD', revenue*77, revenue) as revenue_inr
FROM financials;
```

To get which units are used on the table (millions, billions, thousands)
```
SELECT distinct unit FROM financials;
```

To convert all values in one single unit(millions)
```
SELECT *,
  CASE
    WHEN unit="thousands" THEN revenue/1000
    WHEN unit="billions" THEN revenue*1000
    WHEN unit="millions" THEN revenue
  END as revenue_mln
FROM financials;
```