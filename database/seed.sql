USE pasabuy_db;

-- CLEAR TABLES
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE grocery_list;
TRUNCATE TABLE store_products;
TRUNCATE TABLE userinputs;
TRUNCATE TABLE products;
TRUNCATE TABLE brands;
TRUNCATE TABLE categories;
TRUNCATE TABLE stores;

SET FOREIGN_KEY_CHECKS = 1;

-- SAMPLE CATEGORIES DATA
INSERT INTO categories (category_name) VALUES
('Rice'),
('Chicken'),
('Pork'),
('Canned Goods'),
('Instant Noodles'),
('Bath Soap'),
('Shampoo');

-- SAMPLE BRANDS DATA
INSERT INTO brands (brand_name) VALUES
('NFA'),
('Sinandomeng'),
('Magnolia'),
('Bounty Fresh'),
('Monterey'),
('555'),
('Ligo'),
('Lucky Me!'),
('Payless'),
('Safeguard'),
('Bioderm'),
('Palmolive'),
('Cream Silk');

-- SAMPLE PRODUCTS DATA
INSERT INTO products
(category_id, brand_id, general_name, product_name, price)
VALUES

(1,1,'Rice','NFA Well-Milled Rice',45.00),
(1,2,'Rice','Sinandomeng Premium Rice',58.00),

(2,3,'Chicken','Magnolia Whole Chicken',210.00),
(2,4,'Chicken','Bounty Fresh Whole Chicken',205.00),

(3,5,'Pork','Monterey Pork Kasim',320.00),

(4,6,'Canned Goods','555 Sardines',19.50),
(4,7,'Canned Goods','Ligo Sardines',21.00),

(5,8,'Instant Noodles','Lucky Me! Beef',11.50),
(5,9,'Instant Noodles','Payless Xtra Big',9.00),

(6,10,'Bath Soap','Safeguard Pure White',31.25),
(6,11,'Bath Soap','Bioderm Yellow',18.00),

(7,12,'Shampoo','Palmolive Naturals Shampoo',8.50),
(7,13,'Shampoo','Cream Silk Conditioner',9.75);

-- SAMPLE STORES DATA
INSERT INTO stores
(store_name, latitude, longitude, contact_number, opening_hours, closing_hours)
VALUES

(
'SM Supermarket',
14.5995,
120.9842,
'02-8888-8888',
'08:00',
'21:00'
),

(
'Puregold',
14.6010,
120.9820,
'02-8777-7777',
'08:00',
'20:00'
),

(
'Robinsons Supermarket',
14.6035,
120.9800,
'02-8666-6666',
'09:00',
'21:00'
);

-- STORE PRODUCTS
INSERT INTO store_products
(store_id, product_id, stock, current_price)
VALUES

(1,1,120,45.00),
(1,2,50,58.00),
(1,3,30,210.00),
(1,4,20,205.00),
(1,5,15,320.00),
(1,6,200,19.50),
(1,7,150,21.00),
(1,8,100,11.50),
(1,9,120,9.00),
(1,10,75,31.25),
(1,11,90,18.00),
(1,12,100,8.50),
(1,13,80,9.75),

(2,1,90,46.00),
(2,4,30,203.00),
(2,6,80,19.75),
(2,8,90,11.25),
(2,10,50,31.00),

(3,2,40,57.50),
(3,3,25,212.00),
(3,7,110,20.50),
(3,9,100,8.75),
(3,11,60,18.25);

-- SAMPLE USER DATA
INSERT INTO users
(username, email, user_password)
VALUES
(
'testuser',
'test@example.com',
'test123'
);

-- SAMPLE USER INPUT DATA
INSERT INTO userinputs
(user_id, elderly_count, adult_count, teen_count, children_count, budget, ration_days)
VALUES
(
1,
1,
2,
1,
0,
3000.00,
7
);

-- SAMPLE GENERATED GROCERY LIST DATA

INSERT INTO grocery_list
(input_id, product_id, quantity, unit_price, subtotal)
VALUES

(1,1,5,45.00,225.00),
(1,4,2,205.00,410.00),
(1,6,10,19.50,195.00),
(1,9,12,9.00,108.00);