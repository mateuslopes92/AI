# Indexes

-- Index (BTree data structure)
-- Indexes are used to find values within a specific column more quickly
-- MySQL normally searches sequentially through a column
-- The longer the column, the more expensive operation is
-- UPDATE takes more time, SELECT takes less time

To see the indexes that a table have:
```
SHOW INDEXES FROM customers;
```

To create a index (use the most used value on searchs)
```
CREATE INDEX last_name_idx
ON customers(last_name);
```

Searching after create the indexes the search speed up
```
SELECT * FROM customers
WHERE last_name = "Kajol";
```

We can create a multi column index
```
CREATE INDEX last_name_first_name_idx
ON customers(last_name, first_name);
```

To drop a index can simply:
```
ALTER TABLE customers
DROP INDEX last_name_idx;
```

Search with the multi column index (will get the speed benefit)
```
SELECT * FROM customers
WHERE last_name = "Kajol" and first_name = "Poppy";
```