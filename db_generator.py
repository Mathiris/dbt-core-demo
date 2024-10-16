import pandas as pd
import random
from faker import Faker
from google.oauth2 import service_account

# Initialise Faker
fake = Faker()

# Fonction pour générer des données customers
def generate_customers(num_customers):
    customers_data = []
    for _ in range(num_customers):
        customers_data.append({
            'customer_id': fake.uuid4(),  # Génère un ID unique
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        })
    return pd.DataFrame(customers_data)

# Fonction pour générer des données orders
def generate_orders(num_orders, customer_ids):
    orders_data = []
    for _ in range(num_orders):
        orders_data.append({
            'order_id': fake.uuid4(),  # Génère un ID unique
            'customer_id': random.choice(customer_ids),  # Associe un order à un client existant
            'order_date': fake.date_time_this_year(),  # Génère une date de commande cette année
            'status': random.choice(['pending', 'completed', 'cancelled'])  # Statut de la commande
        })
    return pd.DataFrame(orders_data)

# Fonction pour générer des données products
def generate_products(num_products):
    products_data = []
    for _ in range(num_products):
        products_data.append({
            'product_id': fake.uuid4(),  # Génère un ID unique
            'product_name': fake.word().capitalize(),  # Nom du produit
            'price': round(random.uniform(5.0, 100.0), 2),  # Prix aléatoire entre 5 et 100
            'stock': random.randint(0, 100)  # Stock aléatoire entre 0 et 100
        })
    return pd.DataFrame(products_data)

# Fonction pour générer des données order_items
def generate_order_items(num_items, order_ids, product_ids):
    order_items_data = []
    for _ in range(num_items):
        order_items_data.append({
            'order_item_id': fake.uuid4(),  # Génère un ID unique
            'order_id': random.choice(order_ids),  # Associe l'élément à une commande existante
            'product_id': random.choice(product_ids),  # Associe l'élément à un produit existant
            'quantity': random.randint(1, 5),  # Quantité entre 1 et 5
            'price': round(random.uniform(5.0, 100.0), 2)  # Prix aléatoire pour cet élément
        })
    return pd.DataFrame(order_items_data)

# Paramètres pour générer les données
num_customers = 10  # Nombre de clients
num_orders = 200  # Nombre de commandes
num_products = 50  # Nombre de produits
num_order_items = 500  # Nombre d'éléments de commande

# Génération des données
customers_df = generate_customers(num_customers)
orders_df = generate_orders(num_orders, customers_df['customer_id'].tolist())
products_df = generate_products(num_products)
order_items_df = generate_order_items(num_order_items, orders_df['order_id'].tolist(), products_df['product_id'].tolist())

# Affiche les données générées
print("Customers:")
print(customers_df)
print("\nOrders:")
print(orders_df)
print("\nProducts:")
print(products_df)
print("\nOrder Items:")
print(order_items_df)

# Configuration pour BigQuery
project_id = 'skilled-loader-436608-i6'
dataset_id = 'dbt_tutorial'

# Authentification (Assurez-vous que le fichier des credentials est correctement configuré)
credentials = service_account.Credentials.from_service_account_file('C:\\Users\\MathiasGIANOTTI\\Downloads\\dbt-key.json')

# Insertion des données dans les tables BigQuery
def insert_to_bq(df, table_name):
    table_id = f'{project_id}.{dataset_id}.{table_name}'
    df.to_gbq(destination_table=table_id, project_id=project_id, credentials=credentials, if_exists='replace')

# Insertion des DataFrames dans BigQuery
insert_to_bq(customers_df, 'custom_shop_customers')
insert_to_bq(orders_df, 'custom_shop_orders')
insert_to_bq(products_df, 'custom_shop_products')
insert_to_bq(order_items_df, 'custom_shop_order_items')

print("Les données ont été insérées dans BigQuery avec succès.")
