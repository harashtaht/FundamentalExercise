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
LEFT JOIN books b on a.book_name = b.book_name;

## SUM sold books based on author, order by minimum


-- SELECT u.id, u.name, u.email, u.phone FROM ku_user u
-- RIGHT JOIN ku_order o on o.user_id = u.id
-- WHERE o.status = 2;


