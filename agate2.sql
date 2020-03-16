show databases;

use finalproject;

show tables;

CREATE TABLE authors
(
	author_name VARCHAR(255) NOT NULL PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL
    );
    
CREATE TABLE books
(
	book_name VARCHAR(255) NOT NULL PRIMARY KEY,
    sold_copies INT);
    
INSERT INTO authors (author_name, book_name) VALUES
("author_1", "book_1"),
("author_1", "book_2"),
("author_2", "book_3"),
("author_2", "book_4"),
("author_2", "book_5"),
("author_3", "book_6");

SELECT * FROM authors;


INSERT INTO ku_product (name, effective_date, effective_until, photo, price, status) VALUES
("Basic Lunch",DATE("2019-12-22"),DATE("2019-12-28"),"basic-lunch.jpg",20000.0,2),
