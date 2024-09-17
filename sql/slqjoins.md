# SQL JOINS

By default the join is a inner join

```
SELECT
  movies.movie_id, title, budget, revenue, currency, unit
FROM movies
JOIN financials
ON movies.movie_id=financials.movie_id
```
or
```
SELECT
  movies.movie_id, title, budget, revenue, currency, unit
FROM movies m
JOIN financials f
ON m.movie_id=f.movie_id
```

## LEFT JOIN(LEFT OUTER JOIN)
```
SELECT
  m.movie_id, title, budget, revenue, currency, unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id=f.movie_id
```

## RIGHT JOIN(RIGHT OUTER JOIN)
```
SELECT
  f.movie_id, title, budget, revenue, currency, unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id=f.movie_id
```

## UNION (FULL JOIN)
```
SELECT
  m.movie_id, title, budget, revenue, currency, unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id=f.movie_id

UNION

SELECT
  f.movie_id, title, budget, revenue, currency, unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id=f.movie_id
```