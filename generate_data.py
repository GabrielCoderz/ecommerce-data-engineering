import random
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(0)

num_customers = 100
num_products = 50
num_orders = 200

def generate_customers(num):
    customers = []
    for _ in range(num):
        customer = {
            "customer_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "registration_date": fake.date_this_decade()
        }
        customers.append(customer)
    return pd.DataFrame(customers)

def generate_products(num):
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Sports', 'Toys']
    products = []
    for _ in range(num):
        product = {
            "product_id": fake.uuid4(),
            "product_name": fake.word().capitalize(),
            "category": random.choice(categories),
            "price": round(random.uniform(10.0, 1000.0), 2),
            "stock": random.randint(1, 500)
        }
        products.append(product)
    return pd.DataFrame(products)

def generate_orders(num, customers_df, products_df):
    orders = []
    for _ in range(num):
        customer = customers_df.sample(1).iloc[0]
        product = products_df.sample(1).iloc[0]
        order = {
            "order_id": fake.uuid4(),
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "order_date": fake.date_this_year(),
            "quantity": random.randint(1, 5),
            "total_price": round(product["price"] * random.randint(1, 5), 2),
            "payment_method": random.choice(["Credit Card", "PayPal", "Bank Transfer"]),
            "status": random.choice(["Completed", "Pending", "Cancelled"])
        }
        orders.append(order)
    return pd.DataFrame(orders)

customers_df = generate_customers(num_customers)
products_df = generate_products(num_products)
orders_df = generate_orders(num_orders, customers_df, products_df)

customers_df.to_csv("data/customers.csv", index=False)
products_df.to_csv("data/products.csv", index=False)
orders_df.to_csv("data/orders.csv", index=False)

print("Dados gerados e salvos em arquivos CSV.")