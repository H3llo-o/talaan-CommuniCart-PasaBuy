import csv
import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

def seed_database(csv_filename):
    db = MySQLdb.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        passwd=os.getenv("MYSQL_PASSWORD", "DLq28@03LjpDQ2005!LjM"),
        db="pasabuy_db"
    )
    cursor = db.cursor()

    print("Connected to database. Starting data import...")

    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            cat_name = row['category'].strip()
            brand_name = row['brand'].strip()
            prod_name = row['product_name'].strip()
            unit = row['unit'].strip()
            qty = float(row['unit_qty'])
            price = float(row['price'])

            cursor.execute("INSERT IGNORE INTO categories (category_name) VALUES (%s)", (cat_name,))
            cursor.execute("SELECT category_id FROM categories WHERE category_name = %s", (cat_name,))
            category_id = cursor.fetchone()[0]

            brand_id = None
            if brand_name:
                cursor.execute("INSERT IGNORE INTO brands (brand_name) VALUES (%s)", (brand_name,))
                cursor.execute("SELECT brand_id FROM brands WHERE brand_name = %s", (brand_name,))
                brand_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO products (category_id, brand_id, product_name, unit, unit_per_qty, price)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (category_id, brand_id, prod_name, unit, qty, price))

    db.commit()
    cursor.close()
    db.close()
    print("Database successfully seeded with 500 items")

if __name__ == "__main__":
    seed_database("sample_products.csv")