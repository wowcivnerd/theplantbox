sqlite3 theplantbox.db

DROP TABLE user;
DROP TABLE plant;
DROP TABLE plant_type;

CREATE TABLE user (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, name TEXT, email TEXT);
CREATE TABLE plant (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, planter INTEGER, plant_type INTEGER, planted_date INTEGER, FOREIGN KEY(planter) REFERENCES user(ID), FOREIGN KEY(plant_type) REFERENCES plant_type(ID));
CREATE TABLE plant_type (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, slug TEXT, content TEXT );

INSERT INTO user VALUES (NULL, 'codebrown', 'Ant Brown', 'ant@anbrown.com');
INSERT INTO user VALUES (NULL, 'wowcivdoom', 'Ollie Brown', '6789oliver@gmail.com');
INSERT INTO user VALUES (NULL, 'coco', 'Coco Brown', 'coco@anbrown.com');
INSERT INTO user VALUES (NULL, 'phoebe', 'Phoebe Brown', 'phoebe@anbrown.com');

INSERT INTO plant_type VALUES (NULL, 'Spring Onion', 'spring-onion', 'content of spring onion');
INSERT INTO plant_type VALUES (NULL, 'Potato', 'potato', 'content of spring onion');
INSERT INTO plant_type VALUES (NULL, 'Cauliflower', 'cauliflower', 'content of spring onion');
INSERT INTO plant_type VALUES (NULL, 'Carrot', 'carrot', 'content of spring onion');
INSERT INTO plant_type VALUES (NULL, 'Raspberry', 'raspberry', 'content of spring onion');
INSERT INTO plant_type VALUES (NULL, 'Srawberry', 'strawberry', 'content of spring onion');

INSERT INTO plant VALUES (NULL, 'Spring onions porch', 1, 1, 2022-04-01);

rm theplantbox.db