show databases;

use finalproject;

show tables;

CREATE TABLE authors
(
	author_name VARCHAR(255) NOT NULL,
    book_name VARCHAR(255) NOT NULL
    );
    
CREATE TABLE books
(
	book_name VARCHAR(255) NOT NULL,
    sold_copies INT);
    
INSERT INTO authors (author_name, book_name) VALUES
("author_1", "book_1"),
("author_1", "book_2"),
("author_2", "book_3"),
("author_2", "book_4"),
("author_2", "book_5"),
("author_3", "book_6");

SELECT * FROM books;

INSERT INTO books (sold_copies, book_name) VALUES
(1000, "book_1"),
(1500, "book_2"),
(34000, "book_3"),
(29000, "book_4"),
(40000, "book_5"),
(4400, "book_6");


SELECT author_name, sold_copies FROM authors a
LEFT JOIN books b on a.book_name = b.book_name
ORDER BY sold_copies ASC;

SELECT author_name, SUM(sold_copies) FROM authors a
LEFT JOIN books b on a.book_name = b.book_name;

#######################
### 1.	Create an SQL query that shows the TOP 3 authors who sold the least books in total.
### Answer No 1 

SELECT author_name, SUM(sold_copies) as total_sold FROM authors a
LEFT JOIN books b on a.book_name = b.book_name
GROUP BY author_name
ORDER BY total_sold ASC
LIMIT 3;


######################
#### 2. Write an SQL query to find out how many users inserted more than 2000 
#### but less than 4000 images in their presentations!

CREATE TABLE event_log
(
	user_id INT NOT NULL,
    event_date_time INT NOT NULL
    );
    
SHOW TABLES;
SELECT * FROM event_log;

INSERT INTO event_log (user_id, event_date_time) VALUES
(7494212, 1535308430),
(7494212, 1535308433),
(1475185, 1535308444),
(6946725, 1535308475),
(6946725, 1535308476),
(6946725, 1535308477);

SELECT * FROM event_log;

### Answer No 2

-- 
-- (SELECT 
--         user_id, COUNT(event_date_time) AS times_inserted
--     FROM
--         event_log
--     GROUP BY user_id
--     HAVING (COUNT(event_date_time) < 3
--         AND COUNT(event_date_time) >= 1));
-- 

SELECT 
    COUNT(user_id)
FROM
    (SELECT 
        user_id, COUNT(event_date_time) AS times_inserted
    FROM
        event_log
    GROUP BY user_id
    HAVING (COUNT(event_date_time) < 3
        AND COUNT(event_date_time) >= 1)) AS T;

--  2000< x <4000; --> REAL CONDITION


######################
#### 3. Print every department where the average salary per employee is over than 500$

#JOIN by employee_id, GROUP by department_name
#WHERE avg(salary) >500

CREATE TABLE employees
(
	department_name VARCHAR(30),
    employee_id INT NOT NULL PRIMARY KEY,
    employee_name VARCHAR(255)
    );
    
select * from employees;

CREATE TABLE salaries
(
	salary INT,
    employee_id INT NOT NULL PRIMARY KEY,
    employee_name VARCHAR(255)
    );
    
select * from salaries;

INSERT INTO employees (department_name, employee_id, employee_name) 
VALUES
("Sales", 123, "John Doe"),
("Sales", 211, "Jane Smith"),
("HR", 556, "Billy Bob"),
("Sales", 711, "Robert Hayek"),
("Marketing", 235, "Edward Jorgson"),
("Marketing", 236, "Christine Packard");

INSERT INTO salaries (salary, employee_id, employee_name)
values
(500, 123, "John Doe"),
(600, 211, "Jane Smith"),
(1000, 556, "Billy Bob"),
(400, 711, "Robert Hayek"),
(1200, 235, "Edward Jorgson"),
(200, 236, "Christine Packard");

select department_name, avg(salary) from salaries s
LEFT JOIN employees e on s.employee_id = e.employee_id
GROUP BY department_name;

select department_name, salary from salaries s
LEFT JOIN employees e on s.employee_id = e.employee_id;

## Display department_name with average_salary

SELECT 
    department_name,
    CAST(AVG(salary) AS DECIMAL (10 , 2 )) AS average_sal
FROM
    employees e
        LEFT JOIN
    salaries s ON e.employee_id = s.employee_id
GROUP BY department_name
HAVING (average_sal > 500)
ORDER BY average_sal DESC;


### Answer no 3:
## Display department_name only
SELECT 
    department_name
FROM
    (SELECT 
        department_name,
            CAST(AVG(salary) AS DECIMAL (10 , 2 )) AS average_sal
    FROM
        employees e
    LEFT JOIN salaries s ON e.employee_id = s.employee_id
    GROUP BY department_name
    HAVING (average_sal > 500)) AS T
    ORDER BY average_sal;

### Real condition: (average_sal >500)


######################
#### 4.	Create SQL Query that show Person Data with each their Deposito Amount. 
#### 	Data sorted by PERSON_ID.


