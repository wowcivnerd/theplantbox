create table antplant_page (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    slug TEXT,
    content TEXT,
    header TEXT
);

DROP TABLE antplant_page;

insert into antplant_page values (NULL, 'spring onion', 'spring-onion', 'Plant your spring onions in spring (get it) and autumn.', 'SPRING ONIONS!!!');

select * from antplant_page WHERE 1;

CREATE TABLE IF NOT EXISTS "Plant_page" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Slug STRING, Content TEXT, Title STRING);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE Plant (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name STRING, Planted_Date STRING, Plant_type INTEGER REFERENCES Plant_type (ID));
CREATE TABLE User (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Email TEXT);

CREATE TABLE user (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, name TEXT, email TEXT);
CREATE TABLE plant_type (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, content TEXT );
CREATE TABLE plant (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, planter INTEGER, plant_type INTEGER,FOREIGN KEY(planter) REFERENCES user(ID), FOREIGN KEY(plant_type) REFERENCES plant_type(ID));  --  planter is FK to Table "user",plant_type is FK to Table "plant_type"
