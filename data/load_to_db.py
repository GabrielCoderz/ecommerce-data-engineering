# Load data from csv files to OLTP Database

import pandas as pd
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="ecommerce_oltp",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def create_tables():
    commands = (
        """
        CREATE TABLE customers (
            customer_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            address TEXT,
            phone_number VARCHAR(50),
            registration_date DATE
        )
        """,
        """
        CREATE TABLE products (
            product_id VARCHAR(255) PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            category VARCHAR(50),
            price NUMERIC,
            stock INTEGER
        )
        """,
        """
        CREATE TABLE orders (
            order_id VARCHAR(255) PRIMARY KEY,
            customer_id VARCHAR(255) REFERENCES customers(customer_id),
            product_id VARCHAR(255) REFERENCES products(product_id),
            order_date DATE,
            quantity INTEGER,
            total_price NUMERIC,
            payment_method VARCHAR(50),
            status VARCHAR(50)
        )
        """
    )
    for command in commands:
        cursor.execute(command)
    conn.commit()

def load_csv_to_postgres(csv_file, table_name):
    df = pd.read_csv(csv_file)
    for i, row in df.iterrows():
        cols = ', '.join(list(row.index))
        vals = ', '.join([f"%s" for _ in range(len(row))])
        insert_query = sql.SQL(f"INSERT INTO {table_name} ({cols}) VALUES ({vals})")
        cursor.execute(insert_query, tuple(row))
    conn.commit()


create_tables()

load_csv_to_postgres("customers.csv", "customers")
load_csv_to_postgres("products.csv", "products")
load_csv_to_postgres("orders.csv", "orders")

cursor.close()
conn.close()

print("Dados carregados com sucesso no banco de dados PostgreSQL.")