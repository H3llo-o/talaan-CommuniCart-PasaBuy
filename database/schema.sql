CREATE DATABASE IF NOT EXISTS pasabuy_db;
USE pasabuy_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    brand_id INT,                     
    product_name VARCHAR(150) NOT NULL,
    unit VARCHAR(20) NOT NULL,           
    unit_per_qty DECIMAL(10,2) NOT NULL, 
    price DECIMAL(10,2) NOT NULL,        

    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE SET NULL
);