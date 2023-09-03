import sqlite3


class Products:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
        products (
            "product_id"	INTEGER UNIQUE NOT NULL,
            "warehouse_id"	INTEGER NOT NULL,
            "product_brand" TEXT NOT NULL,
            "product_name"	TEXT NOT NULL,
            "existing_quantity"	NUMERIC NOT NULL,
            "cost_price" NUMERIC NOT NULL,
            "selling_price" NUMERIC NOT NULL,
	        PRIMARY KEY("product_id" AUTOINCREMENT)
        );
        """)
        self.conn.commit()

    def fetch_all_rows(self):
        self.cur.execute(
            """SELECT * FROM products""")
        rows = self.cur.fetchall()
        return rows

    def fetch_by_rowid(self, rowid):
        self.cur.execute(
            "SELECT rowid, product_id, warehouse_id,product_brand, product_name, existing_quantity, cost_price, selling_price FROM products WHERE rowid=?",
            (rowid,))
        row = self.cur.fetchall()
        return row

    def fetch_by_product_id(self, product_id):
        self.cur.execute(
            "SELECT rowid, product_id, warehouse_id, product_brand, product_name, existing_quantity, cost_price, selling_price FROM products WHERE product_id=?",
            (product_id,))
        row = self.cur.fetchall()
        return row

    def insert(self, product_id, warehouse_id, product_brand, product_name, existing_quantity, cost_price,
               selling_price):
        self.cur.execute("""INSERT INTO products VALUES (?, ?, ?, ?, ?, ?,?)""",
                         (product_id, warehouse_id, product_brand, product_name, existing_quantity, cost_price,
                          selling_price))
        self.conn.commit()

    def remove(self, product_id):
        self.cur.execute(
            "DELETE FROM products WHERE product_id=?", (product_id,))
        self.conn.commit()

    def update(self, rowid, product_id, warehouse_id, product_brand, product_name, existing_quantity, cost_price,
               selling_price):
        self.cur.execute("""UPDATE products SET
            product_id=?,
            warehouse_id=?,
            product_brand=?,
            product_name=?,
            existing_quantity=?,
            cost_price=?,
            selling_price=?
        WHERE
            rowid=?
        """, (
            product_id, warehouse_id, product_brand, product_name, existing_quantity, cost_price, selling_price, rowid))
        self.conn.commit()

    # Defining a destructor to close connections
    def __del__(self):
        self.conn.close()


import sqlite3


class Supplier:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
        supplier (
            "sid" INTEGER UNIQUE NOT NULL,
            "product_id" INTEGER NOT NULL,
            "contact_no" NUMERIC NOT NULL,
            "name" TEXT NOT NULL,
            "rating" TEXT NOT NULL,
            PRIMARY KEY("sid")
            FOREIGN KEY("product_id") REFERENCES products("product_id")
        );
        """)
        self.conn.commit()

    def fetch_all_rows(self):
        self.cur.execute("SELECT * FROM supplier")
        rows = self.cur.fetchall()
        return rows

    def fetch_by_warehouse_no(self, sid):
        self.cur.execute("SELECT * FROM supplier WHERE sid=?", (sid,))
        row = self.cur.fetchone()
        return row

    def insert(self, sid, product_id, contact_no, name, rating):
        self.cur.execute("INSERT INTO supplier VALUES (?, ?, ?, ?)", (sid, product_id, contact_no, name, rating))
        self.conn.commit()

    def remove(self, sid):
        self.cur.execute("DELETE FROM supplier WHERE sid=?", (sid,))
        self.conn.commit()

    def update(self, sid, product_id, contact_no, name, rating):
        self.cur.execute("UPDATE supplier SET product_id=?, contact_no=?, name=?, rating=? WHERE sid=?",
                         (sid, product_id, contact_no, name, rating))
        self.conn.commit()

class Warehouse:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
        warehouses (
            "warehouse_no" INTEGER UNIQUE NOT NULL,
            "product_id" INTEGER NOT NULL,
            "capacity" NUMERIC NOT NULL,
            "location" TEXT NOT NULL,
            PRIMARY KEY("warehouse_no")
            FOREIGN KEY("product_id") REFERENCES products("product_id")
        );
        """)
        self.conn.commit()

    def fetch_all_rows(self):
        self.cur.execute("SELECT * FROM warehouses")
        rows = self.cur.fetchall()
        return rows

    def fetch_by_warehouse_no(self, warehouse_no):
        self.cur.execute("SELECT * FROM warehouses WHERE warehouse_no=?", (warehouse_no,))
        row = self.cur.fetchone()
        return row

    def insert(self, warehouse_no, product_id, capacity, location):
        self.cur.execute("INSERT INTO warehouses VALUES (?, ?, ?, ?)",
                         (warehouse_no, product_id, capacity, location))
        self.conn.commit()

    def remove(self, warehouse_no):
        self.cur.execute("DELETE FROM warehouses WHERE warehouse_no=?", (warehouse_no,))
        self.conn.commit()

    def update(self, warehouse_no, product_id, capacity, location):
        self.cur.execute("UPDATE warehouses SET product_id=?, capacity=?, location=? WHERE warehouse_no=?",
                         (product_id, capacity, location, warehouse_no))
        self.conn.commit()

    # Defining a destructor to close connections
    def __del__(self):
        self.conn.close()
