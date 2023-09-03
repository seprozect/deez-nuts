import sqlite3
import random

# Function to create the "warehouses" table and populate it with sample data
def create_and_populate_warehouses_table():
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS
        warehouses (
            "warehouse_no" INTEGER UNIQUE NOT NULL,
            "product_id" INTEGER NOT NULL,
            "capacity" NUMERIC NOT NULL,
            "location" TEXT NOT NULL,
            PRIMARY KEY("warehouse_no"),
            FOREIGN KEY("product_id") REFERENCES products("product_id")
        );"""
    )

    # Sample data to populate the table
    sample_data = [
        (101, random.randint(1, 10), 500, "New York"),
        (102, random.randint(1, 10), 400, "Los Angeles"),
        (103, random.randint(1, 10), 300, "Chicago"),
        (104, random.randint(1, 10), 600, "Houston"),
        (105, random.randint(1, 10), 350, "Miami"),
        (106, random.randint(1, 10), 450, "San Francisco"),
        (107, random.randint(1, 10), 550, "Seattle"),
        (108, random.randint(1, 10), 250, "Atlanta"),
        (109, random.randint(1, 10), 350, "Dallas"),
        (110, random.randint(1, 10), 500, "Boston"),
    ]

    # Insert the sample data into the table
    cursor.executemany("INSERT INTO warehouses VALUES (?, ?, ?, ?)", sample_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_warehouses_table()
