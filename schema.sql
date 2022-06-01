sqlite3 theplantbox.db

DROP TABLE user;
DROP TABLE plant;
DROP TABLE plant_type;

CREATE TABLE user (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,password TEXT, name TEXT, email TEXT);
CREATE TABLE plant (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, planter INTEGER, plant_type INTEGER, planted_date INTEGER, FOREIGN KEY(planter) REFERENCES user(ID), FOREIGN KEY(plant_type) REFERENCES plant_type(ID));
CREATE TABLE plant_type (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, slug TEXT, content TEXT, title TEXT );

-- using TEXT for the date because sqlite3 does not have a date section --
INSERT INTO user VALUES (NULL, 'codebrown', 'Ant Brown','password', 'ant@anbrown.com');
INSERT INTO user VALUES (NULL, 'wowcivdoom', 'Ollie Brown','password', '6789oliver@gmail.com');
INSERT INTO user VALUES (NULL, 'coco', 'Coco Brown','password', 'coco@anbrown.com');
INSERT INTO user VALUES (NULL, 'phoebe', 'Phoebe Brown','password', 'phoebe@anbrown.com');
INSERT INTO user VALUES (NULL, 'Bobolisious', 'Owen Nixon','password', 'owen.i.nixon@gmail.com');

INSERT INTO plant_type VALUES (NULL, 'Spring Onion', 'spring-onion', 'content of spring onion','Spring Onion');
INSERT INTO plant_type VALUES (NULL, 'Potato', 'potato', 'content of spring onion','Potato');
INSERT INTO plant_type VALUES (NULL, 'Cauliflower', 'cauliflower', 'content of spring onion', 'Cauliflower');
INSERT INTO plant_type VALUES (NULL, 'Carrot', 'carrot', 'content of spring onion', 'Carrot');
INSERT INTO plant_type VALUES (NULL, 'Raspberry', 'raspberry', 'content of spring onion', 'Raspberry');
INSERT INTO plant_type VALUES (NULL, 'Strawberry', 'strawberry', 'content of spring onion', 'Strawberry');
INSERT INTO plant_type VALUES (NULL, 'Owen', 'owen', 'content of owen, Carrot','Owen');
INSERT INTO plant_type VALUES (NULL, 'Wyatt', 'wyatt', 'content of Wyatt, Carro-Tea','Wyatt');


INSERT INTO plant VALUES (NULL, 'Spring onions porch', 1, 1, 2022-04-01);
INSERT INTO plant VALUES (NULL, 'Owen', 1, 1, 2022-06-02);

rm theplantbox.db