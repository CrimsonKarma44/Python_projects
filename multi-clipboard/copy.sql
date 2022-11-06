-- Active: 1665728307096@@127.0.0.1@3306@copy
CREATE DATABASE IF NOT EXISTS copy;

CREATE TABLE IF NOT EXISTS copy_list(
    id VARCHAR(20) NOT NULL UNIQUE,
    content VARCHAR(10000)
);

describe copy_list;

INSERT INTO copy_list VALUES("love", "dont cause a thing");

SELECT * FROM copy_list;

DELETE FROM copy_list WHERE id = "love";
DROP TABLE copy_list;

