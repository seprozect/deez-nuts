import sqlite3
import random

# Function to create the "products" table and populate it with sample data
def create_and_populate_products_table():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS
        products (
            "product_id"	INTEGER UNIQUE NOT NULL,
            "warehouse_id"	INTEGER NOT NULL,
            "product_brand" TEXT NOT NULL,
            "product_name"	TEXT NOT NULL,
            "existing_quantity"	NUMERIC NOT NULL,
            "cost_price" NUMERIC NOT NULL,
            "selling_price" NUMERIC NOT NULL,
            PRIMARY KEY("product_id" AUTOINCREMENT)
        );"""
    )

    # Sample data to populate the table
    sample_data = [
        (1, 101, "Kirkland Signature", "Almonds", random.randint(50, 200), 7.99, 15.99),
        (2, 102, "Wonderful", "Pistachios", random.randint(40, 180), 9.99, 18.99),
        (3, 103, "Blue Diamond", "Cashews", random.randint(30, 160), 8.49, 17.99),
        (4, 104, "Fiddyment Farms", "Pistachios", random.randint(20, 140), 10.99, 21.99),
        (5, 105, "Sincerely Nuts", "Walnuts", random.randint(25, 150), 6.99, 13.99),
        (6, 106, "Anna and Sarah", "Hazelnuts", random.randint(60, 220), 8.99, 16.99),
        (7, 107, "Terrasoul Superfoods", "Brazil Nuts", random.randint(35, 190), 9.99, 19.99),
        (8, 108, "Sincerely Nuts", "Pecans", random.randint(70, 240), 7.49, 14.49),
        (9, 109, "Farm Fresh Nuts", "Macadamia Nuts", random.randint(55, 210), 12.99, 25.99),
        (10, 110, "Oh! Nuts", "Dried Apricots", random.randint(45, 200), 5.99, 11.99),
    ]

    # Insert the sample data into the table
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)", sample_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_products_table()
