show databases;

use finalproject;

show tables;

CREATE TABLE 


CREATE TABLE ku_user_status
(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT current_timestamp,
    updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );