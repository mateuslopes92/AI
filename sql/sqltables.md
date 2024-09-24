# TABLES

## Creating Table
```
CREATE TABLE employee (
  employee_id INT NOT NULL,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  age INT,
  gender VARCHAR(50),
  birth_date DATE,
  PRIMARY KEY (employee_id)
);
```

## Inserting Data
```
INSERT INTO employee (employee_id, first_name, last_name, age, gender, birth_date)
VALUES (1, 'Mateus', 'Lopes', 28, 'Male', '1996-03-27')
```

# Creating stored procedure
This is how can create procedures to be reused, the procedures are saved on left menu of workbench
```
CREATE PROCEDURE large_salaries()
SELECT *
FROM employee_salary
WHERE salary > 50000;
```

to use the procedure
```
CALL large_salaries();
```