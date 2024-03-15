-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       state id INT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id),
       FOREIGN KEY(state) REFERENCES state(id)
);
