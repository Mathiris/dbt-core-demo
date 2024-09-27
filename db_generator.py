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

# Paramètres pour générer les données
num_customers = 10  # Nombre de clients
num_orders = 200  # Nombre de commandes

# Génération des données
customers_df = generate_customers(num_customers)
orders_df = generate_orders(num_orders, customers_df['customer_id'].tolist())

# Affiche les données générées
print("Customers:")
print(customers_df)
print("\nOrders:")
print(orders_df)

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

print("Les données ont été insérées dans BigQuery avec succès.")
