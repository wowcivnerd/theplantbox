sqlite3 theplantbox.db

DROP TABLE user;
DROP TABLE plant;
DROP TABLE plant_type;

CREATE TABLE user (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, name TEXT,password TEXT, email TEXT);
CREATE TABLE plant (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, planter INTEGER, plant_type INTEGER, planted_date INTEGER, FOREIGN KEY(planter) REFERENCES user(ID), FOREIGN KEY(plant_type) REFERENCES plant_type(ID));
CREATE TABLE plant_type (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, slug TEXT, content TEXT, title TEXT,image_location TEXT );

-- using TEXT for the date because sqlite3 does not have a date section --
INSERT INTO user VALUES (NULL, 'codebrown', 'Ant Brown','password', 'ant@anbrown.com');
INSERT INTO user VALUES (NULL, 'wowcivdoom', 'Ollie Brown','password', '6789oliver@gmail.com');
INSERT INTO user VALUES (NULL, 'coco', 'Coco Brown','password', 'coco@anbrown.com');
INSERT INTO user VALUES (NULL, 'phoebe', 'Phoebe Brown','password', 'phoebe@anbrown.com');
INSERT INTO user VALUES (NULL, 'Bobolisious', 'Owen Nixon','password', 'owen.i.nixon@gmail.com');

INSERT INTO plant_type VALUES (NULL, 'Test', 'testing', 'This page is a testing page designed by Ollie brown the lead programmer we are testing this without lorem Ipsum cause I am NOT a lazy fuck love youuuuuuu', 'Testing title', '/static/images/test.webp')
INSERT INTO plant_type VALUES (NULL, 'Spring Onion', 'spring-onion', 'content of spring onion','Spring Onion', '/static/images/spring-onion.jpg');
INSERT INTO plant_type VALUES (NULL, 'Potato', 'potato', 'Spring onions ','Potato','/static/images/potato.jpg');
INSERT INTO plant_type VALUES (NULL, 'Cauliflower', 'cauliflower', 'content of spring onion', 'Cauliflower','/static/images/cauliflower.jpg');
INSERT INTO plant_type VALUES (NULL, 'Carrot', 'carrot', 'Carrots are easy to grow once you understand what they do and don’t like. Carrots loathe being transplanted. As seedlings carrots roots are particularly fragile and will not tolerate disturbance, which is why you must always sow seeds in situ to prevent root disturbance. One exception to the rule is the ‘Roly Poly’ variety which can be transplanted.

Carrots get their bright orange colour from beta-carotene, which converts to vitamin A once eaten. They are also rich in antioxidants and fibre, making them healthy as well as tasty!

Refer to our Planting Calendar for when to plant and harvest in your region. 

Sow in batches in spring, summer and early autumn. Always use fresh seed. ', 'Carrot','/static/images/carrot.jpg');
INSERT INTO plant_type VALUES (NULL, 'Raspberry', 'raspberry', 'content of spring onion', 'Raspberry','/static/images/raspberry.jpg');
INSERT INTO plant_type VALUES (NULL, 'Strawberry', 'strawberry', 'content of spring onion', 'Strawberry','/static/images/strawberry.jpg');
INSERT INTO plant_type VALUES (NULL, 'Owen', 'owen', 'content of owen, Carrot','Owen','/static/images/owen.jpg');
INSERT INTO plant_type VALUES (NULL, 'Wyatt', 'wyatt', 'content of Wyatt, Carro-Tea','Wyatt','/static/images/wyatt.jpg');


INSERT INTO plant VALUES (NULL, 'Spring onions porch', 1, 1, 2022-04-01);
INSERT INTO plant VALUES (NULL, 'Owen', 1, 1, 2022-06-02);

rm theplantbox.db