from db_config import get_db_connection


# USERS CRUD OPERATIONS
def create_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, email, user_password)
            VALUES (%s, %s, %s)
        """, (username, email, password))

        conn.commit()
        return cursor.lastrowid

    finally:
        cursor.close()
        conn.close()


def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT *
            FROM users
            WHERE email = %s
        """, (email,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def update_user(user_id, username, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE users
            SET username=%s,
                email=%s
            WHERE user_id=%s
        """, (username, email, user_id))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM users
            WHERE user_id=%s
        """, (user_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


# ==========================================
# USER INPUTS CRUD OPERATIONS
# ==========================================

def create_user_input(user_id, elderly, adult, teen, children, budget, ration_days):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO userinputs
            (user_id, elderly_count, adult_count,
             teen_count, children_count,
             budget, ration_days)
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            user_id,
            elderly,
            adult,
            teen,
            children,
            budget,
            ration_days
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        cursor.close()
        conn.close()


def get_user_inputs(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT *
            FROM userinputs
            WHERE user_id=%s
            ORDER BY request_date DESC
        """, (user_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def delete_user_input(input_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM userinputs
            WHERE input_id=%s
        """, (input_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()



# PRODUCTS CRUD OPERATIONS
def create_product(category_id, brand_id, general_name, product_name, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO products
            (category_id, brand_id, general_name, product_name, price)
            VALUES
            (%s,%s,%s,%s,%s)
        """,
        (
            category_id,
            brand_id,
            general_name,
            product_name,
            price
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        cursor.close()
        conn.close()


def get_products_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                p.product_id,
                p.product_name,
                p.general_name,
                p.price,
                b.brand_name,
                c.category_name

            FROM products p

            JOIN brands b
            ON p.brand_id = b.brand_id

            JOIN categories c
            ON p.category_id = c.category_id

            WHERE p.general_name = %s

            ORDER BY p.price ASC
        """, (category,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def update_product(product_id, category_id, brand_id, general_name, product_name, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE products
            SET
                category_id=%s,
                brand_id=%s,
                general_name=%s,
                product_name=%s,
                price=%s
            WHERE product_id=%s
        """,
        (
            category_id,
            brand_id,
            general_name,
            product_name,
            price,
            product_id
        ))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM products
            WHERE product_id=%s
        """, (product_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()

# GROCERY LIST CRUD OPERATIONS
def add_grocery_item(input_id, product_id, quantity, unit_price, subtotal):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO grocery_list
            (input_id, product_id, quantity, unit_price, subtotal)
            VALUES
            (%s,%s,%s,%s,%s)
        """,
        (
            input_id,
            product_id,
            quantity,
            unit_price,
            subtotal
        ))

        conn.commit()
        return cursor.lastrowid

    finally:
        cursor.close()
        conn.close()


def get_grocery_list(input_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                gl.grocery_list_id,
                gl.quantity,
                gl.unit_price,
                gl.subtotal,
                p.product_name,
                p.general_name,
                b.brand_name

            FROM grocery_list gl

            JOIN products p
            ON gl.product_id = p.product_id

            JOIN brands b
            ON p.brand_id = b.brand_id

            WHERE gl.input_id=%s
        """, (input_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def update_grocery_item(grocery_list_id, product_id, quantity, subtotal):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE grocery_list
            SET
                product_id=%s,
                quantity=%s,
                subtotal=%s
            WHERE grocery_list_id=%s
        """,
        (
            product_id,
            quantity,
            subtotal,
            grocery_list_id
        ))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_grocery_list(input_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM grocery_list
            WHERE input_id=%s
        """, (input_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()

# CATEGORIES CRUD OPERATIONS
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM categories")
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def create_category(category_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO categories(category_name)
            VALUES(%s)
        """, (category_name,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def update_category(category_id, category_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE categories
            SET category_name=%s
            WHERE category_id=%s
        """, (category_name, category_id))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_category(category_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM categories
            WHERE category_id=%s
        """, (category_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()

# BRANDS CRUD OPERATIONS
def get_brands():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM brands")
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def create_brand(brand_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO brands(brand_name)
            VALUES(%s)
        """, (brand_name,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def update_brand(brand_id, brand_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE brands
            SET brand_name=%s
            WHERE brand_id=%s
        """, (brand_name, brand_id))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_brand(brand_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM brands
            WHERE brand_id=%s
        """, (brand_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()

# STORES CRUD OPERATIONS

def create_store(store_name, latitude, longitude, contact_number, opening_hours, closing_hours):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO stores
            (store_name, latitude, longitude,
             contact_number, opening_hours, closing_hours)
            VALUES
            (%s,%s,%s,%s,%s,%s)
        """,
        (
            store_name,
            latitude,
            longitude,
            contact_number,
            opening_hours,
            closing_hours
        ))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def get_stores_by_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                s.store_id,
                s.store_name,
                s.latitude,
                s.longitude,
                sp.current_price,
                sp.stock

            FROM store_products sp

            JOIN stores s
            ON sp.store_id = s.store_id

            WHERE sp.product_id=%s
        """, (product_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def update_store(store_id, store_name, latitude, longitude, contact_number, opening_hours, closing_hours):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE stores
            SET
                store_name=%s,
                latitude=%s,
                longitude=%s,
                contact_number=%s,
                opening_hours=%s,
                closing_hours=%s
            WHERE store_id=%s
        """,
        (
            store_name,
            latitude,
            longitude,
            contact_number,
            opening_hours,
            closing_hours,
            store_id
        ))

        conn.commit()

    finally:
        cursor.close()
        conn.close()


def delete_store(store_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM stores
            WHERE store_id=%s
        """, (store_id,))

        conn.commit()

    finally:
        cursor.close()
        conn.close()