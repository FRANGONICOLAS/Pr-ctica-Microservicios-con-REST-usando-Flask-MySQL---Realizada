
CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);

INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");


CREATE TABLE products (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_name varchar(255),
    price varchar(255),
    origin  varchar(255)
);

INSERT INTO users VALUES(null, "Hp pavillion", "13000000", "Medellin"),
    (null, "Chontaduro", "3000000", "Cali");
